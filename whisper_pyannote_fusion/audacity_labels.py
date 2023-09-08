import json


def convert_whisper_json_to_audacity_labels(json_filename, labels_file):
    """
    Convert the whisper json file to audacity labels
    :param json_filename:  Whisper json filename
    :param labels_file:  Audacity labels filename to write to
    :return: None
    """
    # Open the json file
    with open(json_filename, 'r') as f:
        data = json.load(f)

    # Open the labels file for writing
    with open(labels_file, 'w') as f:
        for dialog in data['segments']:
            f.write('{}\t{}\t{}\n'.format(dialog['start'], dialog['end'], dialog['text']))


def convert_pyannote_json_to_audacity_labels(json_filename, labels_file):
    """
    Convert the pyannote json file to audacity labels
    :param json_filename:  Pyannote json filename
    :param labels_file:  Audacity labels filename to write to
    :return: None
    """
    # Open the json file
    with open(json_filename, 'r') as f:
        data = json.load(f)

    # Open the labels file for writing
    with open(labels_file, 'w') as f:
        for dialog in data['segments']:
            f.write('{}\t{}\t{}\n'.format(dialog['start'], dialog['end'], str(dialog['speaker'])))


def convert_whisper_words_to_audacity_labels(json_filename, labels_file):
    """
    Convert the whisper json file to audacity labels for each word in the segments
    :param json_filename:  Whisper json filename
    :param labels_file:  Audacity labels filename to write to
    :return: None
    """
    # Open the json file
    with open(json_filename, 'r') as f:
        data = json.load(f)

    # Open the labels file for writing
    with open(labels_file, 'w') as f:
        for segment in data['segments']:
            for word in segment['words']:
                f.write('{}\t{}\t{}\n'.format(word['start'], word['end'], word['word']))


def convert_pyannote_whisper_json_to_audacity_labels(json_filename, pyannote_json_filename, labels_file):
    """
    Convert the pyannote whisper json file to audacity labels
    :param json_filename:  Pyannote whisper json filename
    :param labels_file:  Audacity labels filename to write to
    :return: None
    """
    # Open the json files
    with open(json_filename, 'r') as f:
        data = json.load(f)
    with open(pyannote_json_filename, 'r') as f:
        pyannote_data = json.load(f)

    # Open the labels file for writing
    with open(labels_file, 'w') as f:
        for whisper_output, pyannote_segment in zip(data['whisper_outputs'], pyannote_data['segments']):
            # Check if segments exist
            if 'segments' not in whisper_output:
                continue
            for segment in whisper_output['segments']:
                segment_start = pyannote_segment['start']
                for word in segment['words']:
                    f.write(
                        '{}\t{}\t{}\n'.format(segment_start + word['start'], segment_start + word['end'], word['word']))


def convert_whisperx_json_to_audacity_labels(json_filename, labels_file):
    """
    Convert the whisperx json file to audacity labels for each word in the segments
    :param json_filename:  Whisperx json filename
    :param labels_file:  Audacity labels filename to write to
    :return: None
    """
    # Open the json file
    with open(json_filename, 'r') as f:
        data = json.load(f)

    # Open the labels file for writing
    with open(labels_file, 'w') as f:
        for dialog in data['segments']:
            for word in dialog['words']:
                # Check that the word has a start, end and word. If not, then skip
                if 'start' not in word or 'end' not in word or 'word' not in word:
                    continue
                f.write('{}\t{}\t{}\n'.format(word['start'], word['end'], word['word']))
