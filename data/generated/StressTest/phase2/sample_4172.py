# Premise: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 80 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 60
pet_owners_hypothesis = 80

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pet_owners_hypothesis != pet_owners_premise:
    # check if the number of pet owners in the hypothesis contradicts the number of pet owners reported in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of pet owners
    # any number of pet owners equal to 'pet_owners_premise' matches the premise and can be entailed
    label = "entailment"

print(label)

