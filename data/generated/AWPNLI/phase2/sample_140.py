# Premise: There were 10.0 students riding on the school bus and at the first stop, 3.0 students got off of the bus.
# Hypothesis: 7.0 students are left on the bus.
# Golden Label: entailment

initial_students_premise = 10.0
students_off_premise = 3.0
students_left_hypothesis = 7.0

# the hypothesis refers to the number of students left on the bus, which can be computed from the premise
# compute the number of students left on the bus in the premise
students_left_premise = initial_students_premise - students_off_premise
if students_left_hypothesis != students_left_premise:
    # check if the number of students left on the bus in the hypothesis contradicts the number of students left on the bus from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

