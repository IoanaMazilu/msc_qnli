level_graduates_premise = 15
level_graduates_hypothesis = 16

# the hypothesis refers to a higher percentage of college graduates in Amtek's sales staff than the premise
if level_graduates_hypothesis <= level_graduates_premise:
    # check if the estimate of 'level_graduates_hypothesis' contradicts the percentage of college graduates in the premise
    label = "contradiction"
else:
    # the premise provides only an estimate for the percentage of college graduates, and any higher percentage is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
