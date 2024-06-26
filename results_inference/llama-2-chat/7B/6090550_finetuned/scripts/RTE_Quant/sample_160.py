centrifuges_premise = 54000
centrifuges_hypothesis = 54000

# the hypothesis and premise mention the number of centrifuges required to produce enriched uranium
if centrifuges_hypothesis!= centrifuges_premise:
    # check if the number of centrifuges in the hypothesis contradicts the number of centrifuges in the premise
    label = "contradiction"
else:
    # if the number of centrifuges in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
