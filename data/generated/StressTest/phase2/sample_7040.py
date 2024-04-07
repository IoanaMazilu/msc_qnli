# Premise: Calculate the average marks of a student who obtained 56, 60, 72, 85 and 80 marks (out of 100) in Geography, History and Government, Art, Computer Science and Modern Literature?
# Hypothesis: Calculate the average marks of a student who obtained less than 56, 60, 72, 85 and 80 marks (out of 100) in Geography, History and Government, Art, Computer Science and Modern Literature?
# Golden Label: contradiction

marks_premise = [56, 60, 72, 85, 80]
marks_hypothesis = [56, 60, 72, 85, 80]

average_marks_premise = sum(marks_premise) / len(marks_premise)

# the hypothesis refers to the average marks mentioned in the premise
# and suggests that the actual average might be less than the calculated 'average_marks_premise'
# but the premise itself gives the information needed to calculate the exact average,
# so the statement suggesting a lower average is a contradiction
if average_marks_premise < min(marks_hypothesis):
    label = "contradiction"
else:
    label = "entailment"

print(label)
