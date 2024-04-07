# Premise: Susan weighs 15 pounds more than Anna does, and together they weigh a total of 145 pounds.
# Hypothesis: Susan weighs less than 85 pounds more than Anna does, and together they weigh a total of 145 pounds.
# Golden Label: entailment

susan_weight_over_anna_premise = 15
susan_weight_over_anna_hypothesis = 85
total_weight_premise = 145
total_weight_hypothesis = 145

# the hypothesis mentions the weights of Susan and Anna, which are also mentioned in the premise
if susan_weight_over_anna_premise >= susan_weight_over_anna_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif total_weight_hypothesis != total_weight_premise:
    # check if the total weight in the hypothesis contradicts the total weight reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

