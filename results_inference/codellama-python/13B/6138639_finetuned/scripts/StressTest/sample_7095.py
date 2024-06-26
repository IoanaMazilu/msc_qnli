nitin_rank_premise = 15
nitin_rank_hypothesis = 75
class_size = 47

# the hypothesis talks about Nitin's rank in a class, referenced also in the premise
if nitin_rank_premise >= nitin_rank_hypothesis:
    # check if the premise value contradicts the estimate of less than 'nitin_rank_hypothesis'
    label = "contradiction"
else:
    # the premise gives a specific rank for Nitin
    # any rank less than 'nitin_rank_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
