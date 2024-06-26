student_pop_premise = 4004
student_pop_hypothesis = 2004

# the hypothesis refers to the student population in a year mentioned in the premise
if student_pop_hypothesis > student_pop_premise:
    # check if the year of 'student_pop_hypothesis' contradicts the year of 'student_pop_premise'
    label = "contradiction"
elif student_pop_hypothesis < student_pop_premise:
    # check if the year of 'student_pop_hypothesis' contradicts the year of 'student_pop_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
