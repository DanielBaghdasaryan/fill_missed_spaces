import re
import wordninja
from typing import List, Tuple

PUNCTUATIONS_PATTERN: re.Pattern = re.compile(r'[.!?;,:]')
SPACE_PATTERN: re.Pattern = re.compile(r' ')


def correct_text(text: str) -> Tuple[str, List[int]]:
    punctuations: List[str] = []
    sub_sentences: List[str] = []
    prev_index: int = 0
    end_index: int = 0
    for match in PUNCTUATIONS_PATTERN.finditer(text):
        end_index = match.end()
        punctuations.append(text[end_index - 1])
        sub_sentences.append(text[prev_index:end_index - 1])
        prev_index = end_index

    # Case of no punctuations or no . at the end
    if end_index < len(text):
        sub_sentences.append(text[end_index:])

    corrected_sub_sentences: List[str] = [' '.join(wordninja.split(x)) for x in sub_sentences]

    corrected_sentences: List[str] = []
    for i, sentence in enumerate(corrected_sub_sentences):
        if i < len(punctuations):
            corrected_sentences.extend([sentence, punctuations[i] + ' '])
        elif len(sentence) > 0:
            corrected_sentences.append(sentence)

    corrected_text: str = ''.join(corrected_sentences)
    return corrected_text, find_missed_space_indexes(text, corrected_text)


def find_missed_space_indexes(original_text, corrected_text):
    offset = 0
    missed_indices = []
    for match in SPACE_PATTERN.finditer(corrected_text):
        space_index: int = match.start()
        if original_text[space_index - offset] != ' ':
            missed_indices.append(space_index)
            offset += 1
    return missed_indices
