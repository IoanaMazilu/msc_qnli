nitin_rank_premise = 27
nitin_rank_hypothesis = 27
total_students = 89

# the hypothesis refers to Nitin's rank mentioned in the premise
if nitin_rank_hypothesis >= nitin_rank_premise:
    # check if 'nitin_rank_hypothesis' contradicts the rank of Nitin in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
