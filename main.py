import urllib.request

# Ignore pre-production warnings
import warnings
warnings.filterwarnings('ignore')
import nemo
# Import Speech Recognition collection
import nemo.collections.asr as nemo_asr
# Import Natural Language Processing colleciton
import nemo.collections.nlp as nemo_nlp

Audio_sample = '2086-149220-0033.wav'

urllib.request.urlretrieve("https://dldata-public.s3.us-east-2.amazonaws.com/2086-149220-0033.wav", Audio_sample)

# Instantiate pre-trained NeMo models
# Speech Recognition model - QuartzNet
quartznet = nemo_asr.models.EncDecCTCModel.from_pretrained(model_name="QuartzNet15x5NR-En").cuda()
# Punctuation and capitalization model
punctuation = nemo_nlp.models.PunctuationCapitalizationModel.from_pretrained(model_name='Punctuation_Capitalization_with_DistilBERT').cuda()

# Convert our audio sample to text
files = [Audio_sample]
raw_text = ''
text = ''
for fname, transcription in zip(files, quartznet.transcribe(paths2audio_files=files)):
  raw_text = transcription

# Add capitalization and punctuation
res = punctuation.add_punctuation_capitalization(queries=[raw_text])
text = res[0]
print(f'\nRaw recognized text: {raw_text}. \nText with capitalization and punctuation: {text}')
