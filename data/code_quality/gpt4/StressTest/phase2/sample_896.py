wheat_kg_premise = 30
wheat_kg_hypothesis = 30

# the hypothesis talks about the quantity of wheat purchased by Arun, referenced also in the premise
if wheat_kg_hypothesis >= wheat_kg_premise:
    # check if the hypothesis value contradicts the premise that Arun purchased exactly 'wheat_kg_premise' kg of wheat
    label = "contradiction"
else:
    # if the hypothesis value is less than 'wheat_kg_premise', it can be explicitly entailed from the premise
    label = "entailment"

print(label)
