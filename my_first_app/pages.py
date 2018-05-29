from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
import random
from .models import Constants


class Intro(Page):
    def before_next_page(self):
        toguess = random.randint(Constants.minguess,
                                 Constants.maxguess)
        self.player.toguess = toguess
    pass

class Guess(Page):
    form_model = 'player'
    form_fields = ['guess']

    def before_next_page(self):
        diff = self.player.guess - self.player.toguess

    pass


class ResultsWaitPage(WaitPage):

    def after_all_players_arrive(self):
        pass


class Results(Page):
    pass


page_sequence = [
    Intro,
    Guess,
    ResultsWaitPage,
    Results
]
