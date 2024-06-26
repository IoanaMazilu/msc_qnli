course_leg_time_premise = 38
course_leg_time_hypothesis = 28

# the hypothesis refers to the time Dawson took to run the first leg of the course, which is also mentioned in the premise
if course_leg_time_hypothesis >= course_leg_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the hypothesis time is less than the premise time, so it is consistent with the premise
    label = "entailment"

print(label)
