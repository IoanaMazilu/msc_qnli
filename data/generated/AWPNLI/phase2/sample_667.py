# Premise: In fourth grade there were 42.0 students at the start of the year and During the year, 4.0 students left, and 10.0 students were transferred to fifth grade.
# Hypothesis: 26.0 students were in fourth grade at the end.
# Golden Label: contradiction

start_students_premise = 42.0
left_students_premise = 4.0
transferred_students_premise = 10.0
end_students_hypothesis = 26.0

# the hypothesis refers to the number of students at the end, which is also mentioned in the premise
# compute the total number of students at the end in the premise
end_students_premise = start_students_premise - left_students_premise - transferred_students_premise
if end_students_hypothesis != end_students_premise:
    # check if the number of students at the end in the hypothesis contradicts the number from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

