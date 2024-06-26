missing_personnel_premise = 18
missing_personnel_hypothesis = 18

# the premise and hypothesis refer to the same number of missing personnel, so there is no contradiction
if missing_personnel_hypothesis == missing_personnel_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
