# Cleanup Notes - Old TTS Attempts

## Files to Archive/Remove

These files in `law-school-common/04_SCRIPTS/` are old attempts and can be archived:

### ❌ To Remove (Failed/Obsolete)
1. **qwen_tts_mlx_converter.py**
   - Early attempt at MLX integration
   - Does NOT support voice cloning
   - Uses predefined voices only
   - Replaced by: `VOICE_CLONING_SYSTEM/scripts/voice_clone_tts.py`

2. **batch_audio_prep_converter.py**
   - Batch converter for old system
   - Not integrated with voice cloning
   - May need update later for batch operations

3. **Qwen3-TTS_README.md**
   - Documentation for old system
   - Lists predefined voices (not using voice cloning)
   - Replaced by: `VOICE_CLONING_SYSTEM/README.md`

### ✅ To Keep (Still Useful)
1. **law_school_audio_converter.py**
   - Has both voice cloning AND predefined voice support
   - More complex, includes MP3 conversion
   - Keep as reference/backup

### 🤔 Decision Needed
1. **ocr_batch.py** (in same directory)
   - Different purpose (OCR, not TTS)
   - Keep (not related to voice cloning)

## Recommended Actions

### Option A: Clean Removal
```bash
cd law-school-common/04_SCRIPTS
rm qwen_tts_mlx_converter.py
rm Qwen3-TTS_README.md
# Keep law_school_audio_converter.py as backup
```

### Option B: Archive for Reference
```bash
cd law-school-common/04_SCRIPTS
mkdir _OLD_TTS_ATTEMPTS
mv qwen_tts_mlx_converter.py _OLD_TTS_ATTEMPTS/
mv Qwen3-TTS_README.md _OLD_TTS_ATTEMPTS/
mv batch_audio_prep_converter.py _OLD_TTS_ATTEMPTS/
```

## Why These Are Obsolete

### qwen_tts_mlx_converter.py
- No voice cloning support
- Uses 1.7B model (larger, slower)
- Limited to 9 predefined voices
- No MP3 conversion

### Current System Advantages
- ✅ Voice cloning with your voice
- ✅ Smaller 0.6B model (faster)
- ✅ MP3 conversion included
- ✅ Better error handling
- ✅ Progress indicators
- ✅ Self-contained in VOICE_CLONING_SYSTEM/

## Files at Root Level

### voice_sample.wav
**Current Location**: `/1. law-school/voice_sample.wav`  
**Status**: ✅ Already copied to `VOICE_CLONING_SYSTEM/voice_samples/`  
**Action**: Can remove from root after verification

```bash
# After verifying copy exists
cd "/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"
ls -lh VOICE_CLONING_SYSTEM/voice_samples/voice_sample.wav  # Verify
rm voice_sample.wav  # Remove from root
```

## Summary

**New System**: `VOICE_CLONING_SYSTEM/`
- Self-contained
- Voice cloning capable
- Well-documented
- Ready for testing

**Old Scripts**: `law-school-common/04_SCRIPTS/`
- Can be archived
- Not using voice cloning
- Replaced by new system

---

**Decision Point**: Should we archive or delete the old attempts?
**Recommendation**: Archive to `_OLD_TTS_ATTEMPTS/` for reference
