reading_rate_premise = 2
reading_rate_hypothesis = 3

# the hypothesis refers to the reading rate of Jos é mentioned in the premise
if reading_rate_hypothesis <= reading_rate_premise:
    # check if the reading rate in the hypothesis contradicts the reading rate in the premise
    label = "contradiction"
else:
    # if the reading rate in the hypothesis does not contradict the reading rate in the premise, we can infer entailment
    label = "entailment"

print(label)
