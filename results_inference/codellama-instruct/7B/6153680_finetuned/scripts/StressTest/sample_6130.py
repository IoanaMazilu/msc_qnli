x_premise = 11
x_hypothesis = 21

# the hypothesis refers to the number of hours Harry is paid per hour, which is also mentioned in the premise
if x_hypothesis <= x_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
