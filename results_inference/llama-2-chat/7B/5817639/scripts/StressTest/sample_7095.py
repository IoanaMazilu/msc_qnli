rank_premise = 15
rank_hypothesis = 75

# the hypothesis talks about the ranking of a student, referenced also in the premise
if rank_hypothesis <= rank_premise:
    # check if the hypothesis value contradicts the estimate of the ranking in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the ranking
    # any ranking less than 'rank_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
