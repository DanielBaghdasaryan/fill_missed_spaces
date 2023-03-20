import re
import wordninja
from typing import List

PUNCTUATIONS_SET: str = r'[.!?;,:]'


def correct_text(sentence: str) -> str:
    punctuations: List[str] = [x for x in sentence if re.match(PUNCTUATIONS_SET, x)]
    sub_sentences: List[str] = re.split(PUNCTUATIONS_SET, sentence)
    corrected_sub_sentences: List[str] = [' '.join(wordninja.split(x)) for x in sub_sentences]

    corrected_sentence: List[str] = []
    for i, sentence in enumerate(corrected_sub_sentences):
        if i < len(punctuations):
            corrected_sentence.extend([sentence, punctuations[i] + ' '])
        elif len(sentence) > 0:
            corrected_sentence.append(sentence)
    return ''.join(corrected_sentence).strip()
