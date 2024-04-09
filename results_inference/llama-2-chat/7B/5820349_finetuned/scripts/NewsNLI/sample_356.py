gunshot_wounds_premise = 6
gunshot_wounds_hypothesis = 6

# the hypothesis mentions the number of gunshot entrance wounds sustained by Brown, which is also mentioned in the premise
if gunshot_wounds_hypothesis!= gunshot_wounds_premise:
    # check if the number of gunshot wounds in the hypothesis contradicts the number of gunshot wounds reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
