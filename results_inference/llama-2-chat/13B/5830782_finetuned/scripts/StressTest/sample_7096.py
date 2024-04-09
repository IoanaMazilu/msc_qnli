rank_premise = 75
rank_hypothesis = 15
class_size = 47

# the hypothesis talks about Nitin's rank in class, which is also mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis rank contradicts the premise's statement of Nitin ranking less than 75 th
    label = "contradiction"
elif rank_hypothesis < rank_premise:
    # the premise gives an estimate for Nitin's rank
    # any rank less than 'rank_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
