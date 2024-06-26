business_value_premise = 14000
business_value_hypothesis = 24000

# the hypothesis talks about the value of a business jointly owned by the speaker and James and Greg
if business_value_hypothesis!= business_value_premise:
    # check if the value of the business in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
