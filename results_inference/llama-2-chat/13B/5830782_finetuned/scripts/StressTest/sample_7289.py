business_value_premise = 14000
business_value_hypothesis = 24000

# the hypothesis refers to the value of the business mentioned in the premise
if business_value_hypothesis!= business_value_premise:
    # check if the business value in the hypothesis contradicts the business value reported in the premise
    label = "contradiction"
else:
    # if the business value in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
