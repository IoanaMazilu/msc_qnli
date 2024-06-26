# the hypothesis refers to the age difference between John and Tom, referenced also in the premise
if 6 + 3 * 5 > 6 + 3 * 5:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
