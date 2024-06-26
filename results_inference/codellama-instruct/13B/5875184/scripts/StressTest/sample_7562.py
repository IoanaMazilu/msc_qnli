faculty_students_premise = 310 + 232 + 112
faculty_students_hypothesis = 810 + 232 + 112

# the hypothesis refers to the total number of students studying at the faculty of Aerospace Engineering
if faculty_students_hypothesis <= faculty_students_premise:
    # check if the hypothesis value contradicts the estimate of more than 'faculty_students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying at the faculty of Aerospace Engineering
    # any number of students greater than 'faculty_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
