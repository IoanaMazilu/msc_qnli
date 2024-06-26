samsung_premise = 75
samsung_hypothesis = 25
iphone_premise = 70
iphone_hypothesis = 70

# the hypothesis refers to the percentage of Samsung and i phone users mentioned in the premise
if samsung_premise <= samsung_hypothesis:
    # check if the estimate of'samsung_hypothesis' contradicts the percentage of Samsung users in the premise
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the percentage of i phone users in the hypothesis contradicts the percentage of i phone users reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
