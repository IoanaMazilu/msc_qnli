centrifuges_premise = 54000
centrifuges_hypothesis = 54000

# the hypothesis and premise mention the number of centrifuges needed to produce enriched uranium
if centrifuges_premise!= centrifuges_hypothesis:
    # check if the number of centrifuges in the hypothesis contradicts the number of centrifuges in the premise
    label = "contradiction"
else:
    # if the hypothesis values and premise values are the same, we can infer entailment
    label = "entailment"

print(label)
