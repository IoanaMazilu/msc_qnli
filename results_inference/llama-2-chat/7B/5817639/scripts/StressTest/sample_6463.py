students_premise = 102
students_hypothesis = 302

# the hypothesis talks about the number of students studying different topics, as mentioned in the premise
if students_hypothesis <= students_premise:
    # check if the hypothesis value contradicts the estimate of more than'students_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of students, and any number of students greater than'students_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
