# define variables for the numerical entities in the premise and hypothesis
games_premise = 1
games_hypothesis = 1
draws_premise = 1
draws_hypothesis = 1

# check if the number of games in the hypothesis contradicts the number of games in the premise
if games_hypothesis!= games_premise:
    label = "contradiction"
# check if the number of draws in the hypothesis contradicts the number of draws in the premise
elif draws_hypothesis!= draws_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
