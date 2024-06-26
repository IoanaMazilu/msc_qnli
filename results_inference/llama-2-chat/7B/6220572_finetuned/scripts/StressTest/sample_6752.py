people_own_pets_premise = 50
people_own_pets_hypothesis = 50

# the hypothesis refers to the number of pet owners in the premise
if people_own_pets_hypothesis <= people_own_pets_premise:
    # check if the hypothesis value contradicts the number of pet owners in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pet owners
    # any number of pet owners greater than 'people_own_pets_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
