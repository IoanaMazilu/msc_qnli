# Premise: Claire has a total of 96 pets consisting of gerbils and hamsters only.
# Hypothesis: Claire has a total of 66 pets consisting of gerbils and hamsters only.
# Golden Label: contradiction

total_pets_premise = 96
total_pets_hypothesis = 66

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if total_pets_premise != total_pets_hypothesis:
    # check if the total number of pets in the hypothesis contradicts the total number of pets reported in the premise
    label = "contradiction"
else:
    # if the total number of pets in the hypothesis is equal to the total number of pets in the premise, we can infer entailment
    label = "entailment"

print(label)

