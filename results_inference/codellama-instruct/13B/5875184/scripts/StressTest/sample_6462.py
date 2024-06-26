faculty_students_premise = 302
faculty_students_hypothesis = 102

# the hypothesis refers to the number of students studying Random-processing methods at the faculty of Aerospace Engineering
if faculty_students_hypothesis <= faculty_students_premise:
    # check if the estimate of 'faculty_students_hypothesis' contradicts the number of students studying Random-processing methods in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying Random-processing methods
    # any number of students greater than 'faculty_students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
