below_cost_percentage_premise = 16
below_cost_percentage_hypothesis = 26

# the hypothesis talks about the percentage below cost price at which Vijay sells a cupboard, referenced also in the premise
if below_cost_percentage_hypothesis <= below_cost_percentage_premise:
    # check if the hypothesis value contradicts the percentage below cost price in the premise
    label = "contradiction"
elif below_cost_percentage_premise != below_cost_percentage_hypothesis:
    # if the hypothesis values and estimates do not contradict the premise ones, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
