rank_premise = 75
rank_hypothesis = 15
class_size = 47

# the hypothesis talks about the rank of Nitin in a class, referenced also in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'rank_premise'
    label = "contradiction"
elif rank_hypothesis < class_size:
    # check if the rank in the hypothesis is less than the total class size
    label = "contradiction"
else:
    # the premise gives only an estimate for the rank of Nitin
    # any rank less than 'rank_premise' and less than 'class_size' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
