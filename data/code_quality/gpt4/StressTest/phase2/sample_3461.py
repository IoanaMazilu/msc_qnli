deviations_premise = 2
deviations_hypothesis = 2

# the hypothesis refers to the possible number of standard deviations of Jack's score from the mean, also mentioned in the premise
if deviations_hypothesis != deviations_premise:
    # check if the hypothesis value contradicts the number of standard deviations mentioned in the premise
    label = "contradiction"
else:
    # if they are the same, we can infer entailment
    label = "entailment"

print(label)
