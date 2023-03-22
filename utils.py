import re
import wordninja
from typing import List, Tuple

PUNCTUATIONS_PATTERN: re.Pattern = re.compile(r'[.!?;,:]')
SPACE_PATTERN: re.Pattern = re.compile(r' ')


def correct_text(text: str) -> Tuple[str, List[int]]:
    """
    Add missing spaces to the text

    :param text: Text to be correct
    :return: corrected text and list of the indices of added spaces in resulting text
    """

    punctuations: List[str] = []
    sub_sentences: List[str] = []
    prev_index: int = 0
    end_index: int = 0

    # Iterate over punctuation signs and split text by punctuations positions
    for match in PUNCTUATIONS_PATTERN.finditer(text):
        end_index = match.end()  # Get sign position (+1)
        punctuations.append(text[end_index - 1])  # Save sign to the corresponding list
        sub_sentences.append(text[prev_index:end_index - 1])  # Save the subtext from previous sign to the current one
        prev_index = end_index

    # Case of no punctuations or no . at the end
    if end_index < len(text):
        sub_sentences.append(text[end_index:])

    # Split the subtexts to the words and add missed spaces, then join back
    corrected_sub_sentences: List[str] = [' '.join(wordninja.split(x)) for x in sub_sentences]

    # Line up subtexts with punctuation signs adding a space after the signs
    corrected_sentences: List[str] = []
    for i, sentence in enumerate(corrected_sub_sentences):
        if i < len(punctuations):
            corrected_sentences.extend([sentence, punctuations[i] + ' '])
        elif len(sentence) > 0:
            corrected_sentences.append(sentence)

    # Finally join subtexts and signs to one text
    corrected_text: str = ''.join(corrected_sentences).strip()

    return corrected_text, find_missed_space_indexes(text, corrected_text)


def find_missed_space_indexes(original_text: str, corrected_text: str) -> List[int]:
    """
    Find indexes of space in corrected_text missed in original_text
    """

    offset: int = 0  # Offset of index for original_text to compare the symbol with corrected_text
    missed_indices: List[int] = []
    for match in SPACE_PATTERN.finditer(corrected_text):  # Iterate over spaces in corrected_text
        space_index: int = match.start()  # Get space position
        if original_text[space_index - offset] != ' ':
            missed_indices.append(space_index)
            offset += 1

    return missed_indices
