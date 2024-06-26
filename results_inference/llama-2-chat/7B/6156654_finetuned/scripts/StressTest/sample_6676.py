# The hypothesis and premise both mention the marks obtained by Dacid in different subjects
marks_premise = [16, 95, 82, 87, 92]
marks_hypothesis = [96, 95, 82, 87, 92]

# The hypothesis and premise have the same marks for each subject, except for English
# where the hypothesis marks are higher than the premise marks
if marks_hypothesis[0]!= marks_premise[0]:
    # Check if the marks in English in the hypothesis contradict the marks in English in the premise
    label = "contradiction"
elif marks_hypothesis[1]!= marks_premise[1]:
    # Check if the marks in Mathematics in the hypothesis contradict the marks in Mathematics in the premise
    label = "contradiction"
elif marks_hypothesis[2]!= marks_premise[2]:
    # Check if the marks in Physics in the hypothesis contradict the marks in Physics in the premise
    label = "contradiction"
elif marks_hypothesis[3]!= marks_premise[3]:
    # Check if the marks in Chemistry in the hypothesis contradict the marks in Chemistry in the premise
    label = "contradiction"
elif marks_hypothesis[4]!= marks_premise[4]:
    # Check if the marks in Biology in the hypothesis contradict the marks in Biology in the premise
    label = "contradiction"
else:
    # If the marks in each subject in the hypothesis are the same as in the premise, we can infer entailment
    label = "entailment"

print(label)
