employees_veridux_premise = 250
employees_veridux_hypothesis = 850

if employees_veridux_hypothesis <= employees_veridux_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
