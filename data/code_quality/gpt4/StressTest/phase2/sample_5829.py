wheat_kg_premise = 30
wheat_kg_hypothesis = 80

# the hypothesis refers to the quantity of wheat purchased by Arun, also mentioned in the premise
if wheat_kg_hypothesis <= wheat_kg_premise:
    # check if the hypothesis value contradicts the quantity of wheat purchased by Arun in the premise
    label = "contradiction"
elif wheat_kg_premise >= wheat_kg_hypothesis:
    # check if the quantity of wheat purchased by Arun in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # the premise gives a precise amount of wheat purchased by Arun
    # any amount of wheat less than 'wheat_kg_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
