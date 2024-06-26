business_value_premise = 14000
business_value_hypothesis = 24000

# the hypothesis talks about the value of a business which he jointly owns with two other persons (James and Greg), referenced also in the premise
if business_value_hypothesis!= business_value_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives the exact value of the business
    # the hypothesis value is the same as the premise value, so it can be explicitly entailed from the premise
    label = "entailment"

print(label)
