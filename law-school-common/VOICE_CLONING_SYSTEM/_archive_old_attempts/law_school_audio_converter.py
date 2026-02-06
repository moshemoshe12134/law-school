#!/usr/bin/env python3
"""
Law School Audio Converter
Optimized Qwen3-TTS MLX converter for law school prep files.
Converts markdown files to high-quality audio using predefined voices or custom voice cloning.
"""

import os
import sys
import argparse
from pathlib import Path
import soundfile as sf
from mlx_audio.tts.utils import load_model
import subprocess

def text_to_audio_law_school(text, output_path, speaker="Aiden", language="English",
                           instruct="speak at a natural, conversational pace with clear American English pronunciation",
                           ref_audio=None, ref_text=None):
    """
    Convert text to audio optimized for law school content.

    Args:
        text (str): Text to convert to speech
        output_path (str): Path to save the audio file
        speaker (str): Speaker voice (default: Aiden) - used for predefined voices
        language (str): Language of the text
        instruct (str): Voice instruction for natural delivery
        ref_audio (str): Path to reference audio file for voice cloning
        ref_text (str): Transcript of the reference audio
    """

    print("Loading MLX Qwen3-TTS model...")
    if ref_audio and ref_text:
        # Use smaller 0.6B model for voice cloning (faster, less memory)
        model = load_model("mlx-community/Qwen3-TTS-12Hz-0.6B-Base-bf16")
        
        # Load the reference audio file
        print(f"Loading reference audio: {ref_audio}")
        ref_audio_data, sample_rate = sf.read(ref_audio)
        print(f"Audio loaded: {len(ref_audio_data)} samples at {sample_rate}Hz")
        
        print(f"Reference text: {ref_text}")
    else:
        # Use custom voice model for predefined speakers with emotion control
        model = load_model("mlx-community/Qwen3-TTS-12Hz-0.6B-CustomVoice-bf16")

    print(f"Generating audio for law school content ({len(text)} chars)...")

    if ref_audio and ref_text:
        # Voice cloning mode
        results = list(model.generate(
            text=text,
            ref_audio=ref_audio_data,
            ref_text=ref_text,
            language=language,
        ))
    else:
        # Predefined voice with emotion control
        results = list(model.generate_custom_voice(
            text=text,
            speaker=speaker.lower(),
            language=language,
            instruct=instruct,
        ))

    if results:
        # First save as WAV temporarily
        temp_wav = output_path
        if output_path.lower().endswith('.mp3'):
            temp_wav = output_path.replace('.mp3', '_temp.wav')

        print(f"Saving audio to: {temp_wav}")
        sf.write(temp_wav, results[0].audio, results[0].sample_rate)

        # Convert to MP3 if requested
        if output_path.lower().endswith('.mp3'):
            print("Converting to MP3...")
            convert_wav_to_mp3(temp_wav, output_path)
            # Clean up temp file
            Path(temp_wav).unlink()
            print(f"Audio saved as MP3: {output_path}")
        else:
            print("Audio generation complete!")
    else:
        print("No audio generated")

def convert_wav_to_mp3(wav_path, mp3_path):
    """Convert WAV to MP3 using ffmpeg."""
    cmd = [
        'ffmpeg', '-y',  # -y to overwrite
        '-i', wav_path,  # input
        '-codec:a', 'libmp3lame',  # MP3 codec
        '-qscale:a', '2',  # quality (2 = ~190kbps, good quality)
        mp3_path  # output
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Warning: MP3 conversion failed: {result.stderr}")
        # Fallback: keep WAV
        import shutil
        shutil.move(wav_path, mp3_path.replace('.mp3', '.wav'))
    else:
        print("MP3 conversion successful")

def read_markdown_file(file_path):
    """Read and clean markdown content for TTS."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove markdown headers and formatting for cleaner speech
    import re
    # Remove headers
    content = re.sub(r'^#+\s+', '', content, flags=re.MULTILINE)
    # Remove links
    content = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', content)
    # Remove emphasis
    content = re.sub(r'\*\*([^\*]+)\*\*', r'\1', content)
    content = re.sub(r'\*([^\*]+)\*', r'\1', content)
    # Clean up extra whitespace
    content = re.sub(r'\n\s*\n', '\n\n', content)

    return content.strip()

def main():
    parser = argparse.ArgumentParser(description="Convert law school prep files to audio")
    parser.add_argument("input", help="Input markdown file or text")
    parser.add_argument("-o", "--output", help="Output audio file path")
    parser.add_argument("-f", "--format", choices=['wav', 'mp3'], default='wav',
                       help="Output format (default: wav)")
    parser.add_argument("-s", "--speaker", default="Aiden",
                       help="Speaker voice (default: Aiden) - used when not cloning")
    parser.add_argument("-l", "--language", default="English",
                       help="Language of the text")
    parser.add_argument("-i", "--instruct",
                       default="speak at a natural, conversational pace with clear American English pronunciation",
                       help="Voice instruction - used when not cloning")
    parser.add_argument("--ref-audio", help="Path to reference audio file for voice cloning")
    parser.add_argument("--ref-text", help="Transcript of the reference audio for voice cloning")

    args = parser.parse_args()

    # Determine input type and content
    input_path = Path(args.input)
    if input_path.exists() and input_path.suffix.lower() == '.md':
        # Read markdown file
        text = read_markdown_file(input_path)
        print(f"Loaded markdown file: {input_path}")
    else:
        # Treat as direct text
        text = args.input

    # Determine output path
    if args.output:
        output_path = Path(args.output)
        # Ensure correct extension
        if not output_path.suffix:
            output_path = output_path.with_suffix(f'.{args.format}')
    else:
        if input_path.exists() and input_path.suffix.lower() == '.md':
            # Convert .md to .wav/.mp3 in same directory
            output_path = input_path.with_suffix(f'.{args.format}')
        else:
            output_path = Path(f"output.{args.format}")

    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    text_to_audio_law_school(text, str(output_path), args.speaker, args.language, args.instruct,
                             args.ref_audio, args.ref_text)

if __name__ == "__main__":
    main()