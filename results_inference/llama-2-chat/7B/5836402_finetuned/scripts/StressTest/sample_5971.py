course_leg_premise = 6
course_leg_hypothesis = 7

# the hypothesis refers to the time Henry takes to run the second leg of the course mentioned in the premise
if course_leg_hypothesis <= course_leg_premise:
    # check if the hypothesis value contradicts the estimate of more than 'course_leg_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time
    # any time greater than 'course_leg_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
