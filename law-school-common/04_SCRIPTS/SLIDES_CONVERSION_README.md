# PPTX to Markdown Converter - Setup & Usage Guide

## 🎯 Purpose
Convert visual PowerPoint lecture slides to clean Markdown format using modern Vision Language Models (VLMs) and OCR.

## 📦 Installation

### Step 1: Install System Dependencies

**macOS:**
```bash
brew install --cask libreoffice
brew install imagemagick
```

**Ubuntu/Debian:**
```bash
apt-get install libreoffice imagemagick
```

### Step 2: Install Python Dependencies

**Minimum (Simple text extraction only):**
```bash
pip install python-pptx Pillow
```

**Recommended (with VLM/OCR capabilities):**

Choose ONE of these backends:

**Option A: PyVisionAI (Best for complex visual slides)**
```bash
pip install pyvisionai openai
# Requires OpenAI API key - set as: export OPENAI_API_KEY="your-key"
# Or use local Ollama: brew install ollama && ollama pull llava
```

**Option B: olmOCR (Local VLM, no API needed)**
```bash
pip install olmocr
# Requires: Python >=3.11 and GPU with CUDA
```

## 🚀 Usage

### Quick Start - Simple Extraction

For slides with mostly text (fastest, no API needed):
```bash
python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "ACTIVE/CrimLaw/01_SOURCES/original_sources/lecture_slides/2025_Spring" \
  --backend simple \
  --output "ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md"
```

### Advanced - With VLM/OCR

For visual slides with diagrams, charts, complex layouts:

**Using PyVisionAI + OpenAI GPT-4 Vision (best quality):**
```bash
export OPENAI_API_KEY="your-api-key-here"

python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "ACTIVE/CrimLaw/01_SOURCES/original_sources/lecture_slides/2025_Spring" \
  --backend pyvisionai \
  --output "ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md"
```

**Using PyVisionAI + Ollama (local, free):**
```bash
# Start Ollama server
ollama serve &
ollama pull llava

python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "ACTIVE/CrimLaw/01_SOURCES/original_sources/lecture_slides/2025_Spring" \
  --backend pyvisionai \
  --output "ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md"
```

**Using olmOCR (local VLM):**
```bash
python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "ACTIVE/CrimLaw/01_SOURCES/original_sources/lecture_slides/2025_Spring" \
  --backend olmocr \
  --output "ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md"
```

### Convert Single File
```bash
python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "path/to/slide.pptx" \
  --backend simple
```

## 🎛️ Backend Options

| Backend | Quality | Speed | Requirements | Best For |
|---------|---------|-------|--------------|----------|
| **simple** | Basic | ⚡⚡⚡ | None | Text-heavy slides |
| **pyvisionai** | ⭐⭐⭐⭐⭐ | ⚡ | OpenAI API or Ollama | Complex visual slides |
| **olmocr** | ⭐⭐⭐⭐ | ⚡⚡ | GPU + CUDA | Scientific content |
| **gotocr** | ⭐⭐⭐⭐ | ⚡⚡ | Manual setup | Technical diagrams |
| **qwen** | ⭐⭐⭐⭐ | ⚡⚡ | Manual setup | Charts & diagrams |

## 📁 Output Structure

**Example for CrimLaw slides:**
```
ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md/
├── 02 Elements of Crime.md
├── 03 Broken Windows Presentation.md
├── 03 Constitutional Limits Powerpoint 2024.md
├── 04 The Law of Homicide.md
├── 05 Why We Punish COMPLETE.md
├── 05.2 The Function of the Criminal Law.md
├── 06 Capital Punishment Lectures.md
├── 07 Sexual Assault.md
├── 08 Hard Devlin Morality Regulation of Vice.md
└── 09 justification and excuse.md
```

## 💡 Tips

### For Visual/Complex Slides
- Use `pyvisionai` or `olmocr` backends
- These understand diagrams, charts, images
- Extract visual context, not just text

### For Text-Heavy Slides
- Use `simple` backend
- Much faster
- No API costs

### Cost Considerations
- **simple**: Free
- **pyvisionai + OpenAI**: ~$0.01 per slide image with GPT-4 Vision
- **pyvisionai + Ollama**: Free (local)
- **olmocr**: Free (local, requires GPU)

### Troubleshooting

**LibreOffice not found:**
- Make sure it's installed: `which soffice`
- Add to PATH if needed

**ImageMagick not found:**
- Install: `brew install imagemagick` (macOS)
- Check: `which convert`

**GPU/CUDA errors with olmOCR:**
- olmOCR requires CUDA-capable GPU
- Use `pyvisionai` with Ollama instead for CPU-based processing

**Import errors:**
- Ensure all dependencies installed: `pip install -r slides_vlm_requirements.txt`

## 🔄 Recommended Workflow for Your CrimLaw Slides

Based on your slides being "very visual":

1. **First, try simple extraction** to see baseline:
```bash
cd "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"

python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "ACTIVE/CrimLaw/01_SOURCES/original_sources/lecture_slides/2025_Spring" \
  --backend simple \
  --output "ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md"
```

2. **If results are poor (missing visual content), install Ollama** (free, local):
```bash
brew install ollama
ollama serve &
ollama pull llava
```

3. **Re-run with PyVisionAI + Ollama**:
```bash
python law-school-common/04_SCRIPTS/slides_to_markdown_vlm.py \
  "ACTIVE/CrimLaw/01_SOURCES/original_sources/lecture_slides/2025_Spring" \
  --backend pyvisionai \
  --output "ACTIVE/CrimLaw/01_SOURCES/lecture_slides_md"
```

This gives you high-quality OCR with visual understanding, completely free and local!

## 📚 References

- PyVisionAI: https://pyvisionai.com/
- olmOCR: https://pypi.org/project/olmocr/
- GOT-OCR 2.0: https://github.com/ucaslcl/GOT-OCR2.0
- Qwen2.5-VL: https://github.com/QwenLM/Qwen2-VL
