# Premise: Dacid obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 16, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

# Define the marks obtained by Dacid in the premise and hypothesis
marks_premise = [76, 65, 82, 67, 85]
marks_hypothesis = [16, 65, 82, 67, 85]

# Compare each mark from the premise and hypothesis
for mark_p, mark_h in zip(marks_premise, marks_hypothesis):
    if mark_p != mark_h:
        # If any mark from the hypothesis contradicts the corresponding mark from the premise
        label = "contradiction"
        break
else: 
    # If all marks from the hypothesis match the marks from the premise
    label = "entailment"

print(label)

