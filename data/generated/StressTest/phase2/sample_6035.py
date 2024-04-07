# Premise: In the city of San Durango, 40 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, less than 40 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 40
pet_owners_hypothesis = 40

# the hypothesis refers to the number of pet owners mentioned in the premise
if pet_owners_hypothesis >= pet_owners_premise:
    # check if the estimate of 'pet_owners_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

