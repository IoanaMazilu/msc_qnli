employees_premise = 218
employees_hypothesis = 118

if employees_hypothesis <= employees_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
