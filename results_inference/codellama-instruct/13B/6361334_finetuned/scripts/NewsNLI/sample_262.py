napoli_premise = 6
napoli_hypothesis = 6
cagliari_premise = 3
cagliari_hypothesis = 3

# the hypothesis mentions the score of Napoli and Cagliari, which are also mentioned in the premise
if napoli_hypothesis!= napoli_premise:
    # check if the score of Napoli in the hypothesis contradicts the score reported in the premise
    label = "contradiction"
elif cagliari_hypothesis!= cagliari_premise:
    # check if the score of Cagliari from the hypothesis contradicts the score in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
