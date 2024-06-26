pets_owner_premise = 60
pets_owner_hypothesis = 40

# the hypothesis refers to the number of pet owners in the city of San Durango mentioned in the premise
if pets_owner_premise < pets_owner_hypothesis:
    # check if the number of 'pets_owner_hypothesis' contradicts the number of pet owners in the premise
    label = "contradiction"
elif pets_owner_hypothesis > pets_owner_premise:
    # check if the number of pet owners in the hypothesis contradicts the number of pet owners reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
