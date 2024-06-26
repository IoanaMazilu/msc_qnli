offer_premise = 80
offer_hypothesis = 20
shirt_price_premise = 0
shirt_price_hypothesis = 0

# the hypothesis talks about the offer for shirts, which is also mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the offer in the hypothesis contradicts the offer in the premise
    label = "contradiction"
elif shirt_price_hypothesis!= shirt_price_premise:
    # check if the price of the shirt in the hypothesis contradicts the price in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
