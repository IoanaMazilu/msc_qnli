total_pets_premise = 80
total_pets_hypothesis = 80

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if total_pets_hypothesis >= total_pets_premise:
    # check if the hypothesis value contradicts the premise of having less than 'total_pets_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of pets
    # any number less than 'total_pets_premise' contradicts the premise
    label = "contradiction"

print(label)
