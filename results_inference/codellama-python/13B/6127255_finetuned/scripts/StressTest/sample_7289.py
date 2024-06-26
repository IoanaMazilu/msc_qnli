business_income_premise = 14000
business_income_hypothesis = 24000

# the hypothesis refers to the business income mentioned in the premise
if business_income_hypothesis!= business_income_premise:
    # check if the business income in the hypothesis contradicts the business income reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
