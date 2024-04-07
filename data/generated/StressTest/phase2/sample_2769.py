# Premise: After 40 minutes, Annie stops to fix a flat tire.
# Hypothesis: After less than 80 minutes, Annie stops to fix a flat tire.
# Golden Label: entailment

stop_time_premise = 40
stop_time_hypothesis = 80

# the hypothesis refers to the time when Annie stops to fix a flat tire, as mentioned in the premise
if stop_time_hypothesis < stop_time_premise:
    # check if the hypothesis time contradicts the stated stop time in the premise
    label = "contradiction"
elif stop_time_hypothesis > stop_time_premise:
    # the hypothesis gives a time limit that is greater than the time mentioned in the premise
    # therefore, the hypothesis does not contradict the premise but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis time and the premise time are equal, we can infer entailment
    label = "entailment"

print(label)

