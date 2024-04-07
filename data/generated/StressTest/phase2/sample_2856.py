# Premise: Nitin ranks 12 th in a class of 56 students.
# Hypothesis: Nitin ranks less than 82 th in a class of 56 students.
# Golden Label: entailment

nitin_rank_premise = 12
class_size_premise = 56
nitin_rank_hypothesis = 82

# the hypothesis refers to Nitin's ranking and class size mentioned in the premise
if nitin_rank_hypothesis <= nitin_rank_premise:
    # check if the estimate of 'nitin_rank_hypothesis' contradicts Nitin's rank in the premise
    label = "contradiction"
elif nitin_rank_hypothesis > class_size_premise:
    # check if 'nitin_rank_hypothesis' is greater than the total class size
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

