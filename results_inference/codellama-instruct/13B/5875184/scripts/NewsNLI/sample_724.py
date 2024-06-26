# define variables for the numerical entities in the premise and hypothesis
wins_premise = 2
wins_hypothesis = 2
draws_premise = 1
draws_hypothesis = 2

# check if the number of wins in the hypothesis contradicts the number of wins in the premise
if wins_hypothesis!= wins_premise:
    label = "contradiction"
elif draws_hypothesis!= draws_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
