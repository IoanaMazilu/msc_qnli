level_less_than_4_premise = 4
level_1_college_graduates_hypothesis = 15

# the hypothesis refers to the level of college graduates mentioned in the premise
if level_less_than_4_premise!= level_1_college_graduates_hypothesis:
    # check if the level of college graduates in the hypothesis contradicts the level of college graduates mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
