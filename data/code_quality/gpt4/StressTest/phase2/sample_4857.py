nitin_rank_premise = 18
class_size_premise = 49
nitin_rank_hypothesis = 48
class_size_hypothesis = 49

# The hypothesis refers to the Nitin's rank and the class size mentioned in the premise
if nitin_rank_hypothesis >= nitin_rank_premise or class_size_hypothesis != class_size_premise:
    # check if the estimate of nitin_rank_hypothesis contradicts Nitin's rank in the premise or the class size contradicts
    label = "contradiction"
elif nitin_rank_hypothesis < nitin_rank_premise:
    # check if Nitin's rank in the hypothesis can be explicitly entailed from the premise
    label = "entailment"
else:
    label = "neutral"

print(label)
