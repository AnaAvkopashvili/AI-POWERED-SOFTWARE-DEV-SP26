# HW2 Data Governance Reflection

**Student Name:** Ana Avkopashvili 
**Course:** CS-AI-2025 — Building AI-Powered Applications | Spring 2026  
**Assignment:** Homework 2 — Individual Audio Pipeline  
**Date:** April 2026

---

## 1. Consent: What Mechanisms Would Be Needed for Real User Audio?

My pipeline currently processes only synthetic audio — text I wrote, converted to speech by the TTS model, then fed directly into Whisper. No real human voice is ever recorded. If this changed, the consent requirements would shift substantially.

For a product that records real user speech, consent would need to happen before the microphone activates. The consent screen would need to say something like: *"This feature records your voice and sends the audio to OpenAI's Whisper API for transcription. Your audio is not stored after transcription is complete. OpenAI's API data usage policy states that inputs are not used for model training. You can disable voice input at any time in Settings."* That language covers: what is collected, where it goes, how long it is kept, and how the user can stop.

The timing matters. A permission prompt appearing mid-session — after the user has already spoken — is a compliance failure, not just a UX failure. Consent must precede any recording. In a mobile context this would typically be a one-time system-level microphone permission followed by an in-app consent screen on first use of the audio feature specifically.

Revocation is the harder part. A user withdrawing consent after the fact would mean: disabling future recordings (easy), and deleting any stored audio or transcripts tied to their account (requires a proper data deletion pipeline, which my HW2 script does not have — it simply leaves the MP3 in `audio-output/`). In a production system, the generated MP3 files should be deleted immediately after STT completes unless there is an explicit reason to retain them.

---

## 2. Retention: How Long Should Audio Files Be Kept?

The right retention period depends entirely on why the audio was collected. Three scenarios illustrate how different the answer can be.

**Study app generating audio lessons (like the capstone reference in `03_capstone_audio_example.py`):** The audio is synthetic — generated from text by TTS — so it contains no user voice data. Retention can be generous: caching a generated lesson for 30 days is reasonable and reduces API costs. After 30 days, or when the underlying text changes, the cached file should be deleted. Transcripts of user speech (if the student reads back a passage) should be deleted as soon as the accuracy score is computed.

**Customer service transcription tool:** The transcript has legal and operational value — companies reference call logs for dispute resolution and quality assurance. Typical retention in this context is 90 days for operational review, up to 7 years if the call relates to a financial transaction (depending on jurisdiction). The raw audio should be deleted as soon as the transcript is validated; storing both indefinitely doubles the risk with no added value.

**Medical intake form:** This is the most sensitive scenario. Audio recordings of symptoms and medical history are protected health information under HIPAA in the US and equivalent frameworks in Georgia. Minimum retention is typically 6-10 years (depending on whether the patient is an adult or a minor at time of recording). But "must retain" does not mean "retain audio" — the transcript fulfills the legal obligation in most cases, and the raw audio adds biometric and emotional-state risk without legal necessity. Delete raw audio immediately after transcription; retain the structured transcript in an encrypted database.

---

## 3. PII Risks in Audio Data That Do Not Exist in Text

When someone types a message, the data is exactly what they typed. When someone speaks, the recording contains layers of information they did not consciously provide.

**Voice biometrics.** A voiceprint is a biometric identifier — unique to a person like a fingerprint. My pipeline sends audio to OpenAI's Whisper API. Even if OpenAI's policy states they do not retain inputs beyond the request, the audio is transmitted and briefly processed. That transmission window represents an exposure that simply does not exist in text.

**Accent and language markers.** Whisper's `verbose_json` response returns a `language` field. In my test runs this correctly identified English. But accent and dialect patterns in audio can reveal regional origin, ethnicity, or socioeconomic background — information the user never typed and likely did not intend to disclose.

**Background audio.** A phone recording captures the environment. A student recording a voice memo for Exercise 2 might inadvertently capture a roommate's conversation, a TV broadcast, or street noise that identifies their location. Text has no equivalent ambient capture.

**Emotional state.** Pace, pitch, and tremor in voice can be analyzed to infer stress, anxiety, or mood. My pipeline does not perform any emotional analysis, but the raw audio contains that signal. A more sophisticated downstream model could extract it. The user who typed a calm message and the user who spoke with a trembling voice said the same words — but only one of them disclosed their emotional state.

**Recording metadata.** Audio files created by smartphones often embed metadata: recording timestamp, device model, and sometimes GPS coordinates. My STT function reads the file without stripping metadata. A production pipeline should use a library like `mutagen` or `ffmpeg` to remove embedded metadata before transmission.

---

## 4. Data Governance for My Capstone Project

My team assessed audio in Exercise 3 and selected **deferred audio** — audio would add value but is not worth the complexity for the initial version. However, thinking through what would change if we added it later is exactly the kind of forward planning that prevents governance problems from being retrofitted badly.

If we did add voice input to our capstone, the most significant governance challenge would be consent granularity. Our product has multiple user roles. A consent flow that works for one role (a student recording a note to themselves) may not cover another role (an instructor whose voice is captured during a class session). We would need role-specific consent language and a clear policy on whether audio from multi-participant sessions can be processed at all without consent from every participant — which in Georgia's legal context, and under GDPR's requirements for EU users, would require explicit opt-in from all parties.

The cost tracking I built into `hw2-audio-pipeline.py` — specifically the `record_call()` function that logs every API call with timestamp, model, input size, and estimated cost — is directly applicable to a production capstone feature. That log doubles as an audit trail: if a user requests deletion of their data, the log tells us exactly which API calls involved their audio, what was transmitted, and when.

The one thing my current implementation does not handle that a production capstone would need is automatic deletion of the `audio-output/` MP3 files after the pipeline completes. Adding `output_path.unlink()` after STT finishes would be the minimum responsible change.


