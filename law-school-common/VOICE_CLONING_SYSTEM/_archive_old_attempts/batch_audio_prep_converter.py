#!/usr/bin/env python3
"""
Batch Qwen3-TTS Converter for Law School Audio Prep Files
Converts audio prep markdown files to speech audio files.
"""

import os
import sys
import re
from pathlib import Path
import soundfile as sf
from qwen_tts import Qwen3TTSModel
import torch
import frontmatter

def extract_text_from_audio_prep(markdown_path):
    """
    Extract the main text content from an audio prep markdown file.
    Removes frontmatter and formatting, keeps the conversational content.
    """
    with open(markdown_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Parse frontmatter
    post = frontmatter.loads(content)
    text_content = post.content

    # Remove markdown headers and formatting
    # Keep section headers but make them conversational
    text_content = re.sub(r'^#{1,6}\s+', '', text_content, flags=re.MULTILINE)
    text_content = re.sub(r'\*\*([^*]+)\*\*', r'\1', text_content)  # Remove bold
    text_content = re.sub(r'\*([^*]+)\*', r'\1', text_content)    # Remove italic
    text_content = re.sub(r'`([^`]+)`', r'\1', text_content)      # Remove code
    text_content = re.sub(r'^\s*[-*+]\s+', '', text_content, flags=re.MULTILINE)  # Remove list markers
    text_content = re.sub(r'\n\s*\n\s*\n+', '\n\n', text_content)  # Clean up spacing

    return text_content.strip()

def batch_convert_audio_preps(course_dir, speaker="Vivian", language="English"):
    """
    Convert all audio prep files in a course directory to audio files.
    """
    course_path = Path(course_dir)
    audio_prep_dir = course_path / "02_PREP" / "audio"

    if not audio_prep_dir.exists():
        print(f"Audio prep directory not found: {audio_prep_dir}")
        return

    print(f"Loading Qwen3-TTS CustomVoice model...")
    model = Qwen3TTSModel.from_pretrained(
        "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice",
        device_map="auto",
        dtype=torch.bfloat16 if torch.cuda.is_available() else torch.float32,
        attn_implementation="flash_attention_2" if torch.cuda.is_available() else None,
    )

    # Find all audio prep markdown files
    audio_prep_files = list(audio_prep_dir.glob("*_audio.md"))

    if not audio_prep_files:
        print(f"No audio prep files found in {audio_prep_dir}")
        return

    print(f"Found {len(audio_prep_files)} audio prep files to convert")

    for prep_file in audio_prep_files:
        print(f"\nProcessing: {prep_file.name}")

        # Extract text content
        text_content = extract_text_from_audio_prep(prep_file)
        if not text_content:
            print(f"  Skipping {prep_file.name} - no text content found")
            continue

        # Generate output path
        output_path = prep_file.with_suffix('.wav')

        print(f"  Generating audio ({len(text_content)} characters)...")

        try:
            wavs, sr = model.generate_custom_voice(
                text=text_content,
                language=language,
                speaker=speaker,
            )

            sf.write(output_path, wavs[0], sr)
            print(f"  ✓ Saved: {output_path.name}")

        except Exception as e:
            print(f"  ✗ Error processing {prep_file.name}: {e}")

    print(f"\nBatch conversion complete!")

def main():
    import argparse

    parser = argparse.ArgumentParser(description="Batch convert audio prep files to speech")
    parser.add_argument("course_dir", help="Path to course directory (e.g., ACTIVE/Torts)")
    parser.add_argument("-s", "--speaker", default="Vivian",
                       help="Speaker voice (Vivian, Serena, Ryan, etc.)")
    parser.add_argument("-l", "--language", default="English",
                       help="Language of the text")

    args = parser.parse_args()

    batch_convert_audio_preps(args.course_dir, args.speaker, args.language)

if __name__ == "__main__":
    main()