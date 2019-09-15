import string
import random

# Takes a Txt file of stats and returns "Team". A list of player stat dictionaries


def text_to_stats(team_name):
    space_count = 0
    line_count = 0
    stat_str = ""
    name_index = []
    team_name = team_name + ".txt"
# opens file and adds everything but the first two lines into stat_str
    file = open(team_name, "r")
    for line in file:
        if line_count < 2:
            line_count += 1
        else:
            stat_str += line + "\n"
# replaces all "\t" and "\n" in stat_str with "#" then splits stat_str at "#"
    stat_str = stat_str.replace("\t", "#")
    stat_str = stat_str.replace("\n", "#")
    stat_str = stat_str.split("#")
# counts all the "" in stat_str
    for i in range(len(stat_str)):
        if stat_str[i] == "":
            space_count += 1
# deletes all the "" in stat_str
    for i in range(len(stat_str) - space_count):
        if stat_str[i] == "":
            del stat_str[i]
# Creates a list off indexes for all the names in str_stat
    for i in range(len(stat_str)):
        try:
            if stat_str[i][0] in string.ascii_letters:
                name_index.append(i)
        except IndexError:
            pass

# Assigns player variables to their respective stats
    P1 = stat_str[name_index[0] - 1:name_index[1] - 1]
    P2 = stat_str[name_index[1] - 1:name_index[2] - 1]
    P3 = stat_str[name_index[2] - 1:name_index[3] - 1]
    P4 = stat_str[name_index[3] - 1:name_index[4] - 1]
    P5 = stat_str[name_index[4] - 1:name_index[5] - 1]
    P6 = stat_str[name_index[5] - 1:name_index[6] - 1]
    P7 = stat_str[name_index[6] - 1:name_index[7] - 1]
    P8 = stat_str[name_index[7] - 1:name_index[8] - 1]
    P9 = stat_str[name_index[8] - 1:name_index[9] - 1]
    P10 = stat_str[name_index[9] - 1:]

    team = [P1, P2, P3, P4, P5, P6, P7, P8, P9, P10]

    file.close()

    return team


class Player:
    def __init__(self, player_stats):
        s = player_stats
        self.stats = {"Rk": s[0], "name": s[1], "Age": s[2], "G": s[3], "GS": s[4], "MP": s[5],
                      "FG": s[6], "FGA": s[7], "FG%": s[8], "3P": s[9], "3PA": s[10], "3P%": s[11],
                      "2P": s[12], "2PA": s[13], "2P%": s[14], "FT": s[15], "FTA": s[16], "FT%": s[17],
                      "ORB": s[18], "DRB": s[19], "TRB": s[20], "AST": s[21], "STL": s[22], "BLK": s[23],
                      "TOV": s[24], "PF": s[25], "PTS": s[26]}

        self.game_stats = {"MIN": 0, "FG": 0, "3PT": 0, "FT": 0, "OREB": 0,
                           "DREB": 0, "REB": 0, "AST": 0, "STL": 0, "BLK": 0,
                           "TO": 0, "PF": 0, "+/-": 0, "PTS": 0}

    def get_stats(self):
        return self.stats

    def get_game_stat(self, stat):
        return self.game_stats[stat]

    def game_stats(self, stat, num):
        self.game_stats[stat] = num
        return


class Team:
    def __init__(self, team_name):
        self.player_1 = Player(text_to_stats(team_name)[0])
        self.player_2 = Player(text_to_stats(team_name)[1])
        self.player_3 = Player(text_to_stats(team_name)[2])
        self.player_4 = Player(text_to_stats(team_name)[3])
        self.player_5 = Player(text_to_stats(team_name)[4])
        self.player_6 = Player(text_to_stats(team_name)[5])
        self.player_7 = Player(text_to_stats(team_name)[6])
        self.player_8 = Player(text_to_stats(team_name)[7])
        self.player_9 = Player(text_to_stats(team_name)[8])
        self.player_10 = Player(text_to_stats(team_name)[9])

        self.team = [self.player_1, self.player_2, self.player_3, self.player_4, self.player_5,
                     self.player_6, self.player_7, self.player_8, self.player_9, self.player_10]

        self.starters = [self.player_1, self.player_2, self.player_3, self.player_4, self.player_5]

    def get_team(self):
        return self.team

    def get_starters(self):
        return self.starters

    def TO_or_FG(self):
        total_FG = 0.0
        total_TO = 0.0
        for player in self.starters:
            total_FG += float(player.get_stats()["FGA"])
            total_TO += float(player.get_stats()["TOV"])

        TO_or_FG = random.randrange(round(total_FG + total_TO))
        if TO_or_FG <= total_TO:
            return "TOV"
        else:
            return "FG"


