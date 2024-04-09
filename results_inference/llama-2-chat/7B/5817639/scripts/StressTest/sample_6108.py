level_graduates_premise = 0.15
level_graduates_hypothesis = 0.15

# the hypothesis talks about the percentage of sales staff in Amtek, referenced also in the premise
if level_graduates_hypothesis <= level_graduates_premise:
    # check if the hypothesis value contradicts the estimate of more than 'level_graduates_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of sales staff,
    # any percentage greater than 'level_graduates_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
