# Premise: If Arun doubles his speed, then he would take 1 hour less than Anil.
# Hypothesis: If Arun doubles his speed, then he would take less than 6 hour less than Anil.
# Golden Label: entailment

time_difference_premise = 1
time_difference_hypothesis = 6

# the hypothesis refers to the time difference mentioned in the premise
if time_difference_hypothesis < time_difference_premise:
    # check if the estimate of 'time_difference_hypothesis' contradicts the time difference in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

