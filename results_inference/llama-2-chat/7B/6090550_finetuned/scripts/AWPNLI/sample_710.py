balls_premise = 378
jugglers_hypothesis = 63.0
jugglers_premise = 1.0
balls_per_jugler_premise = 6

# the hypothesis refers to the number of jugglers needed, which can be computed from the premise
# compute the number of jugglers needed in the premise
jugglers_needed_premise = balls_premise / jugglers_per_ball_premise

if jugglers_needed_premise!= jugglers_hypothesis:
    # check if the number of jugglers needed in the hypothesis contradicts the number of jugglers needed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
