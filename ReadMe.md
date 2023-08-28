# Whisper PyAnnote Fusion

This library contains some techniques for fusing Whisper ASR output with PyAnnote output.

_Whisper ASR is a model for voice to text transcription. PyAnnote is a model for speaker diarization._ 

It has the following features:
- Single line command to run both whisper and pyannote and then get the ASR and diarization results
- Contains some basic metrics for evaluating the performance of the fusion 
- Small dataset for testing the fusion

## Installation

- Please get or retrieve the hugging face API key. This is needed for the pyannote models. Additionally, you will have to go to the model cards and accept the terms and conditions.
  - Diarization model: https://huggingface.co/pyannote/speaker-diarization
  - Voice activity detection model: https://huggingface.co/pyannote/voice-activity-detection
- Please install `pyannote.audio` from the github repo (https://github.com/pyannote/pyannote-audio) using the following command:
`pip install -qq https://github.com/pyannote/pyannote-audio/archive/refs/heads/develop.zip` (Substitute `pip` for `pipenv` if you wish to use that)
- Install whisperx from the github repo () with the command `pip install git+https://github.com/m-bain/whisperx.git#egg=whisperx` (Substitute `pip` for `pipenv` if you wish to use that)
- Install the spacy model for english:
`python -m spacy download en_core_web_sm`

### Troubleshooting installation

I had to comment out line `from pytorch_lightning.utilities.cloud_io import load as pl_load` since `cloud_io` seems to have moved to `lightning_fabrics`. If the models haven't been downloaded yet this will probably make it not work. However, it should fixed in the future and I'm just noting it here in case it's an issue for someone.

Changing the line to `from lightning_fabric.utilities.cloud_io import _load as pl_load`might work.

Pyannote does require a lot of things to be set up right to function. Please be sure to accept the terms and conditions and get the API key on hugging face. Make sure the right key is being passed through. 

## Data Source

Most of the testing and training was done on one episode of TWIML. This episode is https://twimlai.com/podcast/twimlai/are-llms-overhyped-or-under-appreciated/ and the mp3 file can be downloaded from https://chrt.fm/track/4D4ED/traffic.megaphone.fm/MLN5101605789.mp3?updated=1682369086