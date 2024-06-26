offer_rate_premise = 25
offer_rate_hypothesis = 25

# the hypothesis talks about the offer rate applied to a shirt, referenced also in the premise
if offer_rate_hypothesis >= offer_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'offer_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
