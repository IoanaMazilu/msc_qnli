# Premise: 205 total Tajima's are currently owned by the dealership.
# Hypothesis: less than 205 total Tajima's are currently owned by the dealership.
# Golden Label: contradiction

tajimas_owned_premise = 205
tajimas_owned_hypothesis = 205

# the hypothesis refers to the total number of Tajima's cars owned by the dealership mentioned in the premise
if tajimas_owned_hypothesis >= tajimas_owned_premise:
    # check if the hypothesis value contradicts the premise statement of 'less than 205 Tajima's'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

