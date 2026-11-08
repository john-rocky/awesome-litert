#!/usr/bin/env python3
"""Build models.json and README.md for the OlliteRT model source in this directory.

OlliteRT (https://github.com/NightMean/OlliteRT) reads models.json from its raw URL and lists the
models in its Models tab. Sizes and commit hashes come from the Hugging Face API. Python standard
library only.

    python3 make_ollitert_source.py          # write both files
    python3 make_ollitert_source.py --check  # print what would change, write nothing

A row in PICKS means the file loaded and answered on LiteRT-LM 0.16.1, the runtime in OlliteRT
0.9.7-beta.1. After uploading a new bundle: run that check, add a row, run this script, commit.
contentVersion goes up only when the list changes.
"""
import json
import os
import re
import sys
import urllib.request

HF = "https://huggingface.co"
ORG = "litert-community"
HERE = os.path.dirname(os.path.abspath(__file__))
JSON_PATH = os.path.join(HERE, "models.json")
README_PATH = os.path.join(HERE, "README.md")
RAW_URL = "https://raw.githubusercontent.com/john-rocky/awesome-litert/main/ollitert/models.json"
OFFICIAL_URL = "https://raw.githubusercontent.com/NightMean/OlliteRT/main/model_allowlists/v1/model_allowlist.json"
LITERT_LM = "https://github.com/google-ai-edge/LiteRT-LM"
# OlliteRT 0.9.6 ships LiteRT-LM 0.11.0; the list was checked on 0.16.1, which arrived in 0.9.7.
MIN_APP_VERSION = "0.9.7"

GPU_CPU = "gpu,cpu"

# repo in litert-community, file, context tokens from the file's header, options.
# Options: image, thinking (the template reads enable_thinking), accelerators, vision (the
# accelerator for the vision encoder), note (one sentence added to the description).
PICKS = [
    ("DeepSeek-R1-Distill-Qwen-7B", "DeepSeek-R1-Distill-Qwen-7B_q4_block32_ekv4096.litertlm", 4096, {}),
    ("FastContext-1.0-4B-SFT", "model.litertlm", 4096, {}),
    ("G9v3-3B", "G9v3-3B_int4.litertlm", 4096, {"thinking": True}),
    ("granite-3.0-1b-a400m-instruct", "granite-3.0-1b-a400m-instruct_int8.litertlm", 2048, {}),
    ("granite-4.0-micro", "granite-4.0-micro_int4.litertlm", 4096, {}),
    ("granite-4.1-3b", "granite-4.1-3b_int4.litertlm", 4096, {}),
    ("granite-4.1-8b", "granite-4.1-8b_int4.litertlm", 4096, {}),
    ("granite-4.2-3b", "granite-4.2-3b_int4.litertlm", 4096, {"thinking": True}),
    ("granite-docling-258M", "granite-docling-258M.litertlm", 4096,
     {"image": True, "accelerators": "cpu", "vision": "cpu",
      "note": "Converts document images to structured text; it is not a general chat model. CPU only."}),
    ("InternVL3-1B", "InternVL3-1B.litertlm", 2048, {"image": True}),
    ("InternVL3-2B", "InternVL3-2B.litertlm", 2048, {"image": True}),
    ("InternVL3_5-1B", "model.litertlm", 2048, {"image": True}),
    ("InternVL3_5-2B", "model.litertlm", 2048, {"image": True}),
    ("InternVL3_5-4B", "model.litertlm", 2048, {"image": True}),
    ("Jan-nano", "model.litertlm", 4096, {}),
    ("LLaVA-OneVision-0.5B", "LLaVA-OneVision-0.5B.litertlm", 2048, {"image": True}),
    ("Mage-VL", "Mage-VL.litertlm", 2048, {"image": True}),
    ("Mage-VL-Cowork", "Mage-VL-Cowork_vision-fp16.litertlm", 4096, {"image": True, "thinking": True, "vision": "cpu"}),
    ("Ministral-3-3B-Instruct-2512", "Ministral-3-3B-Instruct-2512_q4_block32_ekv4096.litertlm", 4096, {}),
    ("Ministral-3-3B-Reasoning-2512", "model.litertlm", 4096, {}),
    ("Ministral-3-8B-Instruct-2512", "Ministral-3-8B-Instruct-2512_int4.litertlm", 4096, {}),
    ("MNN-Pocket-0.3B", "MNN-Pocket-0.3B_int8_ekv2048.litertlm", 2048,
     {"accelerators": "cpu", "note": "CPU only: LiteRT-LM 0.16.1, the runtime in OlliteRT 0.9.7, does not run this file on the GPU."}),
    ("Nanbeige4.1-3B", "model.litertlm", 4096, {}),
    ("Nanbeige4.2-3B", "model_fp32act.litertlm", 4096, {}),
    ("North-Micro-Vision-Instruct", "North-Micro-Vision-Instruct_wi8.litertlm", 4096, {"image": True}),
    ("NVIDIA-Nemotron-3.5-Bolt-E4B", "NVIDIA-Nemotron-3.5-Bolt-E4B_int4.litertlm", 2048, {"thinking": True}),
    ("NVIDIA-Nemotron-Labs-Dory1.0-4B", "NVIDIA-Nemotron-Labs-Dory1.0-4B_int4.litertlm", 2048, {"thinking": True}),
    ("OLMo-2-1B-Instruct", "OLMo-2-1B-Instruct_q4_block32_ekv4096.litertlm", 4096, {}),
    ("Ovis2.5-2B", "Ovis2.5-2B.litertlm", 2048, {"image": True}),
    ("PaddleOCR-VL-1.6", "PaddleOCR-VL-1.6.litertlm", 4096,
     {"image": True, "note": "Reads documents: send an image with a task prompt such as `OCR:`. It does not answer general questions."}),
    ("Phi-4-mini-reasoning", "model.litertlm", 4096, {}),
    ("Polaris-4B-Preview", "model.litertlm", 4096, {}),
    ("Qwen2-VL-2B", "Qwen2-VL-2B.litertlm", 4096, {"image": True}),
    ("Qwen2.5-Coder-1.5B-Instruct", "Qwen2.5-Coder-1.5B-Instruct_int4.litertlm", 4096, {}),
    ("Qwen3-4B-Thinking-2507", "model.litertlm", 4096, {}),
    ("sarashina2.2-0.5b-instruct-v0.1", "sarashina2.2-0.5b-instruct-v0.1_int4.litertlm", 4096,
     {"note": "A Japanese model; its English answers are weaker."}),
    ("sarashina2.2-1b-instruct-v0.1", "sarashina2.2-1b-instruct-v0.1_int4.litertlm", 4096, {"note": "A Japanese model."}),
    ("SmolVLM2-2.2B", "SmolVLM2-2.2B.litertlm", 2048, {"image": True}),
    ("SmolVLM2-500M", "SmolVLM2-500M.litertlm", 2048, {"image": True}),
    ("Spark-X2.5-1.7B", "Spark-X2.5-1.7B_int8.litertlm", 4096, {"thinking": True}),
    ("Spark-X2.5-4B", "Spark-X2.5-4B_int4.litertlm", 4096, {"thinking": True}),
    ("Spark-X2.6-1.7B", "Spark-X2.6-1.7B_int8.litertlm", 4096, {"thinking": True}),
    ("Spark-X2.6-4B", "Spark-X2.6-4B_int4.litertlm", 4096, {"thinking": True}),
    ("VibeThinker-3B", "model.litertlm", 4096, {}),
    ("WeVisOne-VL-2B", "WeVisOne-VL-2B_int8.litertlm", 2048, {"image": True}),
]

