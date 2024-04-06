# Premise: In fourth grade there were 10.0 students at the start of the year and During the year, 4.0 students left, and 42.0 new students came to school.
# Hypothesis: 48.0 students were in fourth grade at the end.
# Golden Label: entailment

start_students_premise = 10.0
left_students_premise = 4.0
new_students_premise = 42.0
end_students_hypothesis = 48.0

# the hypothesis refers to the number of students at the end of the year, which can be estimated from the premise
# compute the total number of students in fourth grade at the end of the year in the premise
end_students_premise = start_students_premise - left_students_premise + new_students_premise

if end_students_hypothesis != end_students_premise:
    # check if the number of students in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

