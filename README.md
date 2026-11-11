# Awesome LiteRT

A list of tools, models, sample apps and guides for [LiteRT](https://github.com/google-ai-edge/LiteRT), Google's on-device ML runtime and the successor to TensorFlow Lite, and for [LiteRT-LM](https://github.com/google-ai-edge/LiteRT-LM), its engine for language models.

LiteRT runs models on CPU, GPU and NPU across Android, iOS, macOS, Linux, the browser and embedded boards. Classic models ship as `.tflite` files, and language models as `.litertlm` bundles.

I ([john-rocky](https://github.com/john-rocky)) maintain this list. Entries under that account are my own projects, and so are the recipes, `edge-lint`, the version table and the OlliteRT model source. A weekly script adds new projects that clearly mention LiteRT and have at least 10 stars, so I haven't read every community entry. The list starts with the LiteRT era, September 2024, and leaves out older TensorFlow Lite projects. Pull requests are welcome under the rules in [Contributing](#contributing).

---

## Contents

- [Official](#official)
- [Getting started](#getting-started)
- [Recipes](#recipes)
- [Running models in your app](#running-models-in-your-app)
- [Apps](#apps)
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

- [AI Edge Gallery](https://github.com/google-ai-edge/gallery) — Install the app, pick a model and run it on your phone.
- [LiteRT-LM CLI](https://ai.google.dev/edge/litert-lm/cli/usage) — Install it with `pip install litert-lm`. The page has a complete command that runs a model from [litert-community](https://huggingface.co/litert-community) on any machine with Python.
- [LiteRT quickstarts](https://ai.google.dev/edge/litert) — Android (Kotlin), iOS, Python.

## Recipes

Step-by-step guides for adding one model to an app you already have. Each one tells you what to add and ends with a command that checks it works. [on-device-recipes](https://github.com/john-rocky/on-device-recipes) has the index.

- [Background removal (ormbg) in an existing Android app, on the GPU](https://github.com/john-rocky/LiteRT-Models/blob/main/ormbg/INTEGRATION.md) — LiteRT CompiledModel 2.2.0. On a Pixel 8a, the model takes 246 ms per frame and the whole pipeline 361 ms, with every op on the GPU.
- [Offline chat with Qwen2.5-1.5B-Instruct in an existing Android app](https://github.com/john-rocky/on-device-recipes/blob/main/android-llm-chat/INTEGRATION.md) — LiteRT-LM 0.16.1 (`litertlm-android`), two Gradle entries and two Kotlin files. On a Pixel 8a, it generates 10.48 tokens per second on the CPU and 13.8 on the GPU.
- [A fine-tuned Hugging Face model in an existing iPhone app](https://github.com/john-rocky/swift-litert-lm/blob/main/docs/recipe-hf-finetune-to-iphone.md) — hf-to-litertlm converts the model and swift-litert-lm 0.2.0 runs it. The Swift code is the same on iPhone and Mac, and so far I've only run it on a Mac.

## Running models in your app

- [LiteRT CompiledModel API](https://github.com/google-ai-edge/LiteRT) — The current-generation API for classic models (see [Official](#official)).
- [john-rocky/swift-litert-lm](https://github.com/john-rocky/swift-litert-lm) — SwiftPM package for LiteRT-LM on iPhone/Mac, including an Apple FoundationModels-compatible adapter (guided generation, tool calling) shipped with LiteRT-LM v0.15.0.
- [andrisgauracs/LiteRT.js-Mocap](https://github.com/andrisgauracs/LiteRT.js-Mocap) — Real-time human pose estimation entirely in the browser with LiteRT.js.
- [soniqo/speech-core](https://github.com/soniqo/speech-core) — On-device VAD / streaming STT / TTS / diarization voice-agent pipeline in C++17 (ONNX + LiteRT); Linux, Windows, Android.
- [ShadAdman/EdgeRt](https://github.com/ShadAdman/EdgeRt) — Run models across tflite / LiteRT / ExecuTorch runtimes on edge devices from one harness.
- [NSTiwari/YOLOv10-LiteRT-Android](https://github.com/NSTiwari/YOLOv10-LiteRT-Android) — YOLOv10 converted to `.tflite` and deployed on Android.
- [stevan-milovanovic/LiteRT-for-Android](https://github.com/stevan-milovanovic/LiteRT-for-Android) — Image classification, image captioning and LLM inference on Android.
- [alphasoftwarepy/as-core](https://github.com/alphasoftwarepy/as-core) — Local AI runtime for edge hardware built on LiteRT-LM and Gemma.
- [Desert-Ant-Labs/desert-ant-core](https://github.com/Desert-Ant-Labs/desert-ant-core) — On-device AI SDKs for iOS, macOS, Android and the web: small models that run offline in Swift, Kotlin and JavaScript with Core ML, LiteRT and WebAssembly.
- [TakashiYoshinaga/LocalVisionAI-for-Unity](https://github.com/TakashiYoshinaga/LocalVisionAI-for-Unity) — Offline Unity sample for Android that describes camera photos and answers typed questions with Gemma via LiteRT-LM. The model is bundled in the APK.
- [FilipFan/PolyEngineInfer](https://github.com/FilipFan/PolyEngineInfer) — Run LLM inference in an Android app with llama.cpp, ExecuTorch, LiteRT, ONNX, and more.
- [olibartfast/rf-detr-cpp-inference](https://github.com/olibartfast/rf-detr-cpp-inference) — RF-DETR C++ inference engine for object detection and instance segmentation with ONNX Runtime, TensorRT, Executorch and LiteRT support.

## Apps

Finished apps built on LiteRT or LiteRT-LM.

- [dineshsoudagar/local-llms-on-android](https://github.com/dineshsoudagar/local-llms-on-android) — Offline chat app running Gemma, Qwen and LLaMA on Android with LiteRT.
- [Mohd-Mursaleen/LiteRT-Server](https://github.com/Mohd-Mursaleen/LiteRT-Server) — Native Kotlin app running the Gemma 4 E2B multimodal LLM on-device via LiteRT-LM.
- [iFleey/PPOCRv5-Android](https://github.com/iFleey/PPOCRv5-Android) — Real-time OCR app with PP-OCRv5 on LiteRT.
- [alexeyw/knotwork](https://github.com/alexeyw/knotwork) — Android agent on LiteRT-LM with pipelines you assemble, MCP tool calling, and a confirmation step before risky actions.
- [nikunjsingh93/Mochu-Local-AI-Assistant](https://github.com/nikunjsingh93/Mochu-Local-AI-Assistant) — Android assistant for chat, documents and photos, image generation, web search and voice, all with on-device models.
- [Onion99/Agro](https://github.com/Onion99/Agro) — Cross-platform on-device LLM and agent client on LiteRT-LM and Compose Multiplatform.
- [itsyuimorii/obsidian-gemma4-litert-wiki](https://github.com/itsyuimorii/obsidian-gemma4-litert-wiki) — Runs Gemma 4 E4B inside Obsidian with LiteRT-LM and WebGPU, and builds a wiki over your vault: cards, an index, concept pages and tags, then chat, quizzes and flashcards.
- [battlesbudz/Faraday](https://github.com/battlesbudz/Faraday) — On-device voice agent for Android: Gemma 4 on the phone, with voice conversation, long-term memory and tools.
- [ShadowSafin/AndroLLM](https://github.com/ShadowSafin/AndroLLM) — Open-source Android AI using LiteRT-LM with hardware acceleration, cloud providers, memory, and voice.
- [PrinceBad/Local-LLM-AI](https://github.com/PrinceBad/Local-LLM-AI) — Offline Android app for running LLMs, built on LiteRT and Jetpack Compose.
- [umarpazir11/pocketsage](https://github.com/umarpazir11/pocketsage) — Offline RAG app for Android that answers questions about a PDF.
- [andrisgauracs/eye-photo-sorter](https://github.com/andrisgauracs/eye-photo-sorter) — Sorts a folder of photos into receipts, screenshots, documents, pets, blurry, eyes closed and duplicates, in the browser, with Desert Ant Labs' Eye on LiteRT.js and WebGPU.
- [p-nickzhang-q/photo-ledger](https://github.com/p-nickzhang-q/photo-ledger) — Android expense tracker that turns payment screenshots into ledger entries, offline: on-device OCR plus a 0.6B LLM with constrained decoding.
- [zhzy0077/KataDroid](https://github.com/zhzy0077/KataDroid) — Offline KataGo analysis and SGF editing for Android, with LiteRT CPU and optional NPU inference.
- [Sherin-SEF-AI/Lyne-ADAS](https://github.com/Sherin-SEF-AI/Lyne-ADAS) — On-device driver assistance for Android: forward-collision, drivable-area, pedestrian, lane and traffic-sign warnings that adapt to the phone's performance.
- [SyltechAI/RustSensei](https://github.com/SyltechAI/RustSensei) — Offline Android app that teaches Rust, with a tutor that runs on LiteRT.
- [b0urbonn/appdev_boilerplate](https://github.com/b0urbonn/appdev_boilerplate) — Android chat app in Expo SDK 57, with on-device Gemma 4 via LiteRT-LM, Gemini in the cloud, and image and voice input.

## Bindings & wrappers

[This table](https://github.com/john-rocky/litertlm-release-gate/blob/main/wrappers/TABLE.md) shows which LiteRT-LM version each wrapper and app uses, with a link to where it is set.

Community bindings and SDKs for LiteRT and LiteRT-LM:

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
- [ARM-software/compute-flow](https://github.com/ARM-software/compute-flow) — SDK for building on-device AI applications on Arm with reusable building blocks across inference runtimes.
- [leehack/llamadart](https://github.com/leehack/llamadart) — Cross-platform on-device LLM inference for Dart & Flutter: GGUF via llama.cpp and LiteRT-LM on Android, iOS, macOS, Windows, Linux and web.

## Models

- [Hugging Face: litert-community](https://huggingface.co/litert-community) — 200+ ready-to-run models: LLMs and VLMs as `.litertlm`, classic vision/audio as `.tflite`, many with per-SoC NPU-compiled variants.
- [john-rocky/LiteRT-Models](https://github.com/john-rocky/LiteRT-Models) — Community conversions (TTS, ASR, vision, video) with GPU-acceleration notes and verification records against the source models.
- [KegangWangCCNU/FacePhys-Release](https://github.com/KegangWangCCNU/FacePhys-Release) — rPPG (camera heart-rate) state-space model built on LiteRT.

## Conversion & quantization

- [litert-torch `export_hf`](https://github.com/google-ai-edge/litert-torch) — One command from a Hugging Face repo to a `.litertlm` bundle, quantization recipe included (see [Official](#official)).
- [LiteRT-CLI](https://github.com/google-ai-edge/LiteRT-CLI) — `litert convert` / `litert quantize` for classic models from a small Python wrapper class.
- [ai-edge-quantizer](https://github.com/google-ai-edge/ai-edge-quantizer) — Standalone quantization when you need recipe control (see [Official](#official)).
- [edge-lint](https://github.com/john-rocky/edge-compat#edge-lint--static-delegate-pre-flight) — Predicts which ops of a `.tflite` will fall back from the GPU, with no device or runtime. It returns exit codes and JSON for CI.

## Serving

- [NightMean/OlliteRT](https://github.com/NightMean/OlliteRT) — Turn an Android phone into a fully local OpenAI-compatible LLM inference server.
- [OlliteRT model source](ollitert/) — One URL that adds 45 LiteRT-LM chat models to OlliteRT's model list. I tested each file on LiteRT-LM 0.16.1, the runtime in OlliteRT 0.9.7, and six of them in the app on a Pixel 11 Pro.
- [Cyclenerd/android-llm-server](https://github.com/Cyclenerd/android-llm-server) — Local LLM server for Android (Gemma 4, LiteRT, OpenAI API).
- [imertz/litert-lm-api-server](https://github.com/imertz/litert-lm-api-server) — Lightweight Node.js server exposing an OpenAI-compatible API over LiteRT-LM.
- [angolo40/vicino-llm](https://github.com/angolo40/vicino-llm) — A local OpenAI-compatible LLM server on Android, on Gemma 4 via LiteRT-LM.
- [CubicLM/CubicLM](https://github.com/CubicLM/CubicLM) — Cross-platform AI workspace with local GPU acceleration (GGUF, LiteRT-LM), on-device image generation, 23+ cloud APIs, local memory and an embedded OpenAI-compatible server.

## Benchmarks & engineering notes

- [john-rocky/apple-silicon-llm-bench](https://github.com/john-rocky/apple-silicon-llm-bench) — The same benchmark across LiteRT-LM, Core AI, MLX and llama.cpp on Mac and iPhone, with speed and energy per token, and the scripts to reproduce it.
- [john-rocky/edge-compat](https://github.com/john-rocky/edge-compat) — Measured delegate compatibility for LiteRT: an op-level matrix per backend × runtime version (18 snapshots, 659 entries), a static GPU-fallback linter (`edge-lint`), 200+ model cards with browser and device measurements, and a [browser table + demo zoo](https://john-rocky.github.io/edge-compat/) with an `llms.txt` for agents, including the models that fail.

## Learning

- [LiteRT documentation](https://ai.google.dev/edge/litert) — Start with the platform quickstarts and the NPU guide.
- [litert-samples](https://github.com/google-ai-edge/litert-samples) — Each model recipe in the samples goes from conversion to running the model.
- [onuralpszr/litert-lm-cookbook](https://github.com/onuralpszr/litert-lm-cookbook) — Runnable scripts and Colab notebooks for LiteRT-LM with Gemma 4, from single-turn chat up to a local OpenAI-compatible server.
- [seehiong/local-ai-starter](https://github.com/seehiong/local-ai-starter) — Zero-backend client-side AI assistant starter template on WebGPU + LiteRT-LM.
- [SNU-RTOS/minimal-litert](https://github.com/SNU-RTOS/minimal-litert) — Minimal Bazel-built LiteRT example with XNNPACK/GPU profiling.
- [Data-Sapien/awesome-on-device-mobile-llms](https://github.com/Data-Sapien/awesome-on-device-mobile-llms) — A list about shipping on-device LLMs on mobile: runtime comparisons, model picks and architecture.
- [xprilion/gemma3-270m-finetune-litert](https://github.com/xprilion/gemma3-270m-finetune-litert) — Tutorial and Colab notebook for fine-tuning Gemma 3 270M and running it in the browser with LiteRT.js and WebGPU.

## Contributing

PRs welcome. Criteria for inclusion:

- Public repo (or published resource) that is specifically about LiteRT, LiteRT-LM, `.litertlm` / LiteRT-era `.tflite` deployment.
- Has a README that lets a stranger use it: what it is, how to run it, what platform/hardware it needs.
- Model entries should state the license and how correctness was verified (e.g. parity vs the upstream reference).

Keep each entry short and factual, with no superlatives. Each section lists official Google resources first, then the entries I've chosen. The script adds new ones at the bottom.

A [weekly script](.github/workflows/radar.yml) searches GitHub and Hugging Face for new projects. It adds the ones that clearly mention LiteRT and have at least 10 stars, and lists the rest in [RADAR.md](RADAR.md). If an entry is wrong, open an issue or a pull request. A removed project goes in [`.github/radar-ignore.txt`](.github/radar-ignore.txt), so the script doesn't add it back.
