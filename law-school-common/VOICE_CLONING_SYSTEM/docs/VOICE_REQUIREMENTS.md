# Voice Sample Requirements for Voice Cloning

## Overview

Creating a high-quality voice sample is crucial for good voice cloning results. This document explains what makes a good voice sample and how to create one.

## Technical Requirements

### Essential Specifications
- **Format**: WAV (uncompressed audio)
- **Sample Rate**: 16000 Hz minimum (higher is better)
- **Bit Depth**: 16-bit or higher
- **Channels**: Mono (1 channel)
- **Duration**: 4-10 seconds (4 seconds is optimal)

### Quality Requirements
- **Background Noise**: Minimal to none
- **Clarity**: Clear, unobstructed speech
- **Volume**: Consistent, not too loud or soft
- **Recording**: Single continuous recording (no edits/cuts)

## Content Guidelines

### What to Say
Speak naturally and conversationally. Your voice sample should sound like you're having a normal conversation, not reading or performing.

**Good Examples:**
- "Hey, this is my voice. I'm going to talk for about four seconds."
- "Hi, I'm recording a voice sample for text-to-speech. This should be about four seconds long."
- "This is a sample of my natural speaking voice for voice cloning purposes."

### What to Avoid
- ❌ Reading in a monotone
- ❌ Shouting or whispering
- ❌ Overly dramatic delivery
- ❌ Very fast or very slow speech
- ❌ Multiple sentences with different emotions

### Important Notes
1. **Exact Transcript Required**: You MUST remember exactly what you said. The transcript must match the audio perfectly.
2. **Natural Delivery**: Speak as you normally would in conversation.
3. **Consistent Pace**: Don't speed up or slow down during recording.
4. **One Take**: Record in a single take without pauses or edits.

## Recording Methods

### Method 1: Using Sox (Recommended)

```bash
# Record 4 seconds at 16kHz, mono
sox -d -r 16000 -c 1 voice_sample.wav

# Press Ctrl+C after 4 seconds
```

### Method 2: Using record_voice.sh Script

```bash
# From law-school root directory
./record_voice.sh
```

This script will:
- Record your voice
- Automatically save as proper format
- Show recording duration

### Method 3: Using macOS QuickTime

1. Open QuickTime Player
2. File → New Audio Recording
3. Click record button
4. Speak for 4 seconds
5. Stop recording
6. Save as: `voice_sample_temp.m4a`
7. Convert to WAV:
   ```bash
   sox voice_sample_temp.m4a -r 16000 -c 1 voice_sample.wav
   ```

### Method 4: Using iPhone/Other Device

1. Record voice memo (4 seconds)
2. Export/AirDrop to Mac
3. Convert using sox:
   ```bash
   sox input_file.m4a -r 16000 -c 1 voice_sample.wav
   ```

## Recording Environment

### Ideal Environment
✅ Quiet room with minimal echo  
✅ Close to microphone (6-12 inches)  
✅ Door closed to outside noise  
✅ No fans, AC, or ambient sounds  
✅ Consistent room tone  

### Avoid
❌ Noisy environments  
❌ Echo-heavy rooms  
❌ Too far from microphone  
❌ Windy outdoor locations  
❌ Places with background conversations  

## Validation

After recording, verify your sample:

```bash
# Check file format and quality
sox voice_sample.wav -n stat

# Listen to it
afplay voice_sample.wav

# Check duration (should be 4-10 seconds)
soxi -D voice_sample.wav
```

### Good Sample Characteristics
✅ Clear speech, easy to understand  
✅ No distortion or clipping  
✅ Minimal background noise  
✅ Consistent volume throughout  
✅ Natural conversational tone  

### Signs of Problems
❌ Hissing or static noise  
❌ Words are cut off or unclear  
❌ Volume fluctuates wildly  
❌ Sounds robotic or artificial  
❌ Background sounds audible  

## Transcript Guidelines

The transcript is critical for voice cloning to work properly.

### Rules
1. **Exact Match**: Write exactly what you said, word-for-word
2. **Capitalization**: Use proper capitalization
3. **Punctuation**: Include periods, commas, etc. where natural
4. **No Edits**: Don't "fix" what you said - transcribe accurately

### Example

**Audio**: "Hey, this is my voice, um, I'm going to talk for about four seconds."

**Correct Transcript**: 
```
Hey, this is my voice, um, I'm going to talk for about four seconds.
```

**Wrong Transcript** (don't do this):
```
This is my voice. I'm going to talk for about four seconds.
```
(Missing "Hey" and "um" - won't work!)

## Troubleshooting

### Voice Clone Sounds Wrong

**Possible Causes:**
1. Transcript doesn't match audio exactly
2. Voice sample has too much background noise
3. Sample is too short (< 3 seconds)
4. Recording quality is poor

**Solutions:**
1. Re-record voice sample in quiet environment
2. Double-check transcript matches exactly
3. Aim for 4-6 seconds of speech
4. Use a better microphone if available

### Can't Hear Background Noise in Recording

**Test:**
```bash
# Amplify audio to hear subtle noise
sox voice_sample.wav test_loud.wav vol 3.0
afplay test_loud.wav
```

If you hear hissing, fan noise, or other sounds when amplified, re-record in a quieter space.

## Best Practices Summary

1. **Environment**: Find the quietest room available
2. **Duration**: Aim for 4-6 seconds
3. **Content**: Speak naturally and conversationally
4. **Recording**: Use sox or a good quality microphone
5. **Format**: Save as 16kHz mono WAV
6. **Transcript**: Write down exactly what you said
7. **Verification**: Listen back before using

## Sample Transcript Templates

Use these as guides for what to say:

**Template 1 (Recommended):**
```
Hey, this is my voice. I'm going to talk for about four seconds.
```

**Template 2:**
```
Hi, I'm recording a voice sample. This is how I naturally speak.
```

**Template 3:**
```
This is a sample of my voice for text-to-speech conversion.
```

**Template 4:**
```
Hello, this is me speaking naturally for about four to five seconds.
```

Choose one, speak it naturally, and remember it exactly!

---

**Last Updated**: January 26, 2026  
**Version**: 1.0
