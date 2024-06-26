offer_premise = 0.8
offer_hypothesis = 0.2
price_premise = 0
price_hypothesis = 0

# the hypothesis refers to the offer percentage and the price mentioned in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
