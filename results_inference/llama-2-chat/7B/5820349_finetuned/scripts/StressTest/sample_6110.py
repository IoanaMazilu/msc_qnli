level_one_graduates_premise = 15
level_more_than_one_graduates_hypothesis = 15

# the hypothesis refers to the percentage of Level-more than 1 college graduates in Amtek's sales staff
if level_more_than_one_graduates_hypothesis!= level_one_graduates_premise:
    # check if the percentage of Level-more than 1 college graduates in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis percentage does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
