course_length_premise = 800
course_length_hypothesis = 300

# the hypothesis refers to the length of a course in Wyoming, also mentioned in the premise
if course_length_hypothesis >= course_length_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'course_length_premise' miles
    label = "contradiction"
elif course_length_hypothesis < course_length_premise:
    # the premise gives only an estimate for the course length
    # a course length less than 'course_length_premise' is consistent with the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
