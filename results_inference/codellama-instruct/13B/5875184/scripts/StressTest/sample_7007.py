premise_pets = 96
hypothesis_pets = 66

# the hypothesis refers to the number of pets mentioned in the premise
if hypothesis_pets <= premise_pets:
    # check if the estimate of 'hypothesis_pets' contradicts the number of pets in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of pets
    # any number of pets greater than 'premise_pets' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
