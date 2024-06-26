nitin_rank_premise = 18
class_size_premise = 49
nitin_rank_hypothesis = 68
class_size_hypothesis = 49

# the hypothesis refers to Nitin's rank and class size mentioned in the premise
if nitin_rank_hypothesis != nitin_rank_premise:
    # check if Nitin's rank in the hypothesis contradicts his rank reported in the premise
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
