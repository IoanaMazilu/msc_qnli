# Premise: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 70 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 60
pet_owners_hypothesis = 70

# the hypothesis refers to the number of pet owners in the same city mentioned in the premise
if pet_owners_hypothesis != pet_owners_premise:
    # check if the number of pet owners in the hypothesis contradicts the number of pet owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

