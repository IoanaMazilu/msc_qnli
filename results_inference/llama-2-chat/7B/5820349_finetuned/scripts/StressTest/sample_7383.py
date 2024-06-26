nitin_rank_premise = 24
nitin_rank_hypothesis = 74
class_size = 58

# the hypothesis refers to Nitin's rank mentioned in the premise
if nitin_rank_premise >= nitin_rank_hypothesis:
    # check if Nitin's rank in the premise contradicts the hypothesis
    label = "contradiction"
elif nitin_rank_premise < class_size:
    # check if Nitin's rank in the premise is less than the class size
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
