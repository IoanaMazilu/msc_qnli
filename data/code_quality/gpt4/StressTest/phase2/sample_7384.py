nitin_rank_premise = 74
nitin_rank_hypothesis = 24
class_size = 58

# the hypothesis is about Nitin's rank, which is also referenced in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'nitin_rank_premise'
    label = "contradiction"
elif nitin_rank_hypothesis > class_size:
    # check if Nitin's rank in the hypothesis is possible in a class of 'class_size'
    label = "contradiction"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank less than 'nitin_rank_premise' and within 'class_size' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
