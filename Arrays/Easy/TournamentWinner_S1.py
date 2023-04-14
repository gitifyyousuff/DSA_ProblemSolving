# HOME_TEAM_WON = 1
#O(n)T|O(k)
HOME_TEAM_WON = 1
#O(n)T|O(k)
def tournamentWinner(competitions, results):
    bestTeam = ""
    scores = {bestTeam:0}

    for idx,comptn in enumerate(competitions):
        result = results[idx]
        homeTeam,awayTeam = comptn
        win_team = homeTeam if result == HOME_TEAM_WON else awayTeam

        if win_team not in scores:
            scores[win_team] = 0
        scores[win_team]+=3
        print(win_team,scores[win_team],bestTeam,scores[bestTeam])
        if scores[win_team]>scores[bestTeam]:
            bestTeam = win_team
   
    return bestTeam

# def updateScores(team,points,scores):
#     if team not in scores:
#         scores[team] = 0
#     scores[team]+=points

    

        
    

competitions =  [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
  ]
results =  [0, 0, 1]

tournamentWinner = tournamentWinner(competitions, results)
print(tournamentWinner)