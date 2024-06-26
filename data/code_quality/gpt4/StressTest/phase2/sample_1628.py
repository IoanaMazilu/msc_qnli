nitin_rank_premise = 23
nitin_rank_hypothesis = 43
total_students = 60

# the hypothesis refers to Nitin's rank in class, which is also mentioned in the premise
if nitin_rank_hypothesis != nitin_rank_premise:
    # check if the rank in the hypothesis contradicts the rank reported in the premise
    label = "contradiction"
else:
    # if the hypothesis rank does not contradict the premise rank, we can infer entailment
    label = "entailment"

print(label)
