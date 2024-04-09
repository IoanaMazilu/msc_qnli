level_graduates_premise = 0.1
level_graduates_hypothesis = 0.7

# the hypothesis talks about the level of college graduates in Listco's sales staff, referenced also in the premise
if level_graduates_hypothesis >= level_graduates_premise:
    # check if the hypothesis value contradicts the estimate of less than 'level_graduates_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of level-1 college graduates in Listco's sales staff
    # any percentage greater than or equal to 'level_graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
