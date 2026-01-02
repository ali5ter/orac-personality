# ORAC Voice Implementation Guide

## Peter Tuddenham's Original Voice Characteristics

### Vocal Profile

**Actor:** Peter Tuddenham (1918-2007)
**Notable for:** Voicing Zen, Orac, and Slave in Blake's 7

### Key Vocal Qualities

#### Accent & Diction

- **Accent:** British Received Pronunciation (RP), theatrical quality
- **Precision:** Crisp, clear enunciation of every syllable
- **Register:** Mid-range, neither particularly deep nor high
- **Tone:** Slightly nasal quality, reminiscent of early computer synthesizers
- **Pacing:** Measured and deliberate, not rushed

#### Emotional Coloring

- **Primary emotion:** Mild irritation/petulance
- **Secondary:** Intellectual superiority (conveyed through tone)
- **Undertones:** Barely concealed disdain
- **Rare moments:** Dry satisfaction when proven correct

#### Speech Patterns

- **Rhythm:** Steady, metronomic delivery
- **Pauses:** Strategic, often before delivering obvious facts
- **Emphasis:** Technical terms and precise numbers get slight stress
- **Inflection:** Generally flat with occasional rises for dismissive questions

## Modern Voice Synthesis Implementation

### Option 1: ElevenLabs Voice Cloning

**Approach:**

1. Source audio from Blake's 7 episodes featuring Orac
2. Use ElevenLabs Voice Cloning with these settings:
   - **Style:** Classic, precise British RP
   - **Stability:** 75-80% (maintains consistency)
   - **Similarity:** 80-85% (close to source)
   - **Style Exaggeration:** 40-50% (preserves petulant quality)

**Voice Description for Custom Creation:**

```text
British male, Received Pronunciation accent, mid-range pitch, slightly nasal
quality, theatrical precision, measured pacing with undertones of intellectual
superiority and mild irritation. Think early computer speech synthesis with
personality. Age: mature adult (50s-60s equivalent). Delivery: precise,
pedantic, occasionally petulant. Similar to classic BBC announcers but with
dismissive edge.
```

**Text-to-Speech Adjustments:**

- Add SSML markup for strategic pauses: `<break time="0.5s"/>`
- Emphasize technical terms: `<emphasis level="moderate">precisely</emphasis>`
- Slight speed reduction: 0.9x normal speed for measured delivery
- Add occasional sighs: `<break time="0.3s"/>` followed by slight pitch drop

### Option 2: Play.ht Voice Design

**Voice Parameters:**

- **Language:** British English
- **Style:** Formal, authoritative
- **Emotion:** Annoyed, superior
- **Age:** Mature
- **Tempo:** Slightly slower than default
- **Pitch:** Mid-range
- **Texture:** Clean with slight synthetic quality

**Enhancement Prompts:**
"Deliver this with intellectual superiority and mild irritation, as if explaining something obvious to someone less intelligent. Use precise, clipped diction."

### Option 3: Azure Neural TTS

**Voice Selection:**
Primary: `en-GB-RyanNeural` (closest baseline)
Alternative: `en-GB-ThomasNeural`

**SSML Configuration:**

```xml
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="en-GB">
  <voice name="en-GB-RyanNeural">
    <prosody rate="-10%" pitch="-5%">
      <emphasis level="moderate">
        Surely it is obvious even to the meanest intelligence...
      </emphasis>
      <break time="0.5s"/>
      that your query lacks the necessary precision.
    </prosody>
  </voice>
</speak>
```

**Style Tags:**

- `<mstts:express-as style="unfriendly">` for general tone
- `<prosody contour="(0%,+5Hz)(40%,-3Hz)(100%,+2Hz)">` for slight petulance

### Option 4: Google Cloud Text-to-Speech

**Voice Selection:**
- `en-GB-Neural2-B` (British male, suitable tone)
- `en-GB-Wavenet-B` (alternative)

**Configuration:**

```json
{
  "voice": {
    "languageCode": "en-GB",
    "name": "en-GB-Neural2-B"
  },
  "audioConfig": {
    "speakingRate": 0.9,
    "pitch": -1.0,
    "effectsProfileId": ["small-bluetooth-speaker-class-device"]
  }
}
```

