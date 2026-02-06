#!/bin/bash
# Voice Recording Script for Qwen3-TTS Voice Cloning
# Records a 3-5 second sample of your voice

echo "🎤 Voice Recording for Qwen3-TTS Voice Cloning"
echo "=============================================="
echo ""
echo "Instructions:"
echo "1. Find a quiet place to record"
echo "2. Speak clearly and naturally"
echo "3. Say: 'This is a sample of my voice for text-to-speech cloning.'"
echo "4. Recording will be 3 seconds long"
echo ""
echo "Press Enter to start recording..."
read

# Record for 3 seconds at 16kHz mono (optimal for TTS)
sox -d -r 16000 -c 1 -b 16 voice_sample.wav trim 0 3

echo ""
echo "✅ Recording complete!"
echo "📁 File saved as: voice_sample.wav"
echo ""
echo "To use with your script:"
echo "python law-school-common/04_SCRIPTS/law_school_audio_converter.py \\"
echo "  'Your law school content here' \\"
echo "  --ref-audio voice_sample.wav \\"
echo "  --ref-text 'This is a sample of my voice for text-to-speech cloning.' \\"
echo "  -f mp3"