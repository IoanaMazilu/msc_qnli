offer_premise = 80
offer_hypothesis = 20

# the hypothesis talks about the offer percentage for every shirt, which is also mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the offer percentage in the hypothesis contradicts the offer percentage in the premise
    label = "contradiction"
else:
    # if the offer percentage in the hypothesis does not contradict the offer percentage in the premise, we can infer entailment
    label = "entailment"

print(label)
