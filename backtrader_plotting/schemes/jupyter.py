from .blackly import Blackly
from .tradimo import Tradimo


class BlacklyJupyter(Blackly):
    def _set_params(self):
        super()._set_params()

        self.tag_pre_background_color = None
        self.tag_pre_text_color = None


class TradimoJupyter(Tradimo):
    def _set_params(self):
        super()._set_params()

        self.tag_pre_background_color = None
        self.tag_pre_text_color = None
