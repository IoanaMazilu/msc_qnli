# Premise: In the city of San Durango, 90 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, more than 90 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 90
pet_owners_hypothesis = 90

# the hypothesis refers to the number of pet owners in San Durango mentioned in the premise
if pet_owners_hypothesis != pet_owners_premise:
    # check if the specific number of pet owners in the hypothesis contradicts the specific number of pet owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

