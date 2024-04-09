students_premise = 302
students_hypothesis = 102

# the hypothesis talks about the number of students studying different topics at the faculty of Aerospace Engineering
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of more than'students_premise' studying at the faculty
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students studying different topics
    # any number of students greater than'students_premise' studying at the faculty is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
