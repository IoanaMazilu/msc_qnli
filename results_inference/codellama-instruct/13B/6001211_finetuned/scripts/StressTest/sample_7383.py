nitin_rank_premise = 24
nitin_rank_hypothesis = 74
class_size_premise = 58
class_size_hypothesis = 58

# the hypothesis refers to Nitin's rank and class size mentioned in the premise
if nitin_rank_premise > nitin_rank_hypothesis:
    # check if Nitin's rank in the premise contradicts the hypothesis that he ranks less than 74th
    label = "contradiction"
elif class_size_premise!= class_size_hypothesis:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
