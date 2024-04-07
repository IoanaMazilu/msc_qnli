# Premise: Henry runs the second leg of the course in 7 seconds.
# Hypothesis: Henry runs the second leg of the course in more than 6 seconds.
# Golden Label: entailment

second_leg_time_premise = 7
second_leg_time_hypothesis = 6

# the hypothesis refers to the time Henry takes to run the second leg of the course, which is also mentioned in the premise
if second_leg_time_premise <= second_leg_time_hypothesis:
    # check if the 'second_leg_time_premise' contradicts the hypothesis that the time is more than 'second_leg_time_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)

