nitin_rank_premise = 15
total_students_premise = 47
nitin_rank_hypothesis = 75
total_students_hypothesis = 47

# the hypothesis refers to Nitin's rank and the total number of students in the class, both mentioned in the premise
if nitin_rank_hypothesis <= nitin_rank_premise:
    # check if the hypothesis value contradicts Nitin's rank in the premise
    label = "contradiction"
elif total_students_hypothesis!= total_students_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
