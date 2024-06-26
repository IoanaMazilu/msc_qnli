initial_students_premise = 10.0
students_got_on_premise = 3.0
total_students_hypothesis = 17.0

# the hypothesis refers to the total number of students on the bus, which can be inferred from the premise
# compute the total number of students on the bus in the premise
total_students_premise = initial_students_premise + students_got_on_premise

if total_students_hypothesis != total_students_premise:
    # check if the total number of students in the hypothesis contradicts the total number of students from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
