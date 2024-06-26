offer_premise = 80
offer_hypothesis = 20

# the hypothesis talks about the offer for shirts, which is also mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the offer in the hypothesis contradicts the offer in the premise
    label = "contradiction"
else:
    # if the offer in the hypothesis is less than the premise, we can infer entailment
    label = "entailment"

print(label)
