# Voice Cloning System for Law School Studies

A self-contained system for converting text to audio using your own voice with Qwen3-TTS and Apple MLX.

## 📁 Structure

```
VOICE_CLONING_SYSTEM/
├── scripts/                  # Conversion scripts
│   ├── voice_clone_tts.py   # Main voice cloning script
│   └── test_voice_clone.sh  # Quick test script
├── voice_samples/            # Your voice recordings
│   └── voice_sample.wav     # Your 4-second voice sample
├── test_outputs/             # Test audio outputs
├── docs/                     # Documentation
│   └── VOICE_REQUIREMENTS.md # Voice sample requirements
└── README.md                 # This file
```

## 🎯 Purpose

Convert law school prep materials (markdown files) to audio using your own voice instead of generic AI voices. This helps with:
- Reviewing material while driving/walking
- Multi-sensory learning
- Time-efficient studying

## 🚀 Quick Start

### 1. Activate Environment

```bash
cd "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"
source qwen3-tts-env/bin/activate
```

### 2. Run Quick Test

```bash
cd VOICE_CLONING_SYSTEM
./scripts/test_voice_clone.sh
```

### 3. Convert Your Own Text

```bash
python scripts/voice_clone_tts.py \
  "Your text here" \
  voice_samples/voice_sample.wav \
  "Hey, this is my voice. I'm going to talk for about four seconds." \
  -o test_outputs/my_audio.mp3
```

## 📝 Usage

### Basic Command Structure

```bash
python scripts/voice_clone_tts.py <TEXT> <VOICE_SAMPLE> <TRANSCRIPT> [options]
```

**Arguments:**
- `TEXT`: The text you want to convert
- `VOICE_SAMPLE`: Path to your voice WAV file
- `TRANSCRIPT`: Exact transcript of what you said in the voice sample

**Options:**
- `-o, --output`: Output file path (default: output.wav)
- `-l, --language`: Language (default: English)

### Examples

**1. Simple test:**
```bash
python scripts/voice_clone_tts.py \
  "Hello world, this is a test." \
  voice_samples/voice_sample.wav \
  "Hey, this is my voice. I'm going to talk for about four seconds."
```

**2. Save as MP3:**
```bash
python scripts/voice_clone_tts.py \
  "This is a longer text for testing." \
  voice_samples/voice_sample.wav \
  "Hey, this is my voice. I'm going to talk for about four seconds." \
  -o test_outputs/test.mp3
```

**3. Convert from text file:**
```bash
python scripts/voice_clone_tts.py \
  "$(cat my_notes.txt)" \
  voice_samples/voice_sample.wav \
  "Hey, this is my voice. I'm going to talk for about four seconds." \
  -o test_outputs/notes_audio.mp3
```

## ✅ Requirements

### System Requirements
- Mac with Apple Silicon (M1/M2/M3)
- Python 3.10+
- Virtual environment: `qwen3-tts-env`

### Python Packages (already installed in env)
- mlx-audio
- soundfile
- numpy

### External Tools
- ffmpeg (for MP3 conversion): `brew install ffmpeg`
- sox (for audio processing): `brew install sox`

## 🎤 Voice Sample Requirements

Your voice sample should be:
- **Duration**: 4-10 seconds (4 seconds works great!)
- **Format**: WAV file
- **Sample rate**: 16000 Hz (minimum)
- **Channels**: Mono (1 channel)
- **Quality**: Clean, no background noise
- **Content**: Natural speech, conversational tone

### Creating a Voice Sample

```bash
# Record using Sox
sox -d -r 16000 -c 1 voice_sample.wav

# Or use the recording script
./record_voice.sh
```

**What to say:**
Speak naturally for 4 seconds. Example:
> "Hey, this is my voice. I'm going to talk for about four seconds."

**Remember:** You need the exact transcript of what you said!

## 🔧 Technical Details

### Model
- **Name**: Qwen3-TTS-12Hz-0.6B-Base-bf16
- **Framework**: MLX (Apple Silicon optimized)
- **Repository**: mlx-community/Qwen3-TTS-12Hz-0.6B-Base-bf16
- **Method**: Voice cloning using reference audio

### How It Works
1. Loads your voice sample (WAV file)
2. Extracts voice characteristics
3. Generates new speech in your voice
4. Saves as WAV or converts to MP3

## 📊 Performance

On Apple Silicon:
- Model load time: ~2-3 seconds
- Generation speed: ~1-2x realtime
- Memory usage: ~2-3 GB

## 🐛 Troubleshooting

### "Module not found" errors
```bash
# Make sure environment is activated
source qwen3-tts-env/bin/activate
```

### "Reference audio not found"
```bash
# Check that voice sample exists
ls -lh voice_samples/voice_sample.wav
```

### Poor voice quality
- Use a higher quality voice sample (16kHz+)
- Ensure voice sample is 4-10 seconds
- Remove background noise from recording
- Match transcript exactly to recording

### MP3 conversion fails
```bash
# Install ffmpeg
brew install ffmpeg
```

## 📖 Next Steps

Once you verify the system works:

1. **Test with short text** - Verify voice quality
2. **Test with longer text** - Check consistency
3. **Integration** - Connect to law school prep workflow
4. **Batch processing** - Convert multiple files

## 🔗 Integration with Law School Workflow

This system will integrate with:
- `ACTIVE/*/02_PREP/` folders
- Audio prep markdown files
- Batch conversion scripts

*Integration pending after verification phase.*

## 📞 Support

For issues or questions, check:
1. This README
2. `docs/VOICE_REQUIREMENTS.md`
3. Test outputs in `test_outputs/`

---

**Status**: ✅ Ready for testing  
**Last Updated**: January 26, 2026
