# Premise: In fourth grade there were 42.0 students at the start of the year and During the year, 4.0 students left, and 10.0 students were transferred to fifth grade.
# Hypothesis: 28.0 students were in fourth grade at the end.
# Golden Label: entailment

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

