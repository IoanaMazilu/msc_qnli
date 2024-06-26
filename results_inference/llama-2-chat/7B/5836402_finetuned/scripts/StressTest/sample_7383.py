rank_premise = 24
rank_hypothesis = 74
class_size_premise = 58
class_size_hypothesis = 58

# the hypothesis refers to the rank of Nitin in a class, which is also mentioned in the premise
if rank_premise >= rank_hypothesis:
    # check if the rank of Nitin in the premise contradicts the estimate of less than 'rank_hypothesis'
    label = "contradiction"
elif class_size_hypothesis!= class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
