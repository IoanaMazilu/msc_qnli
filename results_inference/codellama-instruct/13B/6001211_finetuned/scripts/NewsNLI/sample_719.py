acquisition_price_premise = 1000000000
acquisition_price_hypothesis = 1000000000

# the hypothesis mentions the acquisition price for Instagram by Facebook, which is also mentioned in the premise
if acquisition_price_hypothesis!= acquisition_price_premise:
    # check if the acquisition price in the hypothesis contradicts the acquisition price reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
