from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'my_first_app'
    players_per_group = None
    num_rounds = 1

    endowment = 100
    minguess = 0
    maxguess = 100


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    guess = models.IntegerField(min=Constants.minguess,
                                max=Constants.maxguess,
                                verbose_name="Please, insert \
                                any number from {} to \
                                 {}".format(Constants.minguess,
                                            Constants.maxguess,),
                                doc='guess of the player')

    toguess = models.IntegerField(min=Constants.minguess,
                                  max=Constants.maxguess,
                                  doc='random number for a player to guess')

    def set_payoff(self):
        self.diff = abs(self.guess - self.toguess)
        self.payoff = Constants.endowment - self.diff


pass

