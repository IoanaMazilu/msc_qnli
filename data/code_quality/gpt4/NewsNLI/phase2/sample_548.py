offer_premise = 130000000
offer_hypothesis = 130000000

# the hypothesis mentions the world record offer for a Manchester United player, which is also mentioned in the premise
if offer_hypothesis != offer_premise:
    # check if the offer amount in the hypothesis contradicts the offer amount reported in the premise
    label = "contradiction"
else:
    # if the offer amount in the hypothesis does not contradict the offer amount in the premise, we can infer entailment
    label = "entailment"

print(label)