# Premise: Nitin ranks 27 th in a class of 89 students.
# Hypothesis: Nitin ranks less than 77 th in a class of 89 students.
# Golden Label: entailment

nitin_rank_premise = 27
nitin_rank_hypothesis = 77
total_students = 89

# the hypothesis refers to Nitin's rank mentioned in the premise
if nitin_rank_hypothesis <= nitin_rank_premise:
    # check if the estimate of 'nitin_rank_hypothesis' contradicts Nitin's rank in the premise
    label = "contradiction"
elif nitin_rank_hypothesis > total_students:
    # check if the rank in the hypothesis contradicts the total number of students 
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