# Files whose main version moved to external weights on 2026-11-09 (the weights sit in a TFLiteWeights section at the
# end of the file; the answers are the same). Their cards give LiteRT-LM 0.19.0 as the Android floor for such a file,
# and OlliteRT 0.9.7 ships 0.16.1, so the list keeps serving the commit each file was checked at instead of main.
# Remove the whole dict when OlliteRT ships LiteRT-LM 0.19.0. A row may come off earlier once the file on main has
# loaded and answered through OlliteRT (LiteRT-LM 0.16.1) on a phone.
PINNED = {
    "granite-3.0-1b-a400m-instruct": "9571313d93a94e41693d8e9a1d35b0450bb30736",
    "granite-4.0-micro": "894dc75514012b6fd6d3970a47449381abc6a8fd",
    "granite-4.1-8b": "99579c31c55a6d1966e3daef1c04989954530d36",
    "granite-docling-258M": "52db61f1ca7a5f2d60f43a59900f3b84eaca8951",
    "InternVL3-1B": "0a181a9ee4386c9569c2bf3e67b002462543691d",
    "InternVL3-2B": "0c77b1e679335dd4ce87937d061ecf6d07e10a0c",
    "InternVL3_5-1B": "41b14fd8db47eea38e69b7b9b07b225993b073d2",
    "InternVL3_5-2B": "e596184e78525c12697e54890f00dd961c3d1916",
    "InternVL3_5-4B": "7949fcebc8cc9b2c76df1d9fee829d6101c9f25e",
    "LLaVA-OneVision-0.5B": "bf4d93272878ad7de02800c6b7e2bbe58d8c0008",
    "Mage-VL": "36e7fe01a3e18015b29b3e42dc3f6f77dc2ed126",
    "Mage-VL-Cowork": "38bf428bca33e54cd94a8fa979764ba9268df9ac",
    "Ministral-3-8B-Instruct-2512": "f61f6659d4e3313134e5dda51eeba8771235d4bc",
    "MNN-Pocket-0.3B": "475036b0fe8bde0211b9eaf0fad1fe1bf77a3ce9",
    "North-Micro-Vision-Instruct": "d812a8a7219af9351c69e610ee53eec22641328b",
    "NVIDIA-Nemotron-3.5-Bolt-E4B": "6cfb168af35bd4052fab21fe2f8ab35b656f1111",
    "NVIDIA-Nemotron-Labs-Dory1.0-4B": "42ee53aee099800d3895f4c26ad0c1c822d5d9f0",
    "Ovis2.5-2B": "ccb799150dff7a8023c1c539ac0e020df2201430",
    "PaddleOCR-VL-1.6": "2a58a00126eaa2159b1a4368fb56ef5ed522fd57",
    "Qwen2-VL-2B": "be3809f1d80e2adac2ad929bf483c960ca907023",
    "SmolVLM2-2.2B": "29065c4a7d7f129cf634cf435563d4d7c8d20426",
    "SmolVLM2-500M": "fb4a60507747543d408de0c0ccec13e5a23c9c17",
    "Spark-X2.6-1.7B": "344d1a267592b1f3f51efd647cd1b21a408beacb",
    "Spark-X2.6-4B": "9d37e8e347c38f6a2511e4d0be10a92e18c235b8",
    "WeVisOne-VL-2B": "54c673c89dfc499d807ffd63b6b50cd53c72ed50",
}

