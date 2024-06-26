two_weeks_premise = 2
two_weeks_hypothesis = 2

# check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
if two_weeks_hypothesis!= two_weeks_premise:
    label = "contradiction"
else:
    # if the number of weeks in the hypothesis is the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
