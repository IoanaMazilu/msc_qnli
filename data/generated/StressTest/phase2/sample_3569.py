# Premise: In the city of San Durango, 80 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, less than 80 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 80
pet_owners_hypothesis = 80

# the hypothesis refers to the number of pet owners in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the hypothesis value contradicts the exact number of pet owners in the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, it is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)

