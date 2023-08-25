# Whisper PyAnnote Fusion

This library contains some techniques for fusing Whisper ASR output with PyAnnote output.

_Whisper ASR is a model for voice to text transcription. PyAnnote is a model for speaker diarization._ 

It has the following features:
- Single line command to run both whisper and pyannote and then get the ASR and diarization results
- Contains some basic metrics for evaluating the performance of the fusion 
- Small dataset for testing the fusion

## Installation

- Install the spacy model for english:
`python -m spacy download en_core_web_sm`
