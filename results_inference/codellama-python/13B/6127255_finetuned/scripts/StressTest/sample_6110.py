level_one_graduates_premise = 15
level_more_than_one_graduates_hypothesis = 15

# the hypothesis refers to the percentage of Level-more than 1 college graduates in the sales staff, which is not mentioned in the premise
if level_more_than_one_graduates_hypothesis == level_one_graduates_premise:
    # check if the percentage of Level-more than 1 college graduates in the hypothesis contradicts the percentage of Level-1 college graduates in the premise
    label = "contradiction"
else:
    # the premise gives the percentage of Level-1 college graduates, but the hypothesis is about more than Level-1 college graduates
    # the hypothesis percentage is not contradictory to the premise percentage, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
