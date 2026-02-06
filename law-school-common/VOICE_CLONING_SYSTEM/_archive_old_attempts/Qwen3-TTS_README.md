# Qwen3-TTS Integration for Law School Workflow

This directory contains scripts to convert text to speech using Qwen3-TTS, integrated with your law school audio prep workflow.

## Setup

1. **Environment**: The scripts use a dedicated virtual environment at `qwen3-tts-env/`
2. **Activation**: Always activate the environment before running scripts:
   ```bash
   source qwen3-tts-env/bin/activate
   ```

## Available Speakers (CustomVoice Model)

- **Vivian**: Bright, slightly edgy young female voice (Chinese native)
- **Serena**: Warm, gentle young female voice (Chinese native)
- **Ryan**: Dynamic male voice with strong rhythmic drive (English native)
- **Aiden**: Sunny American male voice with clear midrange (English)
- **Ono_Anna**: Playful Japanese female voice (Japanese native)
- **Sohee**: Warm Korean female voice with rich emotion (Korean native)
- **Uncle_Fu**: Seasoned male voice with low, mellow timbre (Chinese)
- **Dylan**: Youthful Beijing male voice (Chinese Beijing dialect)
- **Eric**: Lively Chengdu male voice (Chinese Sichuan dialect)

## Usage

### Single Text to Audio

Convert any text to speech:
```bash
# Activate environment first
source qwen3-tts-env/bin/activate

# Basic usage
python qwen_tts_converter.py "Your text here"

# With custom speaker and output
python qwen_tts_converter.py "Hello world" -s Ryan -o hello.wav

# With language specification
python qwen_tts_converter.py "Bonjour le monde" -l French -s Vivian
```

### Batch Convert Audio Prep Files

Convert all audio prep files in a course to audio:
```bash
# Activate environment first
source qwen3-tts-env/bin/activate

# Convert all audio prep files in Torts course
python batch_audio_prep_converter.py ACTIVE/Torts

# With custom speaker
python batch_audio_prep_converter.py ACTIVE/Torts -s Serena
```

This will:
- Find all `*_audio.md` files in `ACTIVE/{Course}/02_PREP/audio/`
- Extract the text content (removing markdown formatting)
- Generate corresponding `.wav` audio files
- Save them alongside the original markdown files

## Integration with Workflow

### Pre-Class Prep Enhancement
- Generate audio versions of your text prep files for listening during commutes
- Use different speakers for different types of content (e.g., Vivian for statutes, Ryan for arguments)

### Study Sessions
- Convert outline sections to audio for spaced repetition
- Create audio versions of practice questions and answers

## Performance Notes

- **First run**: Model download may take time (several GB)
- **GPU recommended**: Use CUDA if available for faster processing
- **Memory**: 1.7B model requires ~8GB VRAM, 0.6B model needs ~4GB
- **Quality**: CustomVoice model provides consistent, high-quality speech

## Troubleshooting

- **CUDA issues**: If GPU not available, the script will fall back to CPU (slower)
- **Memory errors**: Try the smaller 0.6B model by editing the model name in scripts
- **Network issues**: Models download automatically on first use

## File Locations

- Scripts: `law-school-common/04_SCRIPTS/`
- Environment: `qwen3-tts-env/`
- Audio outputs: Same directory as input markdown files