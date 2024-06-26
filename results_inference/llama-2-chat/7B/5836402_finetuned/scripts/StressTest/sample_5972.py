course_leg_time_premise = 7
course_leg_time_hypothesis = 6

# the hypothesis talks about the time Henry took to run the second leg of the course, referenced also in the premise
if course_leg_time_hypothesis!= course_leg_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
