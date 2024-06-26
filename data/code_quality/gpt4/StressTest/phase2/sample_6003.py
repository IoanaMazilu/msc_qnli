balls_needed_premise = 4
balls_needed_hypothesis = 3
total_balls = 10

# the hypothesis refers to the number of balls John needs which is also mentioned in the premise
if balls_needed_premise <= balls_needed_hypothesis:
    # check if the hypothesis estimate contradicts the number of balls John needs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
