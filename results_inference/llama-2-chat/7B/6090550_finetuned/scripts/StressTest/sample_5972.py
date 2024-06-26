course_leg_time_premise = 7
course_leg_time_hypothesis = 6

# the hypothesis refers to the time Henry runs the second leg of the course, mentioned in the premise
if course_leg_time_hypothesis!= course_leg_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
