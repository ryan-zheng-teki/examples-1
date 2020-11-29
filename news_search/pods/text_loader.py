__copyright__ = "Copyright (c) 2020 Jina AI Limited. All rights reserved."
__license__ = "Apache-2.0"

from typing import Dict

from jina.executors.crafters import BaseCrafter


##The first row has to be dropped
class TextExtractor(BaseCrafter):
    def craft(self, text: str, *args, **kwargs) -> Dict:
        character, sentence = text.split(',', 1)
        return dict(weight=1., text=sentence, meta_info=character.encode('utf8'))