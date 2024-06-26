rank_premise = 48
rank_hypothesis = 18
class_size_premise = 49
class_size_hypothesis = 49

# the hypothesis refers to Nitin's rank in class, also mentioned in the premise
if rank_hypothesis >= rank_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'rank_premise'
    label = "contradiction"
elif class_size_hypothesis != class_size_premise:
    # check if the class size in the hypothesis contradicts the class size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
