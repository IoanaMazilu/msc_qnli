# Premise: In the city of San Durango, 60 people own cats, dogs, or rabbits.
# Hypothesis: In the city of San Durango, 40 people own cats, dogs, or rabbits.
# Golden Label: contradiction

pets_owner_premise = 60
pets_owner_hypothesis = 40

# the hypothesis talks about the number of pet owners in the same city mentioned in the premise
if pets_owner_hypothesis > pets_owner_premise:
    # check if the number of pet owners in the hypothesis contradicts the number of pet owners reported in the premise
    label = "contradiction"
elif pets_owner_hypothesis < pets_owner_premise:
    # check if the number of pet owners in the hypothesis is less than the number of pet owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

