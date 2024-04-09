level_1_graduates_premise = 10
level_7_graduates_premise = 10
level_1_graduates_hypothesis = 10

# the hypothesis refers to the percentage of sales staff with level 1 college graduates
if level_1_graduates_hypothesis <= level_1_graduates_premise:
    # check if the hypothesis value contradicts the estimate of 'level_1_graduates_premise'
    label = "contradiction"
elif level_7_graduates_premise!= level_1_graduates_hypothesis:
    # check if the number of level 7 college graduates in the hypothesis contradicts the number of level 1 college graduates reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
