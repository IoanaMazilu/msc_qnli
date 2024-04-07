# Premise: Claire has a total of 90 pets consisting of gerbils and hamsters only.
# Hypothesis: Claire has a total of 60 pets consisting of gerbils and hamsters only.
# Golden Label: contradiction

pets_premise = 90
pets_hypothesis = 60

# the hypothesis refers to the total number of pets (gerbils and hamsters) that Claire has, as mentioned in the premise
if pets_hypothesis != pets_premise:
    # check if the total number of pets in the hypothesis contradicts the total number of pets reported in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

