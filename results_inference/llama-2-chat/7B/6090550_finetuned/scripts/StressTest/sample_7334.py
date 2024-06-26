samsung_premise = 75
samsung_hypothesis = 85
iphone_premise = 70
iphone_hypothesis = 70

# the hypothesis talks about the percentage of Samsung and iPhone users in ABC limited, which is also mentioned in the premise
if samsung_premise!= samsung_hypothesis:
    # check if the percentage of Samsung users in the hypothesis contradicts the percentage of Samsung users in the premise
    label = "contradiction"
elif iphone_premise!= iphone_hypothesis:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
