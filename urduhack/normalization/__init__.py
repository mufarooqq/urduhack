# coding: utf8
"""
Normalization module
---------------------

The normalization of Urdu text is necessary to make it useful for the machine
learning tasks.
This module provides the following functionality:

    - Normalizing Single Characters
    - Normalizing Combine Characters
    - Put Spaces Before & After Digits
    - Put Spaces After Urdu Punctuations
    - Removal of Diacritics from Urdu Text
"""

from .character import normalize_characters, normalize_combine_characters
from .util import punctuations_space, digits_space, remove_diacritics

__all__ = ["normalize_characters", "normalize_combine_characters",
           "punctuations_space", "digits_space", "remove_diacritics",
           "normalize"]


def normalize(text: str) -> str:
    """
    To normalize some text, all you need to do pass ``unicode`` text. It will return a ``str``
    with normalized characters both single and combined, proper spaces after digits and punctuations
    and diacritics removed.

    Args:
        text (str): raw ``unicode`` Urdu text

    Returns:
        str: normalized urdu text
    """
    text = normalize_characters(text)
    text = normalize_combine_characters(text)
    text = digits_space(text)
    text = punctuations_space(text)
    text = remove_diacritics(text)
    return text
