rank_premise = 75
rank_hypothesis = 15
class_size_premise = 47
class_size_hypothesis = 47

# the hypothesis refers to the rank of Nitin in a class, mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the rank in the hypothesis contradicts the rank in the premise
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
