leave_time_premise = 30
leave_time_hypothesis = 30

# the hypothesis talks about the time difference between when Alice and Bob leave City A, referenced also in the premise
if leave_time_hypothesis != leave_time_premise:
    # check if the hypothesis time contradicts the exact leave time difference 'leave_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
