butter_mixed_premise = 44
butter_mixed_hypothesis = 84

# the hypothesis refers to the amount of butter mixed, which is also mentioned in the premise
if butter_mixed_hypothesis <= butter_mixed_premise:
    # check if the hypothesis value contradicts the amount of butter mixed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
