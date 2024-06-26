months_premise = 4
months_hypothesis = 3

# the hypothesis refers to the number of months before Rakesh left, mentioned in the premise
if months_premise > months_hypothesis:
    # check if the hypothesis value contradicts the number of months Rakesh stayed reported in the premise
    label = "contradiction"
elif months_hypothesis >= months_premise:
    # check if the hypothesis value contradicts the number of months Rakesh stayed reported in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
