level_graduates_premise = 15
level_graduates_hypothesis = 15

# the hypothesis refers to the percentage of sales staff with level-more than 1 college graduates, mentioned in the premise
if level_graduates_hypothesis <= level_graduates_premise:
    # check if the estimate of 'level_graduates_hypothesis' contradicts the percentage of level-1 college graduates in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of level-1 college graduates
    # any percentage greater than 'level_graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
