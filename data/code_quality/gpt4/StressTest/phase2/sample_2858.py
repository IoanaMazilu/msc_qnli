nitin_rank_premise = 12
nitin_rank_hypothesis = 12
total_students_premise = 56
total_students_hypothesis = 56

# the hypothesis refers to Nitin's rank and the total number of students in the class mentioned in the premise
if nitin_rank_hypothesis != nitin_rank_premise:
    # check if the rank of Nitin in the hypothesis contradicts the rank of Nitin reported in the premise
    label = "contradiction"
elif total_students_hypothesis != total_students_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
