# Premise: 6.0 students were sitting at each table in the lunchroom and there are 34.0 tables.
# Hypothesis: 202.0 students were sitting in the lunchroom.
# Golden Label: contradiction

students_per_table_premise = 6.0
tables_premise = 34.0
total_students_hypothesis = 202.0

# the hypothesis refers to the total number of students in the lunchroom, which can be inferred from the premise
# compute the total number of students in the premise
total_students_premise = students_per_table_premise * tables_premise
if total_students_hypothesis != total_students_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

