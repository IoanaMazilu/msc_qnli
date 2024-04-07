# Premise: Dawson runs the first leg of the course in 38 seconds.
# Hypothesis: Dawson runs the first leg of the course in more than 28 seconds.
# Golden Label: entailment

first_leg_time_premise = 38
first_leg_time_hypothesis = 28

# the hypothesis refers to the time Dawson spent running the first leg of the course
if first_leg_time_premise <= first_leg_time_hypothesis:
    # check if the time Dawson spent running the first leg of the course in the premise contradicts the estimate in the hypothesis
    label = "contradiction"
else:
    # if the premise's time is greater than the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)

