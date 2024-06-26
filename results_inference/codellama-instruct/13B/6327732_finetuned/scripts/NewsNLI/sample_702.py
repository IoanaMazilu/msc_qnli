poll_premise = 0.69
poll_hypothesis = 0.12

# the hypothesis mentions a lower percentage of people with a positive view of the United States, which contradicts the premise
if poll_hypothesis > poll_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
