import re
import wordninja
from typing import List

PUNCTUATIONS_PATTERN = re.compile(r'[.!?;,:]')


def correct_text(text: str) -> str:
    punctuations: List[str] = []
    sub_sentences: List[str] = []
    prev_index: int = 0
    for match in PUNCTUATIONS_PATTERN.finditer(text):
        end_index: int = match.end()
        punctuations.append(text[end_index - 1])
        sub_sentences.append(text[prev_index:end_index - 1].strip())
        prev_index = end_index

    corrected_sub_sentences: List[str] = [' '.join(wordninja.split(x)) for x in sub_sentences]

    corrected_sentence: List[str] = []
    for i, sentence in enumerate(corrected_sub_sentences):
        if i < len(punctuations):
            corrected_sentence.extend([sentence, punctuations[i] + ' '])
        elif len(sentence) > 0:
            corrected_sentence.append(sentence)
    return ''.join(corrected_sentence).strip()