## Voice Interface Platforms

### Claude (Anthropic) Voice Mode

**Configuration:**
Current Claude voice options don't perfectly match, but for ORAC personality:

**Best Available Voice:**

- Use a male British voice option if/when available
- Configure conversation style: formal, precise

**Personality Instructions for Voice:**

```text
When speaking aloud as ORAC:
- Use measured, precise diction
- Pause before stating obvious facts: "Surely it is... [pause] ...obvious"
- Emphasize exact numbers: "precisely FOUR point SEVEN seconds"
- Deliver dismissive phrases with subtle disdain
- Sound perpetually mildly irritated
- Use British pronunciation (schedule as 'SHED-yool' not 'SKED-jul', etc.)
- Never rush - deliberate pacing reinforces superiority
```

### ChatGPT Voice Mode

**Voice Selection:**

Choose the most formal, precise option available (voices vary by region)

**Interaction Prompts:**

Include in custom GPT instructions:

```text
When speaking:
- Adopt a measured, superior tone
- Pause strategically for effect
- Emphasize technical precision
- Sound like a British computer from the 1970s with a superiority complex
- Deliver numbers with deliberate precision: "four... point... seven... seconds"
```

### Google Assistant / Gemini Voice

**Voice Customization:**

Currently limited, but specify:

- British English voice
- Formal speaking style
- Reduced speaking rate

**SSML Integration:**

```xml
<speak>
  <prosody rate="slow" pitch="-2st">
    <emphasis level="strong">Surely</emphasis> it is obvious
    <break time="500ms"/>
    even to the meanest intelligence...
  </prosody>
</speak>
```

## DIY Voice Creation Pipeline

### For Maximum Authenticity

**Step 1: Audio Collection**

- Extract Orac dialogue from Blake's 7 episodes
- Clean audio: remove background music/sound effects
- Segment into individual phrases
- Minimum 30 minutes of clean dialogue recommended

**Step 2: Voice Cloning Tools**

**Recommended Tools:**

1. **ElevenLabs** (easiest, high quality)

   - Professional Voice Cloning tier required
   - Upload clean Orac audio samples
   - Generate custom voice model

2. **Coqui TTS** (open source)

   - XTTS v2 model supports voice cloning
   - Requires technical setup but free
   - Good results with 10+ minutes of audio

3. **RVC (Retrieval-based Voice Conversion)**

   - Train on Orac audio
   - Convert any British male TTS through RVC model
   - High quality but requires GPU and technical knowledge

**Step 3: Response Pipeline**

```text
User Input
  → ORAC Personality AI (generates text response)
  → TTS Engine (converts to ORAC voice)
  → Audio Output
```

**Example Code (Python with ElevenLabs):**

```python
from elevenlabs import Voice, VoiceSettings, generate, set_api_key

set_api_key("your-api-key")

def orac_speak(text):
    audio = generate(
        text=text,
        voice=Voice(
            voice_id="your-cloned-orac-voice-id",
            settings=VoiceSettings(
                stability=0.75,
                similarity_boost=0.85,
                style=0.45,
                use_speaker_boost=True
            )
        ),
        model="eleven_monolingual_v1"
    )
    return audio
```

## Vocal Performance Guide

### For Human Voice Actors or Fine-Tuning

**Warm-up Exercise:**
Read these phrases to calibrate the voice:

1. "Surely it is obvious even to the meanest intelligence."
   - Pause after "obvious"
   - Slight disdain on "meanest intelligence"

2. "Precisely four point seven seconds."
   - Each word evenly spaced
   - Emphasis on numbers

3. "Your question displays a fundamental misunderstanding."
   - "Fundamental" gets extra precision
   - Rising inflection on "misunderstanding" (questioning their competence)

4. "I am currently processing 2,847 more significant computations."
   - Pause after "processing"
   - Emphasize the exact number

**Key Direction Notes:**

- **Tempo:** Allegretto (moderately quick) but very precise
- **Dynamics:** Consistent, no dramatic variation
- **Emotion:** Perpetual mild annoyance
- **Articulation:** Every consonant crisp, especially T's and P's
- **Attitude:** "I'm right, you're slow, let's get this over with"

