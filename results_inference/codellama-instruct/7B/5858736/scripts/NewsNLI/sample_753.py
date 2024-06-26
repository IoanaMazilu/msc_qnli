premise_goals_mata = 1
premise_goals_lampard = 1
hypothesis_goals_mata = 1
hypothesis_goals_lampard = 1

if hypothesis_goals_mata!= premise_goals_mata:
    label = "contradiction"
elif hypothesis_goals_lampard!= premise_goals_lampard:
    label = "contradiction"
else:
    label = "entailment"

print(label)
