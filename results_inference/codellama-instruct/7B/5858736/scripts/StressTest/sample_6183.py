employees_veridux_premise = 218
employees_veridux_hypothesis = 818

if employees_veridux_hypothesis >= employees_veridux_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
