wheat_kg_premise = 30
wheat_kg_hypothesis = 40

# the hypothesis refers to the number of kg of wheat purchased, mentioned in the premise
if wheat_kg_hypothesis >= wheat_kg_premise:
    # check if the estimate of 'wheat_kg_hypothesis' contradicts the number of kg of wheat purchased in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of kg of wheat purchased
    # any number of kg of wheat less than 'wheat_kg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
