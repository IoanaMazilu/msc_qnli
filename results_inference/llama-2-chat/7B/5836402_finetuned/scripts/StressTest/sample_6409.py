offer_premise = 80
offer_hypothesis = 20

# the hypothesis refers to the offer for every shirt mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the offer in the hypothesis contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
else:
    # if the offer in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
