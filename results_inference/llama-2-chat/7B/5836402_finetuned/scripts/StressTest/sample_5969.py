course_leg_premise = 38
course_leg_hypothesis = 68

# the hypothesis talks about the time Dawson took to run the first leg of the course, referenced also in the premise
if course_leg_hypothesis!= course_leg_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
