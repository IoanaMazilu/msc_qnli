# Premise: Thomas worked in the factory @ 4550/- per week. Owner told him to give the amount after one month.
# Hypothesis: Thomas worked in the factory @ 8550/- per week. Owner told him to give the amount after one month.
# Golden Label: contradiction

weekly_pay_premise = 4550
weekly_pay_hypothesis = 8550

# the hypothesis refers to the weekly pay of Thomas mentioned in the premise
if weekly_pay_hypothesis != weekly_pay_premise:
    # check if the weekly pay in the hypothesis contradicts the weekly pay reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

