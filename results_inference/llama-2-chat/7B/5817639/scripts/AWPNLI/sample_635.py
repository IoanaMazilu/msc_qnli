bus_count_premise = 8
student_count_premise = 45
bus_students_hypothesis = 3.1

# compare the number of buses in the hypothesis to the number of buses in the premise
if bus_count_hypothesis == bus_count_premise:
    # check if the number of students in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
elif student_count_hypothesis!= student_count_premise:
    # check if the number of students in the hypothesis contradicts the number of students in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
