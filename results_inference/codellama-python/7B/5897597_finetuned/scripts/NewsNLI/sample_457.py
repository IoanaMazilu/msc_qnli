arrested_premise = 6
arrested_hypothesis = 6

# the hypothesis mentions the number of people arrested, which is also mentioned in the premise
if arrested_hypothesis!= arrested_premise:
    # check if the number of people arrested in the hypothesis contradicts the number of people arrested in the premise
    label = "contradiction"
else:
    # if the number of people arrested in the hypothesis does not contradict the number of people arrested in the premise, we can infer entailment
    label = "entailment"

print(label)
