employees_veridux_premise = 180
employees_veridux_hypothesis = 280

if employees_veridux_hypothesis >= employees_veridux_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