DEVICE_RUN = ("Six of them also ran through OlliteRT 0.9.7-beta.1 on a Pixel 11 Pro: SmolVLM2-500M, "
              "sarashina2.2-0.5b-instruct-v0.1, Spark-X2.6-1.7B, PaddleOCR-VL-1.6 and DeepSeek-R1-Distill-Qwen-7B "
              "on the GPU, MNN-Pocket-0.3B on the CPU.")

NOT_LISTED = """\
## Not listed

- **Models with recurrent state** (LFM2 and LFM2.5, Qwen3.5, Falcon-H1, Zamba2, granite-4.0-h and others). OlliteRT keeps one engine and opens a new conversation for each request. On LiteRT-LM 0.16.1 such a model carries its state into the next conversation ([LiteRT-LM #3165](https://github.com/google-ai-edge/LiteRT-LM/issues/3165)), so an earlier request can change a later answer.
- **Files too large for a phone**: Qwen2.5-VL-72B, Muse-Glimmer-30B and Qwen3-30B-A3B (over 20 GB each).
- **Unlimited-OCR-2**: it takes no prompt and expects a padded page image, so a chat request gets no useful answer.
- **SmolLM3-3B**: on a Pixel 11 Pro GPU its thinking fell into repetition on a simple question, and another answer ended in garbled text.
- **Olmo-3-7B-Think**: on a Pixel 11 Pro it generated about 4 tokens per second, so its thinking alone passed OlliteRT's 120-second limit on a request.
"""


LICENSES = {}


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "make_ollitert_source"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read())


def min_memory_gb(size):
    # OlliteRT's steps for an imported model (ModelFactory.estimateMinMemoryGb), but 12 GB from 2 GiB
    # instead of 3: the model cards record GPU engines of 2-3 GB files running out of memory on 8 GB phones.
    gib = size / 2**30
    return 6 if gib < 1 else 8 if gib < 2 else 12 if gib < 5 else 16


def build_entry(repo, file, ctx, opts, previous):
    repo_id = f"{ORG}/{repo}"
    info = fetch(f"{HF}/api/models/{repo_id}")
    if info.get("gated"):
        sys.exit(f"{repo_id} is gated; OlliteRT would need a token")
    rev = PINNED.get(repo, "main")
    tree = fetch(f"{HF}/api/models/{repo_id}/tree/{rev}?expand=true")
    row = next((t for t in tree if t["path"] == file), None)
    if row is None:
        sys.exit(f"{repo_id} has no {file} at {rev}")
    if rev != "main" and row["lastCommit"]["id"] != rev:
        sys.exit(f"{repo_id}: {file} at {rev} was last changed by {row['lastCommit']['id']}, not by the pinned commit")
    card = info.get("cardData") or {}
    base = card.get("base_model")
    base = base[0] if isinstance(base, list) else base
    LICENSES[repo_id] = card.get("license_name") or card.get("license")
    desc = (f"A variant of [{base}]({HF}/{base}) ready for deployment on Android using "
            f"[LiteRT-LM]({LITERT_LM}). {ctx:,}-token context.")
    if opts.get("note"):
        desc += " " + opts["note"]
    config = {"topK": 40, "topP": 0.95, "temperature": 0.7, "maxContextLength": ctx, "maxTokens": ctx,
              "accelerators": opts.get("accelerators", GPU_CPU)}
    if opts.get("image"):
        config["visionAccelerator"] = opts.get("vision", "gpu")
    entry = {"name": repo, "modelId": repo_id, "modelFile": file, "commitHash": row["lastCommit"]["id"],
             "description": desc, "sizeInBytes": row["size"],
             "minDeviceMemoryInGb": min_memory_gb(row["size"]), "defaultConfig": config}
    if opts.get("image"):
        entry["llmSupportImage"] = True
    if opts.get("thinking"):
        entry["llmSupportThinking"] = True
    entry["minAppVersion"] = MIN_APP_VERSION
    # A changed file stays usable: OlliteRT marks the older download as updatable instead of missing.
    prev = previous.get(repo_id)
    if prev:
        older = list(prev.get("updatableModelFiles", []))
        if prev["commitHash"] != entry["commitHash"]:
            older.append({"fileName": prev["modelFile"], "commitHash": prev["commitHash"]})
        if older:
            entry["updatableModelFiles"] = older
            entry["updateInfo"] = prev.get("updateInfo") if prev["commitHash"] == entry["commitHash"] else "The file was updated."
    return entry


