# define variables for the numerical entities in the premise and hypothesis
goals_premise = 4
goals_hypothesis = 4
hat_trick_premise = 1
hat_trick_hypothesis = 1

# check if the number of goals in the hypothesis contradicts the number of goals in the premise
if goals_hypothesis!= goals_premise:
    label = "contradiction"
# check if the number of hat-tricks in the hypothesis contradicts the number of hat-tricks in the premise
elif hat_trick_hypothesis!= hat_trick_premise:
    label = "contradiction"
# if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
else:
    label = "entailment"

print(label)
