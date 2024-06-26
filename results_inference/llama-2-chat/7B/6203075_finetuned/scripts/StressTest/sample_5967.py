course_leg_premise = 38
course_leg_hypothesis = 28

# the hypothesis refers to the time Dawson takes to run the first leg of the course
if course_leg_premise <= course_leg_hypothesis:
    # check if the time in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the time in the premise is greater than the hypothesis, we can infer entailment
    label = "entailment"

print(label)
