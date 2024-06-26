samsung_premise = 25
samsung_hypothesis = 75
iphone_premise = 70
iphone_hypothesis = 70

# the hypothesis talks about the percentage of Samsung and iPhone users in ABC limited, which is also mentioned in the premise
if samsung_hypothesis <= samsung_premise:
    # check if the percentage of Samsung users in the hypothesis contradicts the percentage of Samsung users in the premise
    label = "contradiction"
elif iphone_hypothesis!= iphone_premise:
    # check if the percentage of iPhone users in the hypothesis contradicts the percentage of iPhone users in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
