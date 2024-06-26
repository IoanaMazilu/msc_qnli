business_value_premise = 14000
business_value_hypothesis = 24000

# the hypothesis refers to the value of the business mentioned in the premise
if business_value_hypothesis!= business_value_premise:
    # check if the value of the business in the hypothesis contradicts the value of the business reported in the premise
    label = "contradiction"
elif business_value_hypothesis > business_value_premise:
    # check if the value of the business in the hypothesis is greater than the value reported in the premise
    label = "entailment"
else:
    # if the hypothesis value does not contradict the premise value, but is less than the premise value, we can infer neutrality
    label = "neutral"

print(label)
