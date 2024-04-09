rank_premise = [4, 18, 8, 21]
rank_hypothesis = [4, 18, 8, 21]

# the hypothesis refers to the ranks of two individuals, referenced also in the premise
if any(i > j for i, j in zip(rank_hypothesis, rank_premise)):
    # check if any rank in the hypothesis exceeds the corresponding rank in the premise
    label = "contradiction"
else:
    # the ranks in the hypothesis do not contradict the ranks in the premise, so we can infer entailment
    label = "entailment"

print(label)
