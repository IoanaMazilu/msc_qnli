poll_premise = 0.69
poll_hypothesis = 0.12

# the hypothesis mentions a lower percentage of people with a positive view of the United States
# compared to the premise, which suggests a contradiction
if poll_hypothesis < poll_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
