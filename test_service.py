
from transcribe_searvice import transcribe
import urllib.request
import os
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

transcribe(Audio_sample)