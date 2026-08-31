# Awesome LiteRT

> Curated resources for Google's **LiteRT** on-device ML stack — the runtime (successor to
> TensorFlow Lite), the LiteRT-LM inference engine for language models, conversion and
> quantization tooling, ready-to-run models, bindings for a dozen platforms, sample apps,
> and engineering notes.

LiteRT runs models on CPU / GPU / NPU across Android, iOS, macOS, Linux, the browser and
embedded boards. Classic models ship as `.tflite`, language models as `.litertlm` bundles for
[LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM). This list tracks the ecosystem
growing around both.

*Scope: the LiteRT era (September 2024 onward). The wider TensorFlow Lite back-catalog is out of
scope. PRs welcome — see [Contributing](#contributing).*

---

## Contents

- [Official](#official)
- [Getting started](#getting-started)
- [Running models in your app](#running-models-in-your-app)
- [Bindings & wrappers](#bindings--wrappers)
- [Models](#models)
- [Conversion & quantization](#conversion--quantization)
- [Serving](#serving)
- [Benchmarks & engineering notes](#benchmarks--engineering-notes)
- [Learning](#learning)

## Official

- [google-ai-edge/LiteRT](https://github.com/google-ai-edge/LiteRT) — The runtime: CompiledModel and Interpreter APIs, GPU/NPU acceleration, Android · iOS · desktop · embedded.
- [google-ai-edge/LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM) — Production LLM inference engine over LiteRT: `.litertlm` bundles, prefill/decode pipelines, GPU and NPU backends, C++ / C APIs and a Python CLI (`pip install litert-lm`).
- [google-ai-edge/litert-torch](https://github.com/google-ai-edge/litert-torch) — The official PyTorch path: `torch.export`-based conversion, `export_hf` one-command Hugging Face export, quantization recipes.
- [google-ai-edge/LiteRT-CLI](https://github.com/google-ai-edge/LiteRT-CLI) — `litert` command: convert, quantize, benchmark and run models (including image input) from the terminal; `pip install litert-cli-nightly`.
- [google-ai-edge/ai-edge-quantizer](https://github.com/google-ai-edge/ai-edge-quantizer) — Post-training quantization for LiteRT models: dynamic / weight-only / static recipes, blockwise int4.
- [google-ai-edge/litert-samples](https://github.com/google-ai-edge/litert-samples) — Official sample apps and model recipes: Android/iOS apps, Tensor API implementations, TTS/ASR/vision samples, agent skills and utilities.
- [google-ai-edge/gallery](https://github.com/google-ai-edge/gallery) — The AI Edge Gallery app: try on-device GenAI models on your own phone, straight from a model list.
- [LiteRT documentation](https://ai.google.dev/edge/litert) — Official docs: quickstarts, per-platform guides, NPU delegation.

## Getting started

- [AI Edge Gallery](https://github.com/google-ai-edge/gallery) — Install the app, pick a model, run it on-device; the shortest path to seeing LiteRT work.
- One command for an LLM on any machine with Python: `pip install litert-lm` then `litert-lm run --from-huggingface-repo=litert-community/<model> <model>.litertlm --prompt "..."` — models stream from [litert-community](https://huggingface.co/litert-community).
- [LiteRT quickstarts](https://ai.google.dev/edge/litert) — Android (Kotlin), iOS, Python.

## Running models in your app

- [LiteRT CompiledModel API](https://github.com/google-ai-edge/LiteRT) — The current-generation API for classic models (see [Official](#official)).
- [john-rocky/swift-litert-lm](https://github.com/john-rocky/swift-litert-lm) — SwiftPM package for LiteRT-LM on iPhone/Mac, including an Apple FoundationModels-compatible adapter (guided generation, tool calling) shipped with LiteRT-LM v0.15.0.
- [dineshsoudagar/local-llms-on-android](https://github.com/dineshsoudagar/local-llms-on-android) — Offline chat app running Gemma, Qwen and LLaMA on Android with LiteRT.
- [andrisgauracs/LiteRT.js-Mocap](https://github.com/andrisgauracs/LiteRT.js-Mocap) — Real-time human pose estimation entirely in the browser with LiteRT.js.
- [Mohd-Mursaleen/LiteRT-Server](https://github.com/Mohd-Mursaleen/LiteRT-Server) — Native Kotlin app running the Gemma 4 E2B multimodal LLM on-device via LiteRT-LM.
- [soniqo/speech-core](https://github.com/soniqo/speech-core) — On-device VAD / streaming STT / TTS / diarization voice-agent pipeline in C++17 (ONNX + LiteRT); Linux, Windows, Android.
- [ShadAdman/EdgeRt](https://github.com/ShadAdman/EdgeRt) — Run models across tflite / LiteRT / ExecuTorch runtimes on edge devices from one harness.
- [NSTiwari/YOLOv10-LiteRT-Android](https://github.com/NSTiwari/YOLOv10-LiteRT-Android) — YOLOv10 converted to `.tflite` and deployed on Android.
- [stevan-milovanovic/LiteRT-for-Android](https://github.com/stevan-milovanovic/LiteRT-for-Android) — Image classification, image captioning and LLM inference on Android.
- [iFleey/PPOCRv5-Android](https://github.com/iFleey/PPOCRv5-Android) — Real-time OCR app with PP-OCRv5 on LiteRT.
- [alphasoftwarepy/as-core](https://github.com/alphasoftwarepy/as-core) — Local AI runtime for edge hardware built on LiteRT-LM and Gemma.

## Bindings & wrappers

Community bindings that take LiteRT / LiteRT-LM beyond C++, Kotlin, Swift and Python:

- [leitingzi/kmplitert](https://github.com/leitingzi/kmplitert) — Kotlin Multiplatform: unified type-safe LiteRT API across platforms.
- [hung-yueh/react-native-litert-lm](https://github.com/hung-yueh/react-native-litert-lm) — React Native: LiteRT-LM via Nitro Modules.
- [mylovelycodes/LiteRTLM-Swift](https://github.com/mylovelycodes/LiteRTLM-Swift) — Swift: async/await wrapper over the LiteRT-LM C API for iOS.
- [vladimirvivien/litertlm-go](https://github.com/vladimirvivien/litertlm-go) — Go bindings for LiteRT-LM.
- [offbit-ai/LiteRT](https://github.com/offbit-ai/LiteRT) — Rust bindings for the LiteRT runtime.
- [maceip/litert-lm-rs](https://github.com/maceip/litert-lm-rs) — Rust: safe idiomatic wrapper for LiteRT-LM.
- [OrihuelaConde/LiteRtLmSharp](https://github.com/OrihuelaConde/LiteRtLmSharp) — .NET bindings for LiteRT-LM: Windows, Linux, Android, macOS, MAUI.
- [hugocornellier/flutter_litert](https://github.com/hugocornellier/flutter_litert) — Flutter plugin for LiteRT with bundled native libraries.
- [Mutesa-Cedric/react-litert](https://github.com/Mutesa-Cedric/react-litert) — React library for on-device inference with LiteRT.
- [Uralstech/UAI.LiteRTLM](https://github.com/Uralstech/UAI.LiteRTLM) — Unity: LiteRT-LM inference in Unity apps.
- [Leuconoe/LiteRT-LM-Unity](https://github.com/Leuconoe/LiteRT-LM-Unity) — Unity integration with Android GPU/OpenCL and function calling.
- [winyunq/LiteRT-LM-Unreal](https://github.com/winyunq/LiteRT-LM-Unreal) — Unreal Engine 5 plugin for local LLMs in games.
- [helenkwok/expo-litert-lm](https://github.com/helenkwok/expo-litert-lm) — Expo Modules bindings for LiteRT-LM.
- [sagar-develop/litertlm-kmp](https://github.com/sagar-develop/litertlm-kmp) — Kotlin Multiplatform engine with stateful KV-cache chat sessions.
- [Luxshan2000/LiteRTLM-Swift-SDK](https://github.com/Luxshan2000/LiteRTLM-Swift-SDK) — Swift SDK: text, vision, audio and tool calling on CPU + GPU (Metal).
- [kursor1337/KTensorFlow](https://github.com/kursor1337/KTensorFlow) — Kotlin Multiplatform library for using LiteRT models from common code.
- [nikunjsingh93/ondevice-studio](https://github.com/nikunjsingh93/ondevice-studio) — OnDevice Studio is an Android app that helps you build and preview web apps (HTML/CSS/JS) directly on your device using local AI workflows. Import a compatib...

## Models

- [Hugging Face: litert-community](https://huggingface.co/litert-community) — 200+ ready-to-run models maintained with the LiteRT team: LLMs and VLMs as `.litertlm`, classic vision/audio as `.tflite`, many with per-SoC NPU-compiled variants. Recent arrivals include Mamba2 and gated-delta hybrid architectures (granite-4.0-h, Qwen3.5).
- [john-rocky/LiteRT-Models](https://github.com/john-rocky/LiteRT-Models) — Community conversions (TTS, ASR, vision, video) with GPU-acceleration notes and verification records against the source models.
- [KegangWangCCNU/FacePhys-Release](https://github.com/KegangWangCCNU/FacePhys-Release) — rPPG (camera heart-rate) state-space model built on LiteRT.
- [ShadowSafin/AndroLLM](https://github.com/ShadowSafin/AndroLLM) — Open-source Android AI using LiteRT-LM with hardware acceleration, cloud providers, memory, and voice.

## Conversion & quantization

- [litert-torch `export_hf`](https://github.com/google-ai-edge/litert-torch) — One command from a Hugging Face repo to a `.litertlm` bundle, quantization recipe included (see [Official](#official)).
- [LiteRT-CLI](https://github.com/google-ai-edge/LiteRT-CLI) — `litert convert` / `litert quantize` for classic models from a small Python wrapper class.
- [ai-edge-quantizer](https://github.com/google-ai-edge/ai-edge-quantizer) — Standalone quantization when you need recipe control (see [Official](#official)).

## Serving

- [NightMean/OlliteRT](https://github.com/NightMean/OlliteRT) — Turn an Android phone into a fully local OpenAI-compatible LLM inference server.
- [Cyclenerd/android-llm-server](https://github.com/Cyclenerd/android-llm-server) — Local LLM server for Android (Gemma 4, LiteRT, OpenAI API).
- [imertz/litert-lm-api-server](https://github.com/imertz/litert-lm-api-server) — Lightweight Node.js server exposing an OpenAI-compatible API over LiteRT-LM.
- [angolo40/vicino-llm](https://github.com/angolo40/vicino-llm) — VicinoLLM - your LLM, close to you. A local OpenAI-compatible LLM server on Android, powered by Gemma 4 via LiteRT-LM.

## Benchmarks & engineering notes

- [john-rocky/apple-silicon-llm-bench](https://github.com/john-rocky/apple-silicon-llm-bench) — Reproducible cross-runtime LLM benchmark (LiteRT-LM · Core AI · MLX · llama.cpp) on Mac and iPhone: one instrument, warm-run protocol, thermal gating, energy per token.

## Learning

- [LiteRT documentation](https://ai.google.dev/edge/litert) — Start with the platform quickstarts and the NPU guide.
- [litert-samples](https://github.com/google-ai-edge/litert-samples) — The samples double as tutorials: each model recipe shows the full convert → verify → run path.
- [onuralpszr/litert-lm-cookbook](https://github.com/onuralpszr/litert-lm-cookbook) — Runnable scripts and Colab notebooks for LiteRT-LM with Gemma 4, from single-turn chat up to a local OpenAI-compatible server.
- [seehiong/local-ai-starter](https://github.com/seehiong/local-ai-starter) — Zero-backend client-side AI assistant starter template on WebGPU + LiteRT-LM.
- [SNU-RTOS/minimal-litert](https://github.com/SNU-RTOS/minimal-litert) — Minimal Bazel-built LiteRT example with XNNPACK/GPU profiling.
- [Data-Sapien/awesome-on-device-mobile-llms](https://github.com/Data-Sapien/awesome-on-device-mobile-llms) — Adjacent curation: shipping on-device LLMs on mobile (runtime comparisons, model picks, architecture).

## Contributing

PRs welcome. Criteria for inclusion:

- Public repo (or published resource) that is specifically about LiteRT, LiteRT-LM, `.litertlm` / LiteRT-era `.tflite` deployment.
- Has a README that lets a stranger use it: what it is, how to run it, what platform/hardware it needs.
- Model entries should state the license and how correctness was verified (e.g. parity vs the upstream reference).

One line per entry, factual tone, no superlatives. Within each section: official Google
resources first, then entries ordered by how useful and proven they are for that section's
purpose — never by authorship. New radar finds join at the bottom until they earn a higher spot.

New entries are also scouted and added weekly by an automated [radar](.github/workflows/radar.yml)
(GitHub / Hugging Face search): confident finds — a strong LiteRT signal plus real traction —
land in the list automatically, and everything else waits in [RADAR.md](RADAR.md) until it
qualifies. Spotted a bad entry? Open an issue or PR; removals are pinned in
[`.github/radar-ignore.txt`](.github/radar-ignore.txt) so the radar never re-adds them.
