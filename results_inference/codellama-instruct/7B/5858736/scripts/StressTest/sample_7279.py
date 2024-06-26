employees_veridux_premise = 510
employees_veridux_hypothesis = 210

if employees_veridux_hypothesis >= employees_veridux_premise:
    label = "entailment"
else:
    label = "contradiction"

print(label)
