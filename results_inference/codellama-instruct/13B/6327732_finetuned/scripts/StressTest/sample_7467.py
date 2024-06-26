level_premise = 10
level_hypothesis = 7

# the hypothesis talks about the level of education required for the sales staff, referenced also in the premise
if level_hypothesis >= level_premise:
    # check if the hypothesis value contradicts the estimate of 'level_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the level of education required for the sales staff
    # any level of education less than 'level_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
