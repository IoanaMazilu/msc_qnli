offer_premise = 20
offer_hypothesis = 80
shirt_price_premise = Rs.
shirt_price_hypothesis = Rs.

# the hypothesis refers to the offer percentage and the price of the shirt mentioned in the premise
if offer_hypothesis <= offer_premise:
    # check if the hypothesis value contradicts the offer percentage in the premise
    label = "contradiction"
elif shirt_price_hypothesis!= shirt_price_premise:
    # check if the price of the shirt in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
