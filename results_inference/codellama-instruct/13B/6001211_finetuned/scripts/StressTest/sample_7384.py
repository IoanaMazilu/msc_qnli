rank_premise = 74
rank_hypothesis = 24
class_size = 58

# the hypothesis talks about Nitin's rank in the class, referenced also in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis rank contradicts the estimate of less than 'rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank less than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
