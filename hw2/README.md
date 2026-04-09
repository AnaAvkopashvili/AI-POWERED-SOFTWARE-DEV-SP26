# HW2: Individual Audio Pipeline

A round-trip TTS → STT pipeline that synthesizes speech from text using OpenAI TTS, transcribes it back using Whisper, compares the result, and logs cost and latency for every API call.

## Install dependencies

```bash
pip install -r requirements.txt
```

## Set up your API key

```bash
cp .env.example .env
# Edit .env and replace the placeholder with your real OpenRouter key
```

## Run the pipeline

```bash
# Full pipeline with default text
python hw2-audio-pipeline.py

# Full pipeline with custom text
python hw2-audio-pipeline.py "Your text to synthesize here"

# Transcribe an existing audio file only
python hw2-audio-pipeline.py --transcribe path/to/audio.mp3
```

## Expected output

```
============================================================
HW2 AUDIO PIPELINE
============================================================

[1/4] Generating speech — voice: nova
  Text (290 chars): "Machine learning models learn patterns from data..."
  Generated in 2.14s
  File: audio-output/voice_nova_sample.mp3 (47.3 KB)
  Cost: $0.00435

[2/4] Generating speech — voice: alloy
  Text (290 chars): "Machine learning models learn patterns from data..."
  Generated in 1.98s
  File: audio-output/voice_alloy_sample.mp3 (45.8 KB)
  Cost: $0.00435

[3/4] Transcribing: audio-output/voice_nova_sample.mp3
  Transcript: "Machine learning models learn patterns from data..."
  Language detected: english
  Audio duration: 14.2s
  Transcribed in 1.52s
  Cost: $0.00142

[4/4] Comparing original vs transcribed text
  Word overlap accuracy: 97.4%
  Original words:    46
  Transcribed words: 46

============================================================
COST AND LATENCY SUMMARY
============================================================
  TTS calls:     2  |  Total cost: $0.00870  |  Avg latency: 2.06s
  STT calls:     1  |  Total cost: $0.00142  |  Avg latency: 1.52s
  Pipeline total cost: $0.01012
```

## Repository structure

```
hw2/
├── hw2-audio-pipeline.py
├── reflection.md
├── requirements.txt
├── .env.example
├── README.md
└── audio-output/
    ├── voice_nova_sample.mp3
    └── voice_alloy_sample.mp3
```
