ranking_premise = 74
ranking_hypothesis = 24

# the hypothesis talks about the ranking of a student, referenced also in the premise
if ranking_hypothesis <= ranking_premise:
    # check if the hypothesis value contradicts the estimate of less than 'ranking_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ranking
    # any ranking greater than 'ranking_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
