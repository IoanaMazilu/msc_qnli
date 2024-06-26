 class_rank_premise = 24
class_rank_hypothesis = 74

# the hypothesis refers to the rank of Nitin in a class, mentioned in the premise
if class_rank_premise >= class_rank_hypothesis:
    # check if the rank in the hypothesis contradicts the rank in the premise
    label = "contradiction"
else:
    # if the rank in the hypothesis is less than the rank in the premise, we can infer entailment
    label = "entailment"

print(label)
