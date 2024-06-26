business_value_premise = 14000
business_value_hypothesis = 64000

# the hypothesis talks about the value of a business, referenced also in the premise
if business_value_hypothesis <= business_value_premise:
    # check if the hypothesis value contradicts the estimate of 'business_value_premise'
    label = "contradiction"
elif business_value_hypothesis > business_value_premise:
    # the premise gives only an exact value for the business
    # any value of business greater than 'business_value_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
