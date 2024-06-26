journalists_premise = 4
journalists_hypothesis = 3

# the hypothesis mentions the number of journalists being held, which is also mentioned in the premise
# we need to check if the number of journalists in the hypothesis contradicts the number of journalists in the premise
if journalists_hypothesis != journalists_premise:
    label = "contradiction"
else:
    # if the number of journalists in the hypothesis does not contradict the number of journalists in the premise, we cannot infer entailment nor contradiction
    label = "neutral"

print(label)
