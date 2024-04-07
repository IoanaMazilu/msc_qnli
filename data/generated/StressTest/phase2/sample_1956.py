# Premise: Claire has a total of 90 pets consisting of gerbils and hamsters only.
# Hypothesis: Claire has a total of more than 20 pets consisting of gerbils and hamsters only.
# Golden Label: entailment

total_pets_premise = 90
total_pets_hypothesis = 20

# the hypothesis refers to the total number of pets mentioned in the premise
if total_pets_premise <= total_pets_hypothesis:
    # check if the estimate of 'total_pets_hypothesis' contradicts the number of pets in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

