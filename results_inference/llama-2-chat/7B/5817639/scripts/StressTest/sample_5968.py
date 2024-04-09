course_time_premise = 28
course_time_hypothesis = 38

# the hypothesis talks about the time taken by Dawson in the first leg of the course, referenced in the premise
if course_time_hypothesis >= course_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'course_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Dawson in the first leg of the course
    # any time greater than or equal to 'course_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
