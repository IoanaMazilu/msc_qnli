# define variables for the number of executed men and the source of the information
executed_men_premise = 3
source_premise = "Human Rights Watch"

# extract the number of executed men from the hypothesis
executed_men_hypothesis = 3

# check if the number of executed men from the hypothesis contradicts the number of executed men in the premise
if executed_men_hypothesis!= executed_men_premise:
    label = "contradiction"
else:
    # if the number of executed men from the hypothesis does not contradict the number of executed men in the premise, we can infer entailment
    label = "entailment"

print(label)
