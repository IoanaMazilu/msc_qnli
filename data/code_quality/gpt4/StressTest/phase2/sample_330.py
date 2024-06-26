efficiency_tanya_premise = 25
efficiency_tanya_hypothesis = 65

# the hypothesis refers to Tanya's efficiency compared to Sakshi's, which is also mentioned in the premise
if efficiency_tanya_hypothesis <= efficiency_tanya_premise:
    # check if the hypothesis value contradicts the efficiency percentage in the premise
    label = "contradiction"
elif efficiency_tanya_hypothesis > efficiency_tanya_premise:
    # the hypothesis gives a range for Tanya's efficiency percentage
    # any efficiency percentage less than 'efficiency_tanya_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
