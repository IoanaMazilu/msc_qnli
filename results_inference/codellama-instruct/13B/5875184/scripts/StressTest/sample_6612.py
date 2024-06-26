faculty_students_premise = 312
faculty_students_hypothesis = 112

# the hypothesis refers to the number of students studying Random-processing methods
if faculty_students_hypothesis <= faculty_students_premise:
    # check if the hypothesis value contradicts the estimate of more than 'faculty_students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying Random-processing methods
    # any number of students greater than 'faculty_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
