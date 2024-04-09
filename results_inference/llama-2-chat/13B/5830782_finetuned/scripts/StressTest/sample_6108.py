level_one_graduates_premise = 15
level_less_than_four_graduates_hypothesis = 15

# the hypothesis refers to the percentage of Level-1 college graduates and Level-less than 4 college graduates in Amtek's sales staff
if level_one_graduates_premise!= level_less_than_four_graduates_hypothesis:
    # check if the percentage of Level-less than 4 college graduates in the hypothesis contradicts the percentage of Level-1 college graduates in the premise
    label = "contradiction"
else:
    # if the percentage of Level-less than 4 college graduates in the hypothesis does not contradict the percentage of Level-1 college graduates in the premise, we can infer entailment
    label = "entailment"

print(label)
