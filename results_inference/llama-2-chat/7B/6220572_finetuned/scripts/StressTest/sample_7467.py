level_graduates_premise = 10
level_graduates_hypothesis = 7

# the hypothesis refers to the percentage of college graduates in sales staff, also mentioned in the premise
if level_graduates_premise >= level_graduates_hypothesis:
    # check if the estimate of 'level_graduates_hypothesis' contradicts the percentage of college graduates in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of college graduates
    # any percentage greater than 'level_graduates_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
