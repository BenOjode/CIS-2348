# ZyLabs 10.15
# Benjamin Ojode
# 1663352

class Team:
    def __init__(self):
        self.teamname = 'none'
        self.teamwins = 0
        self.team_losses = 0

    def get_win_percentage(self):
        return self.teamwins/(self.teamwins + self.team_losses)

if __name__ == "__main__":
    team = Team()

    teamname = input()
    teamwins = int(input())
    team_losses = int(input())

    team.teamname = teamname
    team.teamwins = teamwins
    team.team_losses = team_losses

    if team.get_win_percentage() >= 0.5:
        print('Congratulations, Team '+ str(team.teamname) + ' has a winning average!')
    else:
        print('Team ' + str(team.teamname) + ' has a losing average.')