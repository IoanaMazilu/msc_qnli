students_at_school = 390.0
classrooms_per_student = 30.0
total_classrooms = students_at_school / classrooms_per_student

# the hypothesis refers to the number of classrooms needed, which can be calculated from the premise
# the hypothesis value is 11.0
if total_classrooms >= 11.0:
    # check if the hypothesis value contradicts the total classrooms calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the total classrooms, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise
    label = "entailment"

print(label)
