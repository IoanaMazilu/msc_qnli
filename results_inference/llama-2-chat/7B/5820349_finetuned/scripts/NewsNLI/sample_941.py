missing_personnel_premise = 18
missing_personnel_hypothesis = 18

# the hypothesis mentions the number of missing personnel, which is also referenced in the premise
# however, the hypothesis refers to the possibility of not being able to recover all of them, which contradicts the premise's assertion that they have been contacted
if missing_personnel_hypothesis!= missing_personnel_premise:
    label = "contradiction"
else:
    label = "contradiction"

print(label)
