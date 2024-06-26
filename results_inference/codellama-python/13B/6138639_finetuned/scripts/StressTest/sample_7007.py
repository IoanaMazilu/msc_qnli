total_pets_premise = 96
total_pets_hypothesis = 66

# the hypothesis talks about the total number of pets Claire has, referenced also in the premise
if total_pets_hypothesis!= total_pets_premise:
    # check if the total number of pets in the hypothesis contradicts the total number of pets reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
