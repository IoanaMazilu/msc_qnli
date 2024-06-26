weeks_premise = 3
weeks_hypothesis = 6

# the hypothesis refers to the number of weeks Rikki has gone to the gym, which is also mentioned in the premise
if weeks_premise >= weeks_hypothesis:
    # check if the number of weeks in the hypothesis contradicts the number of weeks in the premise
    label = "contradiction"
else:
    # if the number of weeks in the hypothesis is less than the number of weeks in the premise, we can infer entailment
    label = "entailment"

print(label)
