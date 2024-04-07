# Premise: less than 64000 in a business which he jointly owns with two other persons (James and Greg)
# Hypothesis: 14000 in a business which he jointly owns with two other persons (James and Greg)
# Golden Label: neutral

business_ownership_premise = 64000
business_ownership_hypothesis = 14000

# the hypothesis refers to the value of a business mentioned in the premise
if business_ownership_hypothesis >= business_ownership_premise:
    # check if the 'business_ownership_hypothesis' contradicts the premise's estimate of less than 'business_ownership_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise estimate, we can infer entailment
    label = "entailment"

print(label)

