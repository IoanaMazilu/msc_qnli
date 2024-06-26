severity = 1

# hypothesis and premise are talking about the same scenario
# the hypothesis refers to the weight gain of Leo, which is also mentioned in the premise

if_leo_gains_10_pounds_premise = 10
if_leo_gains_80_pounds_hypothesis = 80

weight_percentage_premise = 50
weight_percentage_hypothesis = 50

# the hypothesis refers to the same scenario and condition as the premise
# calculate the weight gain in the hypothesis
weight_gain_hypothesis = if_leo_gains_80_pounds_hypothesis - if_leo_gains_10_pounds_premise
if weight_gain_hypothesis!= weight_gain_premise:
    # check if the weight gain in the hypothesis contradicts the weight gain in the premise
    label = "contradiction"
else:
    # if the weight gain in the hypothesis does not contradict the weight gain in the premise, we can infer entailment
    label = "entailment"

print(label)
