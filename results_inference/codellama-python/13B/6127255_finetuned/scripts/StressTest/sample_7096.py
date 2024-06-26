nitin_rank_premise = 75
nitin_rank_hypothesis = 15
class_size = 47

# the hypothesis talks about Nitin's rank in a class, referenced also in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'nitin_rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank less than 'nitin_rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
