nitin_rank_premise = 74
nitin_rank_hypothesis = 24
class_size = 58

# the hypothesis refers to the rank of Nitin, which is also mentioned in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the rank in the hypothesis contradicts the premise
    label = "contradiction"
elif nitin_rank_hypothesis < nitin_rank_premise:
    # if the rank in the hypothesis is less than the rank in the premise, it is consistent with the premise
    label = "entailment"
else:
    # if the rank in the hypothesis is equal to the rank in the premise, it is neutral
    label = "neutral"

print(label)
