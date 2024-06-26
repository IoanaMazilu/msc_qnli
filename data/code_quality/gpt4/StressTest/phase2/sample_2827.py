course_length_premise = 400
course_length_hypothesis = 300

# the hypothesis mentions the length of a course mentioned also in the premise
if course_length_hypothesis >= course_length_premise:
    # check if the hypothesis length contradicts the estimate of less than 'course_length_premise'
    label = "contradiction"
elif course_length_hypothesis < course_length_premise:
    # the premise gives only an estimate for the course length
    # a course length less than 'course_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
