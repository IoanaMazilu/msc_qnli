nitin_rank_premise = 15
nitin_rank_hypothesis = 75
class_size = 47

# the hypothesis refers to Nitin's rank mentioned in the premise
if nitin_rank_premise >= nitin_rank_hypothesis:
    # check if Nitin's rank in the premise contradicts the hypothesis of ranking less than 75
    label = "contradiction"
else:
    # if Nitin's rank does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
