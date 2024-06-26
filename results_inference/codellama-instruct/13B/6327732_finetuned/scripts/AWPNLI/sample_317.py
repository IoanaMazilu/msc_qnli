num_students_premise = 390.0
num_students_per_classroom_premise = 30.0
num_classrooms_hypothesis = 11.0

# the hypothesis refers to the number of classrooms, which are also mentioned in the premise
# compute the total number of students in the premise
total_num_students_premise = num_students_premise / num_students_per_classroom_premise
if total_num_students_premise!= num_classrooms_hypothesis:
    # check if the number of classrooms in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
