students_premise = 90
students_hypothesis = 50

# the hypothesis talks about a percentage of boys at a school, referenced also in the premise
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of more than'students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students
    # any number of students greater than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
