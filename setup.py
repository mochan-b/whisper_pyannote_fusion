from setuptools import setup, find_packages

setup(
    name='whisper-pyannote-fusion',
    version='0.0.1',
    description='Fuse whisper and pyannote results',
    author='Mochan Shrestha',
    install_requires=[
        'jiwer',
        'pytest',
        'pyannote.audio',
        'pyannote.metrics',
        'whisper-normalizer',
        'intervaltree',
        'openai-whisper',
        'spacy',
        'jellyfish'
    ],
)
