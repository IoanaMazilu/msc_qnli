terrorists_killed_premise = 5
terrorists_killed_hypothesis = 5
terrorists_captured_premise = 11
terrorists_captured_hypothesis = 11

# the hypothesis mentions the number of terrorists killed and captured by Kenyan forces, which is also mentioned in the premise
if terrorists_killed_hypothesis != terrorists_killed_premise:
    # check if the number of terrorists killed in the hypothesis contradicts the number killed as reported in the premise
    label = "contradiction"
elif terrorists_captured_hypothesis != terrorists_captured_premise:
    # check if the number of terrorists captured from the hypothesis contradicts the number captured in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
