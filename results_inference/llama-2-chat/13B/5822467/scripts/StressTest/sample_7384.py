nitin_rank_premise = 74
nitin_rank_hypothesis = 24
class_size_premise = 58

# the hypothesis talks about Nitin's rank, which is a numerical value, and the class size
if nitin_rank_hypothesis <= nitin_rank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'nitin_rank_premise'
    label = "contradiction"
elif nitin_rank_hypothesis > class_size_premise / 2:
    # check if the hypothesis value is greater than half of the class size, which is consistent with the premise
    label = "neutral"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank between 1 and 58 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
