earnings_rise_percentage_premise = 26
earnings_rise_percentage_hypothesis = 36
earnings_after_rise = 693

# the hypothesis refers to the same situation as the premise, with Albert's earnings rising and the final amount he would earn
if earnings_rise_percentage_hypothesis < earnings_rise_percentage_premise:
    # check if the percentage rise in the hypothesis contradicts the percentage rise in the premise
    label = "contradiction"
elif earnings_rise_percentage_hypothesis > earnings_rise_percentage_premise:
    # the premise gives a specific percentage for the earnings rise
    # a higher percentage rise in the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise, so it's neutral
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
