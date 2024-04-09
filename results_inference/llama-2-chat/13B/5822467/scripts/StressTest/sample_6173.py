tip_premise = 15
tip_hypothesis = 25
discounted_price_premise = 0
discounted_price_hypothesis = 0

# the premise mentions the tip paid over the original price and the discounted price
if tip_premise <= tip_hypothesis:
    # check if the estimate of 'tip_hypothesis' contradicts the tip paid in the premise
    label = "contradiction"
elif discounted_price_hypothesis!= discounted_price_premise:
    # check if the discounted price in the hypothesis contradicts the discounted price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
