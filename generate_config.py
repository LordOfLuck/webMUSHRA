import yaml, os

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


folder = 'configs/resources/audio/synthesized_audio/'


with open(os.path.join(folder, 'test_sentences.txt')) as f:
    sentences = [s.strip() for s in f.readlines()]

output = {
    'testname': 'Compare TTS models',
    'testId': 'tts_experiment',
    'bufferSize': '4096',  # this actually influences if the app fails or not :/
    'stopOnErrors': True,
    'showButtonPreviousPage': True,
    'remoteService': 'service/write.php',

    'pages': [
        {
          'type': 'generic',
          'id': 'intro_page',
          'name': 'Speech synthesis evaluation',
          'content': 'Hi, <b>welcome</b> to this speech synthesis survey. My name is Jan Vainer and I need your help! In my thesis, I tried to develop a high-quality <b>speech synthesis system</b>. But before submitting the thesis, <b>the system needs a quality evaluation</b>. Please evaluate the following sentence recordings according to overall quality. Your rating should cover <b>perceived speech fluency</b> and <b>voice quality</b>. On each page, you will be presented with 5 recordings of the same sentence. One recording is synthesized from my system, three recordings are synthesized from other systems and the last recording is a human speaker. The recordings are randomly shuffled. There will be <b>10 pages in total</b> and the survey should take between <b>5 to 7 minutes</b>.',
        }
    ]
}

for i, s in enumerate(sentences):
    page = {
      'type': 'mushra',
      'id': 'sentence'+str(i),
      'name': s,
      'content': 'Please rate each audio according to perceived speech quality and fluency.',
      'showWaveform': False,
      'enableLooping': False,
      'reference': f'configs/resources/audio/synthesized_audio/reference/{i}.wav',
      'createAnchor35': False,
      'createAnchor70': False,
      'randomize': True,
      'showConditionNames': False,
      'stimuli': {
          'deep_voice': f'configs/resources/audio/synthesized_audio/deepvoice3/{i}.wav',
          'fertiliity_griffin': f'configs/resources/audio/synthesized_audio/fertility_griffin/{i}.wav',
          'tacotron_2': f'configs/resources/audio/synthesized_audio/tacotron_2/{i}.wav',
          'fertility': f'configs/resources/audio/synthesized_audio/fertility/{i}.wav',
        }    
    }
    output['pages'].append(page)


output['pages'].append(
    {
      'type': 'finish',
      'name': 'Thank you!',
      'content': 'Your evaluation is much appreciated! ;)',
      'writeResults': True,
      'questionnaire':
          {'-type' : 'likert',
            'name': 'gender',
            'label': 'Gender',
            'response':
             { 
               '-value' : 'female',
               'label': 'Female',
               '-value': 'male',
               'label': 'Male',
               '-value': 'other',
               'label': 'Other'
             }
           }
    }
)


with open(os.path.join('configs', 'tts_experiment.yaml'), 'w') as f:
    yaml.dump(
        output, 
        f, 
        default_flow_style=False, 
        allow_unicode=True, 
        sort_keys=False, 
        Dumper=MyDumper, 
        indent=2
    )
    print(yaml.dump(output, default_flow_style=False, allow_unicode=True, sort_keys=False, Dumper=MyDumper, indent=2))



