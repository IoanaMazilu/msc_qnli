# The hypothesis and premise have different mark ranges
# The hypothesis is entailed by the premise

average_marks_premise = 56 + 60 + 72 + 85 + 80
average_marks_hypothesis = 26 + 60 + 72 + 85 + 80

if average_marks_premise <= average_marks_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
