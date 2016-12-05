from __future__ import print_function
import numpy

class Player:
    def __init__(self, name, avgscore, stdev, seed):
        self.name = name
        self.avgscore = avgscore
        self.stdev = stdev
        self.seed = seed

class League:
    def __init__(self, playerlist):
        assert len(playerlist)==6, "only 6 player tournaments supported, size is %d" % size    
        self.playerlist = playerlist

    def seed(self, seed):
        return next(player for player in self.playerlist if player.seed == seed)
 

class Tournament:
    def play(self, player1, player2):
        score1 = numpy.random.normal(player1.avgscore, player1.stdev)
        score2 = numpy.random.normal(player2.avgscore, player2.stdev)
        if score1 >= score2:
            return player1
        elif score2 > score1:
            return player2
        
    def run(self, league):
        semis4 = self.play(league.seed(4), league.seed(5))
        semis3 = self.play(league.seed(3), league.seed(6))
        finals1 = self.play(league.seed(1), semis4)
        finals2 = self.play(league.seed(2), semis3)
        winner = self.play(finals1, finals2)
        return winner.name
        

def main():
        
    dudes = [
        Player("Will K.", 110.61, 20.51, 1),
        Player("Asif", 103.80, 18.00, 2),
        Player("Michael", 114.45, 25.89, 3),
        Player("Evan", 97.11, 20.51, 4),
        Player("Ben", 108.41, 17.91, 5),
        Player("Andrew", 97.05, 17.40, 6)
    ]

    our_league = League(dudes)
    tournament = Tournament()
    print(tournament.run(our_league))

if __name__=='__main__':
    main()
