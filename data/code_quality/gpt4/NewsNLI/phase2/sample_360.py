foreign_aid_premise = 0.01
foreign_aid_hypothesis = 0.01

# the hypothesis mentions the proportion of the federal budget allocated to foreign aid, which is also mentioned in the premise
if foreign_aid_hypothesis != foreign_aid_premise:
    # check if the proportion in the hypothesis contradicts the proportion reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
