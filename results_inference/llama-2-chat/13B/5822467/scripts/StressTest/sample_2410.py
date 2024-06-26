mile_course_premise = 100
mile_course_hypothesis = 300

# the hypothesis talks about the length of the course, referenced also in the premise
if mile_course_hypothesis <= mile_course_premise:
    # check if the hypothesis value contradicts the estimate of more than'mile_course_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the course
    # any length of the course greater than'mile_course_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
