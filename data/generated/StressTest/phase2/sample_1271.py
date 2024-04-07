# Premise: In the city of San Durango, 90 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pet_owners_premise = 90
pet_owners_hypothesis = 60

# the hypothesis talks about the number of pet owners in the city of San Durango, referenced also in the premise
if pet_owners_hypothesis > pet_owners_premise:
    # check if the number of pet owners in the hypothesis contradicts the number of pet owners reported in the premise
    label = "contradiction"
elif pet_owners_hypothesis < pet_owners_premise:
    # check if the number of pet owners in the hypothesis is less than the number of pet owners reported in the premise
    label = "entailment"
else:
    # if the number of pet owners in the hypothesis matches the number of pet owners reported in the premise, we can infer entailment
    label = "entailment"

print(label)

