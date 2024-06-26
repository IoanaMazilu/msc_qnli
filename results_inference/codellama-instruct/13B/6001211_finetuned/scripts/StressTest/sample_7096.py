rank_premise = 75
rank_hypothesis = 15
class_size = 47

# the hypothesis refers to Nitin's rank in the class, which is also mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis rank contradicts the premise's estimate of less than 'rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank less than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
