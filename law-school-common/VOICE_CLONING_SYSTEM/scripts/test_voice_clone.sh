#!/bin/bash
# Quick test script for voice cloning system

echo "=========================================="
echo "VOICE CLONING SYSTEM TEST"
echo "=========================================="
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Base directory
BASEDIR="/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"
VOICE_DIR="$BASEDIR/VOICE_CLONING_SYSTEM"

# Check if we're in the right directory
if [ ! -d "$VOICE_DIR" ]; then
    echo -e "${RED}❌ Voice cloning directory not found!${NC}"
    exit 1
fi

# Check environment
if [ -z "$VIRTUAL_ENV" ]; then
    echo -e "${YELLOW}⚠️  Virtual environment not activated${NC}"
    echo "Activating environment..."
    source "$BASEDIR/qwen3-tts-env/bin/activate"
fi

echo -e "${GREEN}✅ Environment activated${NC}"
echo "Python: $(which python)"
echo ""

# Using the stabilized sample with silence buffers to break the AI loop
VOICE_SAMPLE="$VOICE_DIR/voice_samples/stabilized_sample.wav"
if [ ! -f "$VOICE_SAMPLE" ]; then
    VOICE_SAMPLE="$VOICE_DIR/voice_samples/denoised_sample.wav"
fi

# The transcript MUST match what the AI hears. Adding a period at the end
# helps the model understand that the reference sentence is finished.
TRANSCRIPT="hey this is my voice i am going to talk for about four seconds."

# Test text - starting with a neutral phrase to avoid "Hey" confusion
TEST_TEXT="Today, I am testing the high-stability mode of my voice cloning system to ensure it works for my law school studies."

# Output file
OUTPUT="$VOICE_DIR/test_outputs/test_$(date +%Y%m%d_%H%M%S).mp3"

echo "=========================================="
echo "Running voice cloning test..."
echo "=========================================="
echo "Text: $TEST_TEXT"
echo "Output: $OUTPUT"
echo ""

# Run the conversion
cd "$VOICE_DIR"
python scripts/voice_clone_tts.py \
    "$TEST_TEXT" \
    "$VOICE_SAMPLE" \
    "$TRANSCRIPT" \
    -o "$OUTPUT" \
    --skip-start 300

# Check result
if [ $? -eq 0 ] && [ -f "$OUTPUT" ]; then
    echo ""
    echo "=========================================="
    echo -e "${GREEN}✅ TEST SUCCESSFUL!${NC}"
    echo "=========================================="
    echo "Output file: $OUTPUT"
    echo "Size: $(du -h "$OUTPUT" | cut -f1)"
    echo ""
    echo "🎧 Play the audio to verify voice quality:"
    echo "   afplay \"$OUTPUT\""
    echo ""
else
    echo ""
    echo "=========================================="
    echo -e "${RED}❌ TEST FAILED${NC}"
    echo "=========================================="
    echo "Check the error messages above"
    exit 1
fi
