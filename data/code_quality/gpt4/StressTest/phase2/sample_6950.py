ratio_premise = 5 / 4
ratio_hypothesis = 5 / 4

# the hypothesis refers to the age ratio of Arun and Deepak mentioned in the premise
if ratio_hypothesis >= ratio_premise:
    # check if the 'ratio_hypothesis' contradicts the age ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
