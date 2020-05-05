import os
from librosa.util import fix_length
from librosa.core import load
from librosa.output import write_wav
import soundfile as sf


files = [f'{i}.wav' for i in range(99)]

deepvoice = '/home/jan/synthesized_audio/deepvoice3'
efficient_tts = '/home/jan/synthesized_audio/efficient_tts'
tacotron2 = '/home/jan/synthesized_audio/tacotron_2'
reference = '/home/jan/synthesized_audio/reference'
fertility = '/home/jan/synthesized_audio/fertility'
fertility_griffin = '/home/jan/synthesized_audio/fertility_griffin'

# TODO:
# load each file, find max len and pad all remaining to the same length. Save
for f in files:
    dv = load(os.path.join(deepvoice, f))[0]
    et = load(os.path.join(efficient_tts, f))[0]
    t2 = load(os.path.join(tacotron2, f))[0]
    fert = load(os.path.join(fertility, f))[0]
    fert_grif = load(os.path.join(fertility_griffin, f))[0]
    ref = load(os.path.join(reference, f))[0]
    
    max_len = max(len(dv), len(et), len(t2), len(ref), len(fert), len(fert_grif))
    
    dv = fix_length(dv, max_len)[:, None].repeat(2, axis=1)
    et = fix_length(et, max_len)# [:, None].repeat(2, axis=1)
    t2 = fix_length(t2, max_len)[:, None].repeat(2, axis=1)
    ref = fix_length(ref, max_len)[:, None].repeat(2, axis=1)
    fert = fix_length(fert, max_len)[:, None].repeat(2, axis=1)
    fert_grif = fix_length(fert_grif, max_len)[:, None].repeat(2, axis=1)
        
    sf.write(os.path.join(deepvoice, f), dv, 22050, subtype='PCM_16')
    sf.write(os.path.join(efficient_tts, f), et, 22050, subtype='PCM_16')
    sf.write(os.path.join(tacotron2, f), t2, 22050, subtype='PCM_16')
    sf.write(os.path.join(reference, f), ref, 22050, subtype='PCM_16')
    sf.write(os.path.join(fertility, f), fert, 22050, subtype='PCM_16')
    sf.write(os.path.join(fertility_griffin, f), fert_grif, 22050, subtype='PCM_16')
