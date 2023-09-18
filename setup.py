from setuptools import setup, find_packages

long_description = """Algorithms to fuse whisper and pyannote outputs to get transcript as well as speaker diarization.
For full information please see blog post:
http://mochan.info/deep-learning/whisper/pyannote/asr/diarization/2023/09/07/whisper-pyannote-fusion.html
"""

setup(
    name='whisper-pyannote-fusion',
    version='0.0.3',
    description='Fuse whisper and pyannote results',
    author='Mochan Shrestha',
    packages=['whisper_pyannote_fusion'],
    install_requires=[
        'jiwer',
        'pytest',
        'pyannote.audio',
        'pyannote.metrics',
        'whisper-normalizer',
        'intervaltree',
        'openai-whisper',
        'spacy',
        'jellyfish',
        'torch',
        'torchvision'
    ],
    long_description=long_description,
)
