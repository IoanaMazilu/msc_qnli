percentage_premise = 0.69
percentage_hypothesis = 0.12

# the hypothesis mentions a lower percentage of people having a positive view of the United States, which contradicts the premise
if percentage_hypothesis > percentage_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
