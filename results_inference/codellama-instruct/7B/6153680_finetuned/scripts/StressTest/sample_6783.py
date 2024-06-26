x_premise = 40
x_hypothesis = 70

# the hypothesis refers to the number of hours James is paid per hour, which is also mentioned in the premise
if x_hypothesis <= x_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
