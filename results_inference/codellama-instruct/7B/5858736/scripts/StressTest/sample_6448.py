# the hypothesis refers to the age difference between John and Frank
if (8 - 5) * 2 <= 2 * (5 - 8):
    # check if the estimate of '(8 - 5) * 2' contradicts the age difference mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
