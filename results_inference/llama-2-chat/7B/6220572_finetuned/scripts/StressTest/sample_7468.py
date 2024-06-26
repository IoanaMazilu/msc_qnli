level_less_than_7_premise = 7
level_1_graduates_hypothesis = 7

# the hypothesis talks about the level of college graduates in the sales staff, referenced also in the premise
if level_less_than_7_premise == level_1_graduates_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'level_less_than_7_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the level of college graduates
    # any level of college graduates consistent with 'level_less_than_7_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
