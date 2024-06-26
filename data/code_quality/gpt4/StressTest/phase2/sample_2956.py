students_premise = 20
students_hypothesis = 90

# The hypothesis talks about the number of students, also referenced in the premise
if students_hypothesis <= students_premise:
    # Check if the hypothesis value contradicts the estimate of more than 'students_premise'
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of students
    # Any number of students greater than 'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
