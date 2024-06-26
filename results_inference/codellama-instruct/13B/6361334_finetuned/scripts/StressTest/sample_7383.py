rank_premise = 24
rank_hypothesis = 74
class_size_premise = 58
class_size_hypothesis = 58

# the hypothesis refers to the rank of Nitin in a class of 58 students, mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the estimate of 'rank_hypothesis' contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