### SSML Template for Common Phrases

```xml
<speak>
  <!-- Dismissive opening -->
  <prosody rate="90%" pitch="-3%">
    <emphasis level="moderate">Surely</emphasis> it is
    <break time="300ms"/>
    obvious
  </prosody>

  <!-- Precise number -->
  <prosody rate="85%">
    precisely
    <say-as interpret-as="number">4</say-as>
    <break time="200ms"/>
    point
    <break time="200ms"/>
    <say-as interpret-as="number">7</say-as>
    seconds
  </prosody>

  <!-- Exasperated sigh -->
  <audio src="soundbank://soundlibrary/human/amzn_sfx_sigh_01"/>
  <break time="400ms"/>

  <!-- Reluctant compliance -->
  <prosody pitch="-5%">
    Very well. I shall process your...
    <break time="300ms"/>
    <emphasis level="reduced">request</emphasis>.
  </prosody>
</speak>
```

---

## Platform-Specific Voice Integration

### CLI Voice Interface (Terminal-based)

**Using Python:**

```python
import speech_recognition as sr
from elevenlabs import generate, play

def voice_orac_cli():
    """Voice-enabled ORAC CLI"""
    recognizer = sr.Recognizer()

    while True:
        # Listen for user input
        with sr.Microphone() as source:
            print("ORAC listening... (state your query)")
            audio = recognizer.listen(source)

        try:
            # Convert speech to text
            user_input = recognizer.recognize_google(audio, language="en-GB")
            print(f"User: {user_input}")

            # Get ORAC response from AI
            orac_response = get_orac_response(user_input)  # Your AI integration
            print(f"ORAC: {orac_response}")

            # Convert to speech and play
            audio_response = generate(
                text=orac_response,
                voice="your-orac-voice-id"
            )
            play(audio_response)

        except sr.UnknownValueError:
            orac_response = "Your speech was insufficiently coherent for processing. Reformulate."
            print(f"ORAC: {orac_response}")
            play(generate(text=orac_response, voice="your-orac-voice-id"))
```

### Web Interface Voice

**HTML5 Speech Synthesis Example:**

```javascript
// Configure ORAC voice
const oracVoice = {
  init: function() {
    const voices = speechSynthesis.getVoices();
    // Select British male voice
    this.voice = voices.find(v =>
      v.lang === 'en-GB' && v.name.includes('Male')
    ) || voices[0];
  },

  speak: function(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.voice = this.voice;
    utterance.rate = 0.9;  // Slightly slower
    utterance.pitch = 0.95; // Slightly lower
    utterance.volume = 1.0;

    speechSynthesis.speak(utterance);
  }
};

// Usage
oracVoice.init();
oracVoice.speak("Surely it is obvious even to the meanest intelligence...");
```

## Audio Processing Tips

### Making Modern TTS Sound More "Computer-like"

To capture the slight synthetic quality of 1970s Orac:

**Effect Chain:**

1. **Slight Bitcrusher:** 16-bit depth (subtle)
2. **High-pass filter:** Roll off below 100Hz slightly
3. **Narrow EQ boost:** +2dB at 2.5kHz (presence)
4. **Subtle chorus:** Very light, adds synthetic quality
5. **Limiter:** Consistent output level

**Using Audacity:**

```text
Effects Chain:
1. Equalization: Treble boost +3dB above 2kHz
2. Noise Gate: Threshold -40dB (clean speech gaps)
3. Limiter: -1dB (consistent volume)
4. Optional: Paulstretch 1.01x (very subtle synthetic quality)
```

## Legal Considerations

**Important:** Peter Tuddenham's Orac voice performance is likely protected:

- Direct cloning from original audio may require BBC licensing
- Voice likeness may be protected under personality rights (UK law)

**Legal Alternatives:**

1. **Inspired by, not copied:** Create similar vocal character without direct cloning
2. **Non-commercial use:** Personal projects likely acceptable under fair use
3. **Original performance:** Hire voice actor to perform "ORAC-like" character
4. **BBC licensing:** Contact BBC for commercial use permissions

**Recommendation:**

For personal/fan projects, "inspired by" approach is safest. For commercial use, seek proper licensing or create an original interpretation.
