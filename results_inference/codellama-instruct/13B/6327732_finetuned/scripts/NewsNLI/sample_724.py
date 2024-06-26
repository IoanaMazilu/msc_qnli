# define variables for the numerical entities in the premise and hypothesis
wins_premise = 2
wins_hypothesis = 2
draws_premise = 2
draws_hypothesis = 2

# check if the number of wins and draws in the hypothesis contradicts the number of wins and draws in the premise
if wins_hypothesis!= wins_premise or draws_hypothesis!= draws_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
