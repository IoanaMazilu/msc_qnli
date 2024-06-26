dogsled_team_premise = 100
dogsled_team_hypothesis = 300

if dogsled_team_hypothesis <= dogsled_team_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
