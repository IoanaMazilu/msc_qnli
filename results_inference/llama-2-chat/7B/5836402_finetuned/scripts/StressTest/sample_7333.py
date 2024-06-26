samsung_premise = 0.70
iphone_premise = 0.70
samsung_hypothesis = 0.75
iphone_hypothesis = 0.70

# the hypothesis talks about the percentage of Samsung and iPhones users in ABC limited, referenced also in the premise
if samsung_hypothesis!= samsung_premise:
    # check if the percentage of Samsung users in the hypothesis contradicts the percentage of Samsung users reported in the premise
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the percentage of iPhones users in the hypothesis contradicts the percentage of iPhones users reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
