nitin_rank_premise = 24
nitin_rank_hypothesis = 74
students_in_class_premise = 58
students_in_class_hypothesis = 58

# the hypothesis refers to Nitin's rank and the class size mentioned in the premise
if nitin_rank_hypothesis > students_in_class_premise:
    # check if the rank given in the hypothesis contradicts the total number of students in the premise
    label = "contradiction"
elif students_in_class_hypothesis != students_in_class_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students in the premise
    label = "contradiction"
elif nitin_rank_hypothesis < nitin_rank_premise:
    # check if the rank given in the hypothesis contradicts Nitin's rank in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
