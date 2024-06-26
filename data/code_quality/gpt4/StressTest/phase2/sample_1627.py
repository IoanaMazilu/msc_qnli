rank_premise = 33
rank_hypothesis = 23
class_size = 60

# the hypothesis talks about Nitin's rank in the class, also referenced in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the premise of ranking less than 'rank_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Nitin's rank
    # any rank less than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
