#!/usr/bin/env python3
"""
Voice Cloning Text-to-Speech Converter
Uses Qwen3-TTS with MLX for voice cloning on Apple Silicon.

This script converts text to audio using your own voice sample.
"""

import os
import sys
import argparse
from pathlib import Path
import soundfile as sf
import librosa
import numpy as np
from mlx_audio.tts.utils import load_model
import subprocess
import mlx.core as mx

def voice_clone_tts(text, output_path, ref_audio_path, ref_text, language="English", skip_start_ms=0):
    """
    Convert text to audio using voice cloning.

    Args:
        text (str): Text to convert to speech
        output_path (str): Path to save the audio file
        ref_audio_path (str): Path to reference audio file (WAV, 4-10 seconds recommended)
        ref_text (str): Exact transcript of the reference audio
        language (str): Language of the text (default: English)
        skip_start_ms (int): Milliseconds to trim from the start of generated audio
    """
    
    print("=" * 60)
    print("VOICE CLONING TEXT-TO-SPEECH")
    print("=" * 60)
    
    # Validate reference audio exists
    if not Path(ref_audio_path).exists():
        raise FileNotFoundError(f"Reference audio not found: {ref_audio_path}")
    
    # Clean text inputs for better tokenizer matching
    text = text.strip()
    ref_text = ref_text.strip()
    
    # ADVANCED FIX: Add a longer silent buffer (dots and space) 
    # This helps the model "settle" before speaking the actual first word
    buffered_text = "... " + text
    
    print(f"\n📝 Text to convert: {text[:100]}{'...' if len(text) > 100 else ''}")
    print(f"📝 Total characters: {len(text)}")
    print(f"🎤 Voice sample: {ref_audio_path}")
    print(f"💬 Reference text: {ref_text}")
    print(f"🌍 Language: {language}")
    
    # Load the MLX model (1.7B is higher quality for law school studies)
    print(f"\n🔄 Loading Qwen3-TTS 1.7B model (MLX-optimized)...")
    model_id = "mlx-community/Qwen3-TTS-12Hz-1.7B-Base-bf16"
    model = load_model(model_id)
    print("✅ Model loaded successfully")
    
    # Target sample rate for Qwen3-TTS is 24000 Hz
    TARGET_SR = 24000
    
    # Load the reference audio
    print(f"\n🔄 Loading reference audio...")
    ref_audio_data, sample_rate = sf.read(ref_audio_path)
    
    # Ensure audio is mono
    if len(ref_audio_data.shape) > 1:
        print(f"🔄 Converting stereo to mono...")
        ref_audio_data = librosa.to_mono(ref_audio_data.T)
    
    # Resample if necessary
    if sample_rate != TARGET_SR:
        print(f"🔄 Resampling reference audio from {sample_rate}Hz to {TARGET_SR}Hz...")
        ref_audio_data = librosa.resample(ref_audio_data, orig_sr=sample_rate, target_sr=TARGET_SR)
        sample_rate = TARGET_SR
    
    # Normalize audio levels
    ref_audio_data = librosa.util.normalize(ref_audio_data)
    
    # Convert numpy array to MLX array
    ref_audio_data = mx.array(ref_audio_data)
    audio_duration = len(ref_audio_data) / sample_rate
    print(f"✅ Audio loaded and normalized:")
    print(f"   - Duration: {audio_duration:.2f} seconds")
    print(f"   - Sample rate: {sample_rate} Hz")
    
    # Generate audio with voice cloning
    print(f"\n🎙️  Generating audio with your voice...")
    # FIXED: Updated parameters for better voice cloning quality
    # Previous parameters were too restrictive causing hallucinations
    results = list(model.generate(
        text=buffered_text,
        ref_audio=ref_audio_data,
        ref_text=ref_text,
        language=language,
        temperature=0.8,        # Increased from 0.05 - better for voice cloning
        top_k=50,               # Increased from 3 - allows more vocabulary diversity
        top_p=0.95,             # Adjusted from 1.0 - better sampling
        max_tokens=4096,
        repetition_penalty=1.1  # Reduced from 2.0 - prevents over-penalization
    ))
    
    if not results:
        print("❌ No audio generated")
        return False
    
    # Concatenate all audio segments
    full_audio = np.concatenate([res.audio for res in results])
    sr = results[0].sample_rate
    
    print("\n🧹 Post-processing audio (Removing artifacts)...")
    
    # 1. Trim leading/trailing silence from the generated audio
    # The 'top_db' parameter controls sensitivity; 20-30 is usually good for noisy starts
    full_audio, _ = librosa.effects.trim(full_audio, top_db=30)
    
    # 2. Apply requested start skip (to remove any lingering "fucked up" start)
    # We enfore a minimum skip to handle the ". " buffer we added
    actual_skip_ms = max(skip_start_ms, 500) # Increased default floor
    skip_samples = int((actual_skip_ms / 1000.0) * sr)
    if skip_samples < len(full_audio):
        print(f"✂️  Trimming first {actual_skip_ms}ms to remove hallucination buffer...")
        full_audio = full_audio[skip_samples:]
    
    # 3. Apply a short fade-in/fade-out (50ms) to prevent clicks
    fade_len = int(0.05 * sr)
    if len(full_audio) > fade_len * 2:
        fade_in = np.linspace(0, 1, fade_len)
        fade_out = np.linspace(1, 0, fade_len)
        full_audio[:fade_len] *= fade_in
        full_audio[-fade_len:] *= fade_out
    
    # 4. Final normalization
    full_audio = librosa.util.normalize(full_audio)
    
    # Determine output format
    output_format = Path(output_path).suffix.lower()
    
    if output_format == '.mp3':
        temp_wav = str(Path(output_path).with_suffix('.wav'))
        sf.write(temp_wav, full_audio, sr)
        success = convert_wav_to_mp3(temp_wav, output_path)
        if success:
            Path(temp_wav).unlink()
        else:
            return False
    else:
        sf.write(output_path, full_audio, sr)
    
    print(f"✅ Audio saved to: {output_path}")
    return True
    
    # Show file info
    output_size = Path(output_path).stat().st_size / 1024  # KB
    print(f"\n📊 Output file:")
    print(f"   - Size: {output_size:.1f} KB")
    print(f"   - Format: {output_format.upper()}")
    
    print("\n" + "=" * 60)
    print("✨ VOICE CLONING COMPLETE!")
    print("=" * 60)
    
    return True

