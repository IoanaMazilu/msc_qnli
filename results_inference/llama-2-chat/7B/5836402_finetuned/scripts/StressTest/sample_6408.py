offer_premise = 20
offer_hypothesis = 80

# the hypothesis refers to the offer for shirts mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the estimate of 'offer_hypothesis' contradicts the offer in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
