level_one_graduates_premise = 10
level_less_than_seven_graduates_hypothesis = 10

# the hypothesis refers to the percentage of Level-less than 7 college graduates in the sales staff, which is also mentioned in the premise
if level_less_than_seven_graduates_hypothesis!= level_one_graduates_premise:
    # check if the percentage of Level-less than 7 college graduates in the hypothesis contradicts the percentage of Level-1 college graduates in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
