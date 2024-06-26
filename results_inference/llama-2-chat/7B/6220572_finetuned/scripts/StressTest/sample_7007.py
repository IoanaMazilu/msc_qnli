gerbils_pets_premise = 96
gerbils_pets_hypothesis = 66

# the hypothesis refers to the number of pets consisting of gerbils and hamsters mentioned in the premise
if gerbils_pets_hypothesis == gerbils_pets_premise:
    # check if the number of pets in the hypothesis matches the number of pets reported in the premise
    label = "entailment"
elif gerbils_pets_hypothesis > gerbils_pets_premise:
    # check if the estimate of 'gerbils_pets_hypothesis' contradicts the number of pets in the premise
    label = "contradiction"
else:
    # any number of pets less than 'gerbils_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
