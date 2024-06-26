course_premise = 38
course_hypothesis = 28

# the hypothesis talks about the time taken by Dawson in the first leg of the course
if course_hypothesis <= course_premise:
    # check if the hypothesis value contradicts the estimate of less than 'course_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the time taken by Dawson in the first leg of the course
    # any time taken by Dawson in the first leg that is greater than the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
