# List all the marks Nancy obtained in each subject according to the premise
marks_premise = [66, 75, 52, 68, 89]

# List all the marks Nancy obtained in each subject according to the hypothesis
marks_hypothesis = [86, 75, 52, 68, 89]

# Compare the marks in each subject according to the premise and hypothesis
for subject, marks_premise in enumerate(marks_premise):
    if marks_hypothesis[subject]!= marks_premise:
        label = "contradiction"
        break
else:
    label = "entailment"

print(label)
