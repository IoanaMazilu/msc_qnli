employees_veridux_premise = 280
employees_veridux_hypothesis = 180

if employees_veridux_hypothesis >= employees_veridux_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
