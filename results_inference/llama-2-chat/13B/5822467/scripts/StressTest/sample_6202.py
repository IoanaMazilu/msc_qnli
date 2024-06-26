milestogo_premise = 300
milestogo_hypothesis = 200

# the hypothesis refers to the number of miles traveled on the first day of the vacation
if milestogo_premise > milestogo_hypothesis:
    # the hypothesis value is less than the premise value, so there is no contradiction
    label = "entailment"
elif milestogo_hypothesis > milestogo_premise:
    # the premise value is less than the hypothesis value, so there is a contradiction
    label = "contradiction"
else:
    # the premise and hypothesis values are equal, so there is no entailment or contradiction
    label = "neutral"

print(label)
