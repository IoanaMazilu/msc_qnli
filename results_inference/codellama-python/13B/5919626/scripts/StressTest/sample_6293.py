students_class_premise = 20
students_class_hypothesis = 20

# the hypothesis refers to the number of students in the class
if students_class_hypothesis <= students_class_premise:
    # check if the hypothesis value contradicts the estimate of'students_class_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students greater than'students_class_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
