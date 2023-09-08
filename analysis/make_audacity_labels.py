from whisper_pyannote_fusion.audacity_labels import convert_whisper_json_to_audacity_labels, \
    convert_pyannote_json_to_audacity_labels, convert_whisper_words_to_audacity_labels, \
    convert_pyannote_whisper_json_to_audacity_labels, convert_whisperx_json_to_audacity_labels

if __name__ == '__main__':
    # Convert the json data to audacity labels
    # TODO: Move this to the unit tests
    pyannote_json = '../data/pyannote_results.json'
    convert_whisper_json_to_audacity_labels('../data/whisper_transcript.json', '../data/labels_whisper.txt')
    convert_pyannote_json_to_audacity_labels(pyannote_json, '../data/labels_pyannote.txt')
    convert_whisper_words_to_audacity_labels('../data/whisper_transcript.json', '../data/labels_whisper_words.txt')
    convert_pyannote_whisper_json_to_audacity_labels('../data/whisper_pyannote_results_1.json', pyannote_json,
                                                     '../data/labels_pyannote_whisper.txt')
    convert_whisperx_json_to_audacity_labels('../data/whisperx_alignment.json', '../data/labels_whisperx.txt')