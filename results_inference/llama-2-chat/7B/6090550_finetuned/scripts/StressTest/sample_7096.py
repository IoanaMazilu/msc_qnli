nitin_rank_premise = 75
nitin_rank_hypothesis = 15
class_size = 47

# the hypothesis refers to Nitin's rank in a class, which is also mentioned in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the rank in the hypothesis contradicts the rank in the premise
    label = "contradiction"
else:
    # if the rank in the hypothesis is less than the rank in the premise, we can infer entailment
    label = "entailment"

print(label)
