#!/usr/bin/env python3
"""
Qwen3-TTS MLX Converter (Fastest for Mac)
Uses Apple's MLX framework for native performance on Apple Silicon.
"""

import os
import sys
import argparse
from pathlib import Path
import soundfile as sf
from mlx_audio.tts.utils import load_model

def text_to_audio_mlx(text, output_path, speaker="Vivian", language="English", instruct=None):
    """
    Convert text to audio using MLX-optimized Qwen3-TTS.

    Args:
        text (str): Text to convert to speech
        output_path (str): Path to save the audio file
        speaker (str): Speaker voice to use
        language (str): Language of the text
        instruct (str): Optional instruction for voice style
    """

    print("Loading MLX Qwen3-TTS model...")
    # Use the MLX-optimized community model
    model = load_model("mlx-community/Qwen3-TTS-12Hz-1.7B-CustomVoice-bf16")

    print(f"Generating audio for text: {text[:50]}...")

    # Prepare generation parameters
    gen_kwargs = {
        "text": text,
        "speaker": speaker,
        "language": language,
    }

    if instruct:
        gen_kwargs["instruct"] = instruct

    # Generate audio
    results = list(model.generate_custom_voice(**gen_kwargs))

    if results:
        print(f"Saving audio to: {output_path}")
        sf.write(output_path, results[0].audio, results[0].sample_rate)
        print("Audio generation complete!")
    else:
        print("No audio generated")

def main():
    parser = argparse.ArgumentParser(description="Convert text to speech using MLX Qwen3-TTS")
    parser.add_argument("text", help="Text to convert to speech")
    parser.add_argument("-o", "--output", help="Output audio file path (default: output.wav)")
    parser.add_argument("-s", "--speaker", default="Vivian",
                       help="Speaker voice (Vivian, Serena, Ryan, etc.)")
    parser.add_argument("-l", "--language", default="English",
                       help="Language of the text")
    parser.add_argument("-i", "--instruct", help="Voice instruction (e.g., 'speak excitedly')")

    args = parser.parse_args()

    output_path = args.output or "output.wav"

    # Ensure output directory exists
    output_dir = Path(output_path).parent
    output_dir.mkdir(parents=True, exist_ok=True)

    text_to_audio_mlx(args.text, output_path, args.speaker, args.language, args.instruct)

if __name__ == "__main__":
    main()