nitin_rank_premise = 24
total_students_premise = 58
nitin_rank_hypothesis = 74

# the hypothesis refers to Nitin's rank, which is also mentioned in the premise
if nitin_rank_premise >= nitin_rank_hypothesis:
    # check if the premise rank contradicts the hypothesis rank
    label = "contradiction"
elif nitin_rank_premise < nitin_rank_hypothesis:
    # if the premise rank is less than the hypothesis rank, it is consistent with the hypothesis
    # but it cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the premise rank is equal to the hypothesis rank, it is consistent with the hypothesis
    # and can be explicitly entailed from the hypothesis
    label = "entailment"

print(label)
