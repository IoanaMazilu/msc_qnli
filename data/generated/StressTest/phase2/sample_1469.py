# Premise: Claire has a total of 86 pets consisting of gerbils and hamsters only.
# Hypothesis: Claire has a total of more than 86 pets consisting of gerbils and hamsters only.
# Golden Label: contradiction

total_pets_premise = 86
total_pets_hypothesis = 86

# the hypothesis refers to the total number of pets Claire has, which is also mentioned in the premise
if total_pets_hypothesis >= total_pets_premise:
    # check if the hypothesis value contradicts the exact number of 'total_pets_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

