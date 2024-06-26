students_start_premise = 10.0
students_left_premise = 4.0
new_students_premise = 42.0
students_end_hypothesis = 50.0

# the hypothesis refers to the number of students at the end of the year, which is related to the premise
# compute the total number of students at the end of the year in the premise
students_end_premise = students_start_premise - students_left_premise + new_students_premise
if students_end_hypothesis != students_end_premise:
    # check if the number of students at the end of the year in the hypothesis contradicts the calculated number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
