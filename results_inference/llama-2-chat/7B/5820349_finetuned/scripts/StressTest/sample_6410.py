offer_premise = 20
offer_hypothesis = 80

# the hypothesis talks about the offer percentage for a shirt, referenced also in the premise
if offer_hypothesis!= offer_premise:
    # check if the offer percentage in the hypothesis contradicts the offer percentage in the premise
    label = "contradiction"
else:
    # if the offer percentages in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
