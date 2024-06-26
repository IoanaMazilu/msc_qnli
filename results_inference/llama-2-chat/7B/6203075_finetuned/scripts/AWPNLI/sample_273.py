start_students_premise = 10.0
left_students_premise = 4.0
new_students_premise = 42.0
end_students_hypothesis = 50.0

# the hypothesis refers to the number of students in fourth grade at the end, which can be calculated from the premise
# calculate the total number of students at the end of the year according to the premise
total_students_end_premise = start_students_premise + (left_students_premise / 100) + new_students_premise
if end_students_hypothesis!= total_students_end_premise:
    # check if the number of students in the hypothesis contradicts the number of students at the end according to the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
