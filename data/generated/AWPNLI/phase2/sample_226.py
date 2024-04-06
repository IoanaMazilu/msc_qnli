# Premise: 6.0 students were sitting at each table in the lunchroom and there are 34.0 tables.
# Hypothesis: 204.0 students were sitting in the lunchroom.
# Golden Label: entailment

students_per_table_premise = 6.0
tables_premise = 34.0
total_students_hypothesis = 204.0

# the hypothesis refers to the total number of students, which can be calculated from the premise
# compute the total number of students in the premise
total_students_premise = students_per_table_premise * tables_premise
if total_students_hypothesis != total_students_premise:
    # check if the number of students in the hypothesis contradicts the number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

