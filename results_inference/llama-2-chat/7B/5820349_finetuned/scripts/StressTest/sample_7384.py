nitin_rank_premise = 74
nitin_rank_hypothesis = 24
class_size = 58

# the hypothesis talks about the rank of Nitin in the class, referenced also in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the hypothesis value contradicts the estimate of less than 'nitin_rank_premise'
    label = "contradiction"
elif nitin_rank_hypothesis < class_size:
    # the premise gives only an estimate for the rank of Nitin
    # any rank less than 'class_size' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
