length_premise = 10.7
length_hypothesis = 10.7

# the hypothesis mentions the length of the gondola, which is also mentioned in the premise
if length_hypothesis!= length_premise:
    # check if the length in the hypothesis contradicts the length reported in the premise
    label = "contradiction"
else:
    # if the hypothesis length does not contradict the premise length, we can infer entailment
    label = "entailment"

print(label)
