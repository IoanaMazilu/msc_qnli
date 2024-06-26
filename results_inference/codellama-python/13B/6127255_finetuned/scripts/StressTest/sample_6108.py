level_one_graduates_premise = 15
level_one_graduates_hypothesis = 15

# the hypothesis refers to the percentage of Level-1 college graduates in Amtek's sales staff, mentioned in the premise
if level_one_graduates_hypothesis!= level_one_graduates_premise:
    # check if the percentage of Level-1 college graduates in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
