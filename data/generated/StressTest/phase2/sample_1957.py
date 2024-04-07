# Premise: Claire has a total of more than 20 pets consisting of gerbils and hamsters only.
# Hypothesis: Claire has a total of 90 pets consisting of gerbils and hamsters only.
# Golden Label: neutral

total_pets_premise = 20
total_pets_hypothesis = 90

# the hypothesis refers to the total number of pets belonging to Claire, mentioned in the premise
if total_pets_hypothesis <= total_pets_premise:
    # check if the hypothesis value contradicts the estimate of more than 'total_pets_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the total number of pets
    # any total number of pets greater than 'total_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