# name of player who did action
    def possesion_name(self, action):
        total_action = 0.0
        tracker = 0
        action_player = ""
        for player in self.starters:
            total_action += float(player.get_stats()[action])
        roll = random.randrange(1, round(total_action) + 1)
        for player in self.starters:
            tracker += round(float(player.get_stats()[action]))
            if roll <= tracker:
                action_player = player.get_stats()["name"]
                return action_player

    def shot_chance(self, shot, player):
        if shot == "Three point":
            fg_p = "3P%"
        elif shot == "Two point":
            fg_p = "2P%"

        make_chance = round(float(player.get_stats()[fg_p]) * 100)
        chance = random.randrange(1, 101)

        if chance <= make_chance:
            shot = shot + " miss"
        else:
            shot = shot + " make"

        return shot

    def three_or_two(self, action_player):
        for player in self.team:
            if player.get_stats()["name"] == action_player:
                total_shots = round(float(player.get_stats()["3PA"]) + float(player.get_stats()["2PA"]))
                roll = random.randrange(1, total_shots + 1)
                if roll <= round(float(player.get_stats()["3PA"])):
                    shot = "Three point"
                else:
                    shot = "Two point"
                shot = self.shot_chance(shot, player)
                return shot


# A whole play returned as a string
    def possesion(self):
        action = self.TO_or_FG()
        action_player = self.possesion_name(action)
        if action == "FG":
            action = self.three_or_two(action_player)
        play = action_player + "\t" + action
        return play


class Game:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.PBP = ""
        self.time = 720
        self.scoreA = 0
        self.scoreB = 0

    def change_PBP(self, string):
        self.PBP += self.minutes() + "\t" + string + "\n"
        return

    def minutes(self):
        minutes = self.time / 60
        if minutes <= 0:
            return "0:00"
        minutes = "{0:.2f}".format(minutes)
        minutes = str(minutes)
        period = minutes.find(".")
        seconds = minutes[period:]
        minutes = minutes[:period]
        seconds = 60 * float(seconds)
        seconds = str(seconds)
        period = seconds.find(".")
        seconds = seconds[:period]
        if len(seconds) == 1:
            seconds = "0" + seconds
        time = minutes + ":" + seconds
        return time

    def tip_off(self):
        max_reb_A = 0
        max_reb_B = 0
        tipper_A = ""
        tipper_B = ""
        posessor = ""
        start = ""
        teamA = self.teamA.get_team()
        teamB = self.teamB.get_team()

        for player in teamA:
            player_TRB = float(player.get_stats()["TRB"])
            player_name = player.get_stats()["name"]
            if player_TRB >= max_reb_A:
                tipper_A = player_name
                max_reb_A = player_TRB
        for player in teamB:
            player_TRB = float(player.get_stats()["TRB"])
            player_name = player.get_stats()["name"]
            if player_TRB >= max_reb_B:
                tipper_B = player_name
                max_reb_B = player_TRB

        coin_flip = random.randrange(2)
        if coin_flip == 0:
            start = "A"
            index = random.randrange(len(teamA))
            posessor = teamA[index].get_stats()["name"]

        else:
            start = "B"
            index = random.randrange(len(teamA))
            posessor = teamB[index].get_stats()["name"]

        tip_play = tipper_A + " " + "vs" + " " + tipper_B + "(" + posessor + " " + "gains possesion" + ")"
        return tip_play, start

    def play_by_play(self):
        A_score = 0
        B_score = 0
        play = ""
        quarter = 0
        tip_play = self.tip_off()[0]
        posessor = self.tip_off()[1]
        shot_clock = random.randrange(10, 24)
        # self.change_PBP(tip_play)

        breaker = "----------------------------------------------------------"
        quarter_str = ""
        self.change_PBP(tip_play)

        for i in range(4):
            quarter += 1
            if quarter == 1:
                quarter_str = "1st Quarter"
            elif quarter == 2:
                quarter_str = "2nd Quarter"
            elif quarter == 3:
                quarter_str = "3rd Quarter"
            elif quarter == 4:
                quarter_str = "4th Quarter"
            
            self.change_PBP(breaker)
            self.change_PBP(quarter_str)
            self.change_PBP(breaker)

            while self.time > 0:
                if posessor == "A":
                    play = self.teamA.possesion()
                    self.time -= shot_clock
                    posessor = "B"
                    self.change_PBP(play)
                    shot = play.split("\t")[1]
                    print(shot)
                    if(shot == 'Two point make'):
                      A_score += 2
                    elif(shot == 'Three point make'):
                      A_score += 3
                elif posessor == "B":
                    play = self.teamA.possesion()
                    self.time -= shot_clock
                    posessor = "A"
                    self.change_PBP(play)
                    shot = play.split("\t")[1]
                    if(shot == 'Two point make'):
                      B_score += 2
                    elif(shot == 'Three point make'):
                      B_score += 3
            self.time = 720

        if(quarter == 4):
          self.PBP += "\n"
          if(A_score > B_score):
            self.PBP += "TimberWolves win {} to {}".format(A_score, B_score)
          else:
            self.PBP += "Rockets win {} to {}".format(B_score, A_score)

          if(A_score > 130 or B_score > 130):
            self.PBP += "\nYeah scores a bit high, not the most accurate simulation :("

        return self.PBP


Houston = Team("Houston")
Timberwolves = Team("Timberwolves")
Game = Game(Houston, Timberwolves)

print(Game.play_by_play())

# for i in range(1, 100):
#     print(str(Houston.possesion_name("FGA", i)[2]) + " " + str(Houston.possesion_name("FGA", i)[1]) + " " + Houston.possesion_name("FGA", i)[0])
