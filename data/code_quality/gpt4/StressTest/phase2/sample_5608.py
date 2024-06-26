leave_after_premise = 208
leave_after_hypothesis = 108

# the hypothesis refers to the time difference between Hannah and Glen leaving City A
if leave_after_hypothesis >= leave_after_premise:
    # check if the hypothesis time contradicts the estimate of less than 'leave_after_premise'
    label = "contradiction"
elif leave_after_hypothesis < leave_after_premise:
    # if the hypothesis value doesn't contradict the premise one, but also isn't explicitly stated in the premise, we infer neutrality
    label = "neutral"

print(label)
