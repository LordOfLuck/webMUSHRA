import yaml, os

class MyDumper(yaml.Dumper):

    def increase_indent(self, flow=False, indentless=False):
        return super(MyDumper, self).increase_indent(flow, False)


folder = 'configs/resources/audio/synthesized_audio/'


with open(os.path.join(folder, 'test_sentences.txt')) as f:
    sentences = [s.strip() for s in f.readlines()]

output = {
    'testname': 'Compare TTS models',
    'testId': 'tts_random',
    'bufferSize': '4096',  # this actually influences if the app fails or not :/
    'stopOnErrors': True,
    'showButtonPreviousPage': True,
    'remoteService': 'service/write.php',

    'pages': [
        {
          'type': 'generic',
          'id': 'intro_page',
          'name': 'Welcome to this survey',
          'content': 'Some welcome text.',
        }
    ]
}

for i, s in enumerate(sentences):
    page = {
      'type': 'mushra',
      'id': 'sentence'+str(i),
      'name': 'Some name',
      'content': s,
      'showWaveform': True,
      'enableLooping': False,
      'reference': f'configs/resources/audio/synthesized_audio/reference/{i}.wav',
      'createAnchor35': False,
      'createAnchor70': False,
      'randomize': True,
      'showConditionNames': False,
      'stimuli': {
          'deep_voice': f'configs/resources/audio/synthesized_audio/deepvoice3/{i}.wav',
          'efficient_tts': f'configs/resources/audio/synthesized_audio/efficient_tts/{i}.wav',
          'tacotron_2': f'configs/resources/audio/synthesized_audio/tacotron_2/{i}.wav',
        }    
    }
    output['pages'].append(page)


output['pages'].append(
    {
      'type': 'finish',
      'name': 'Thank you!',
      'content': 'Some welcome text.',
      'writeResults': True
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



