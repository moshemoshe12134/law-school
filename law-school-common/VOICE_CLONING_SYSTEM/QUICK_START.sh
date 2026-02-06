#!/bin/bash
# Quick Start - Voice Cloning System
# Run this to get started!

cat << 'EOF'
╔═══════════════════════════════════════════════════════════╗
║                                                           ║
║        🎙️  VOICE CLONING SYSTEM - QUICK START 🎙️         ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝

📍 You are here: VOICE_CLONING_SYSTEM/

📚 What's available:
   ├── scripts/
   │   ├── voice_clone_tts.py       ← Main conversion script
   │   └── test_voice_clone.sh      ← Quick test
   ├── voice_samples/
   │   └── voice_sample.wav         ← Your voice (4 seconds)
   ├── test_outputs/                 ← Generated audio goes here
   └── docs/
       ├── README.md                 ← Full documentation
       ├── VOICE_REQUIREMENTS.md     ← How to record voice
       └── CLEANUP_NOTES.md          ← What we removed

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🚀 STEP 1: Activate Python Environment

   cd "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"
   source qwen3-tts-env/bin/activate

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🧪 STEP 2: Run Quick Test

   cd VOICE_CLONING_SYSTEM
   ./scripts/test_voice_clone.sh

   This will:
   ✓ Check your environment
   ✓ Verify voice sample
   ✓ Generate test audio
   ✓ Save to test_outputs/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎧 STEP 3: Listen to Result

   afplay test_outputs/test_*.mp3

   Does it sound like you? ✅ = Success! 🎉

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📖 STEP 4: Read Documentation

   cat README.md                    ← Full guide
   cat docs/VOICE_REQUIREMENTS.md   ← Voice sample tips

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 STEP 5: Convert Your Own Text

   python scripts/voice_clone_tts.py \
     "Your text here" \
     voice_samples/voice_sample.wav \
     "Hey, this is my voice. I'm going to talk for about four seconds." \
     -o test_outputs/my_audio.mp3

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

⚠️  IMPORTANT NOTES:

1. 📝 Transcript must match your voice sample EXACTLY
2. 🎤 Voice sample location: voice_samples/voice_sample.wav
3. 🐍 Always activate environment first
4. 🔊 Test outputs saved to: test_outputs/

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

❓ Troubleshooting:

   Problem: Module not found
   Solution: source qwen3-tts-env/bin/activate

   Problem: Voice sounds wrong
   Solution: Check transcript matches voice_sample.wav exactly

   Problem: MP3 conversion fails
   Solution: brew install ffmpeg

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

✨ Ready to test? Run this:

   cd "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"
   source qwen3-tts-env/bin/activate
   cd VOICE_CLONING_SYSTEM
   ./scripts/test_voice_clone.sh

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📅 Status: Ready for testing
📅 Created: January 26, 2026

EOF
