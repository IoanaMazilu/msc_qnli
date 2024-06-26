offer_premise = 80
offer_hypothesis = 20

# the hypothesis talks about the discount offered in the shop, which is also referenced in the premise
if offer_hypothesis >= offer_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_premise'
    label = "contradiction"
elif offer_hypothesis < offer_premise:
    # if the discount offered in the hypothesis is less than the discount offered in the premise, 
    # it's consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
