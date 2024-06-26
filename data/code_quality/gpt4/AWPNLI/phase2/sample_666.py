students_start_premise = 42.0
students_left_premise = 4.0
students_transferred_premise = 10.0
students_end_hypothesis = 28.0

# the hypothesis refers to the number of students at the end of the year, which can be computed from the premise
# compute the total number of students in the premise at the end of the year
students_end_premise = students_start_premise - students_left_premise - students_transferred_premise
if students_end_hypothesis != students_end_premise:
    # check if the number of students at the end in the hypothesis contradicts the number of students at the end from the premise
    label = "contradiction"
else:
    # if the number of students at the end in the hypothesis does not contradict the number of students at the end from the premise, we can infer entailment
    label = "entailment"    

print(label)
