course_length_premise = 100
course_length_hypothesis = 300

# the hypothesis specifies the length of the course mentioned in the premise
if course_length_hypothesis <= course_length_premise:
    # check if the hypothesis value contradicts the estimate of more than 'course_length_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the course length
    # any course length greater than 'course_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
