#!/bin/bash
# Comprehensive Test Suite for Voice Cloning System
# This runs multiple legal-themed tests to verify stability and quality.

# Colors
GREEN='\033[0;32m'
CYAN='\033[0;36m'
YELLOW='\033[1;33m'
NC='\033[0m'

BASEDIR="/Users/mosheklein/Library/CloudStorage/GoogleDrive-mosheklein.mk@gmail.com/My Drive/1. law-school"
VOICE_DIR="$BASEDIR/VOICE_CLONING_SYSTEM"
OUTPUT_DIR="$VOICE_DIR/test_outputs/suite_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$OUTPUT_DIR"

# Activate environment
source "$BASEDIR/qwen3-tts-env/bin/activate"

# Using the TRIMMED reference to remove common "Hey" hallucination tokens
VOICE_SAMPLE="$VOICE_DIR/voice_samples/trimmed_ref.wav"
TRANSCRIPT="this is my voice i am going to talk for about four seconds."

if [ ! -f "$VOICE_SAMPLE" ]; then
    echo "⚠️  Trimmed ref not found, falling back to stabilized..."
    VOICE_SAMPLE="$VOICE_DIR/voice_samples/stabilized_sample.wav"
    TRANSCRIPT="i am going to talk for about four seconds."
fi

echo -e "${CYAN}==========================================${NC}"
echo -e "${CYAN}🚀 STARTING LEGAL VOICE BENCHMARKS (V2 STABILIZED)${NC}"
echo -e "${CYAN}==========================================${NC}"
echo "Outputs will be saved to: $OUTPUT_DIR"
echo ""

run_test() {
    local label=$1
    local text=$2
    local filename=$3

    echo -e "${YELLOW}Running Test: $label...${NC}"
    python3 "$VOICE_DIR/scripts/voice_clone_tts.py" \
        "$text" \
        "$VOICE_SAMPLE" \
        "$TRANSCRIPT" \
        -o "$OUTPUT_DIR/$filename" \
        --skip-start 2000  # Increased to 2s with new parameters
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✅ Generated: $filename${NC}"
    else
        echo -e "${RED}❌ Failed: $label${NC}"
    fi
    echo "------------------------------------------"
}

# 1. Short Legal Definition
run_test "Definitions" \
"Res ipsa loquitur is a doctrine that infers negligence from the very nature of an accident or injury in the absence of direct evidence." \
"01_definition.mp3"

# 2. Case Snippet (Torts/Foreseeability)
run_test "Case Summary" \
"In the case of Palsgraf versus Long Island Railroad, Chief Judge Cardozo established that a defendant owes a duty of care only to those plaintiffs who are in the zone of foreseeable danger." \
"02_case_summary.mp3"

# 3. List and Punctuation (Checking flow)
run_test "Punctuation & Flow" \
"To prove a prima facie case for negligence, the plaintiff must establish four distinct elements: duty, breach, causation, and actual damages." \
"03_flow_test.mp3"

# 4. Question & Emphasis
run_test "Questioning" \
"Why does the court apply the business judgment rule here? It is because the law presumes that directors act in good faith and in the best interests of the corporation." \
"04_emphasis_test.mp3"

# 5. Contracts Law
run_test "Contracts" \
"A contract requires offer, acceptance, and consideration. The offer must be definite and communicated to the offeree, who then has the power to accept or reject it." \
"05_contracts.mp3"

# 6. Constitutional Law
run_test "Constitutional" \
"The First Amendment protects freedom of speech, but this protection is not absolute. The government may regulate speech that incites imminent lawless action under Brandenburg." \
"06_constitutional.mp3"

# 7. Criminal Law
run_test "Criminal" \
"In criminal law, mens rea refers to the mental state required for a crime, such as intent or knowledge. Actus reus is the physical act or conduct that constitutes the crime." \
"07_criminal.mp3"

# 8. Property Law
run_test "Property" \
"In property law, a fee simple absolute is the most complete ownership interest one can have in real property. It is perpetual, inheritable, and includes all rights to the land." \
"08_property.mp3"

# 9. Evidence Law
run_test "Evidence" \
"Hearsay is an out-of-court statement offered to prove the truth of the matter asserted. However, there are numerous exceptions to the hearsay rule, such as admissions by party opponent." \
"09_evidence.mp3"

# 10. Torts (Strict Liability)
run_test "Strict Liability" \
"Strict liability applies to activities that are inherently dangerous or involve wild animals. Unlike negligence, fault is not required for liability in strict liability cases." \
"10_strict_liability.mp3"
