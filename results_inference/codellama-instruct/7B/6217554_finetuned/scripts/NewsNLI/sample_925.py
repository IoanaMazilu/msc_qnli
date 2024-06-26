cartograms_premise = 366
cartograms_hypothesis = 366

# the hypothesis mentions the number of cartograms, which is also referenced in the premise
if cartograms_hypothesis!= cartograms_premise:
    # check if the number of cartograms in the hypothesis contradicts the number of cartograms in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
