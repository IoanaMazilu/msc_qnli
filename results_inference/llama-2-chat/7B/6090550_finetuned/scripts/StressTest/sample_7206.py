# defining the premise and hypothesis
premise_marks = 99
hypothesis_marks = 45

# calculating the average marks in the premise and hypothesis
average_marks_premise = (premise_marks * 100) / 1
average_marks_hypothesis = (hypothesis_marks * 100) / 1

# checking if the hypothesis contradicts the premise
if average_marks_premise <= average_marks_hypothesis:
    label = "entailment"
else:
    label = "contradiction"

print(label)