def convert_wav_to_mp3(wav_path, mp3_path):
    """Convert WAV to MP3 using ffmpeg."""
    try:
        cmd = [
            'ffmpeg', '-y',  # -y to overwrite
            '-i', wav_path,  # input
            '-codec:a', 'libmp3lame',  # MP3 codec
            '-qscale:a', '2',  # quality (2 = ~190kbps, good quality)
            '-loglevel', 'error',  # Only show errors
            mp3_path  # output
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            print(f"❌ FFmpeg error: {result.stderr}")
            return False
        
        return True
    
    except FileNotFoundError:
        print("❌ ffmpeg not found. Please install: brew install ffmpeg")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="Voice Cloning TTS - Convert text to speech using your voice",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Basic usage (WAV output)
  python voice_clone_tts.py "Hello world" voice_sample.wav "This is my voice"
  
  # MP3 output
  python voice_clone_tts.py "Hello world" voice_sample.wav "This is my voice" -o output.mp3
  
  # From text file
  python voice_clone_tts.py "$(cat input.txt)" voice_sample.wav "This is my voice" -o output.mp3
        """
    )
    
    parser.add_argument('text', type=str, help='Text to convert to speech')
    parser.add_argument('ref_audio', type=str, help='Path to reference audio file (WAV)')
    parser.add_argument('ref_text', type=str, help='Transcript of the reference audio')
    parser.add_argument('-o', '--output', type=str, default='output.wav',
                       help='Output file path (default: output.wav)')
    parser.add_argument('-l', '--language', type=str, default='English',
                       help='Language of the text (default: English)')
    parser.add_argument('--skip-start', type=int, default=0,
                       help='Number of milliseconds to skip/trim from the start of output (default: 0)')
    
    args = parser.parse_args()
    
    try:
        success = voice_clone_tts(
            text=args.text,
            output_path=args.output,
            ref_audio_path=args.ref_audio,
            ref_text=args.ref_text,
            language=args.language,
            skip_start_ms=args.skip_start
        )
        
        sys.exit(0 if success else 1)
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
