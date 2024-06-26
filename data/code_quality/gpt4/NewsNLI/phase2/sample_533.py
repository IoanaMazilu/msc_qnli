eluded_capture_premise = 3
eluded_capture_hypothesis = 3

# the hypothesis mentions the number of times Torrealba has eluded capture, which is also mentioned in the premise
if eluded_capture_hypothesis != eluded_capture_premise:
    # check if the number of times he eluded capture in the hypothesis contradicts the number of times reported in the premise
    label = "contradiction"
else:
    # if the number from the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
