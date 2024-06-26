nitin_rank_premise = 15
nitin_rank_hypothesis = 65
total_students = 47

# the hypothesis refers to Nitin's rank in the class, which is also mentioned in the premise
if nitin_rank_hypothesis!= nitin_rank_premise:
    # check if the rank in the hypothesis contradicts the rank mentioned in the premise
    label = "contradiction"
else:
    # if the rank in the hypothesis does not contradict the rank in the premise, we can infer entailment
    label = "entailment"

print(label)
