start_students_premise = 10.0
left_students_premise = 4.0
new_students_premise = 42.0
end_students_hypothesis = 50.0

# the hypothesis refers to the number of students in fourth grade at the end, which can be computed from the premise
# compute the total number of students at the end of the year
total_students_end = start_students_premise + new_students_premise - left_students_premise

if end_students_hypothesis!= total_students_end:
    # check if the number of students in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