def check_list(models):
    official = {m["modelId"] for m in fetch(OFFICIAL_URL)["models"]}
    names = set()
    for m in models:
        norm = re.sub(r"[^a-zA-Z0-9]", "_", m["name"])
        if "/" in m["name"] or norm in names or m["modelId"] in official:
            sys.exit(f"bad entry: {m['name']} ({m['modelId']})")
        names.add(norm)


def gb(size):
    return f"{size / 1e9:.2f} GB"


def readme(models):
    lines = [
        "# OlliteRT model source",
        "",
        f"{len(models)} LiteRT-LM chat models from [{ORG}]({HF}/{ORG}) for [OlliteRT](https://github.com/NightMean/OlliteRT), "
        "an Android app that serves a model on the phone over an OpenAI-compatible API.",
        "",
        "1. In OlliteRT, open Settings → Model Sources → + → From model list URL (.json).",
        f"2. Paste `{RAW_URL}`.",
        "3. Open the Models tab, download a model and tap Start Server.",
        "",
        "Every file below loaded and answered on LiteRT-LM 0.16.1, the runtime in OlliteRT 0.9.7-beta.1, on a Mac CPU. "
        f"{DEVICE_RUN} The Runs on column comes from the Android records on each model card, "
        "or from the row's note where the app's runtime is the limit. "
        "The list sets `minAppVersion` to 0.9.7. "
        "Generated by [`make_ollitert_source.py`](make_ollitert_source.py).",
        "",
        "| Model | Download | Input | Context | Runs on | Suggested RAM | License |",
        "|---|---|---|---|---|---|---|",
    ]
    for m in sorted(models, key=lambda m: m["name"].lower()):
        cfg = m["defaultConfig"]
        kind = "Text, image" if m.get("llmSupportImage") else "Text"
        runs = cfg["accelerators"].replace("gpu", "GPU").replace("cpu", "CPU").replace(",", ", ")
        lines.append(f"| [{m['name']}]({HF}/{m['modelId']}) | {gb(m['sizeInBytes'])} | {kind} | {cfg['maxContextLength']:,} "
                     f"| {runs} | {m['minDeviceMemoryInGb']} GB | {LICENSES[m['modelId']]} |")
    lines += ["", "Some models think before they answer. OlliteRT returns that text inside `content` as `<think>…</think>`. "
              "It stops a request after 120 seconds by default; for a large model or long thinking, raise "
              "Chat completions timeout under Settings → Advanced Settings."]
    return "\n".join(lines) + "\n\n" + NOT_LISTED


def main():
    check_only = "--check" in sys.argv
    old = {}
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH) as f:
            old = json.load(f)
    previous = {m["modelId"]: m for m in old.get("models", [])}
    models = [build_entry(repo, file, ctx, opts, previous) for repo, file, ctx, opts in PICKS]
    models.sort(key=lambda m: m["name"].lower())
    check_list(models)
    changed = models != old.get("models")
    doc = {
        "schemaVersion": 1,
        "contentVersion": old.get("contentVersion", 0) + (1 if changed else 0),
        "sourceName": "john-rocky LiteRT models",
        "sourceDescription": f"LiteRT-LM chat models on {ORG}, converted by john-rocky and checked on LiteRT-LM 0.16.1.",
        "sourceIconUrl": "",
        "models": models,
    }
    print(f"{len(models)} models, contentVersion {doc['contentVersion']}, {'changed' if changed else 'no change'}")
    if check_only:
        for m in models:
            p = previous.get(m["modelId"])
            if p != m:
                print(("update " if p else "new    ") + m["name"])
        return
    with open(JSON_PATH, "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
        f.write("\n")
    with open(README_PATH, "w") as f:
        f.write(readme(models))


if __name__ == "__main__":
    main()
