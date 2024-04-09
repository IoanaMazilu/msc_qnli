wheat_purchased_premise = 30
wheat_purchased_hypothesis = 40
rate_premise = Rs

# the hypothesis talks about the amount of wheat purchased and the rate, both referenced in the premise
if wheat_purchased_hypothesis <= wheat_purchased_premise:
    # check if the hypothesis value contradicts the estimate of 'wheat_purchased_premise'
    label = "contradiction"
elif wheat_purchased_hypothesis > wheat_purchased_premise:
    # check if the hypothesis value entails the estimate of 'wheat_purchased_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the amount of wheat purchased
    # any amount of wheat less than 'wheat_purchased_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
