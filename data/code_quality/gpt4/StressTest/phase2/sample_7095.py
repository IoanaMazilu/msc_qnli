nitin_rank_premise = 15
nitin_rank_hypothesis = 75
class_size_premise = 47
class_size_hypothesis = 47

# the hypothesis refers to Nitin's rank and the class size mentioned in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if the rank of 'nitin_rank_hypothesis' contradicts the rank of Nitin in the premise
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
