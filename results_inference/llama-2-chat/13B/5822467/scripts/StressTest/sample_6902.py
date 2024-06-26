offer_premise = 30
offer_hypothesis = 80
price_premise = Rs
price_hypothesis = Rs

# the hypothesis refers to the offer percentage and price mentioned in the premise
if offer_hypothesis > offer_premise:
    # check if the estimate of 'offer_hypothesis' contradicts the offer percentage in the premise
    label = "contradiction"
elif price_hypothesis!= price_premise:
    # check if the price mentioned in the hypothesis contradicts the price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
