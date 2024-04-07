# Premise: If Albert’s monthly earnings rise by 26 %, he would earn $693.
# Hypothesis: If Albert’s monthly earnings rise by 46 %, he would earn $693.
# Golden Label: contradiction

earnings_rise_premise = 26
earnings_rise_hypothesis = 46
earnings_after_rise = 693

# the hypothesis refers to Albert's earnings increase, as mentioned in the premise
if earnings_rise_premise != earnings_rise_hypothesis:
    # check if the percentage of earnings rise in the hypothesis contradicts the percentage of earnings rise in the premise
    label = "contradiction"
else:
    # if the percentage of earnings rise in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

