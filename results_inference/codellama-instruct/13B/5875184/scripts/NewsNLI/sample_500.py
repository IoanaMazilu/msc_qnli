# define variables for the numerical entities in the premise
sevilla_goals = 3
zaragoza_goals = 1

# define variables for the numerical entities in the hypothesis
sevilla_goals_hypothesis = 3
zaragoza_goals_hypothesis = 1

# check if the number of goals scored by Sevilla in the hypothesis contradicts the number of goals scored by Sevilla in the premise
if sevilla_goals_hypothesis!= sevilla_goals:
    label = "contradiction"
elif zaragoza_goals_hypothesis!= zaragoza_goals:
    label = "contradiction"
else:
    label = "entailment"

print(label)
