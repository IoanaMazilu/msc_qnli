nitin_rank_premise = 24
nitin_rank_hypothesis = 74

# the hypothesis talks about Nitin's rank in a class of 58 students, referenced also in the premise
if nitin_rank_hypothesis < nitin_rank_premise:
    # check if the hypothesis value contradicts the estimate of Nitin's rank in the premise
    label = "contradiction"
elif nitin_rank_premise == 24:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank less than 74th is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
