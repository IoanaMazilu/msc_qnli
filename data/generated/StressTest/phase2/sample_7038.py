# Premise: Calculate the average marks of a student who obtained 56, 60, 72, 85 and 80 marks (out of 100) in Geography, History and Government, Art, Computer Science and Modern Literature?
# Hypothesis: Calculate the average marks of a student who obtained more than 26, 60, 72, 85 and 80 marks (out of 100) in Geography, History and Government, Art, Computer Science and Modern Literature?
# Golden Label: entailment

marks_premise = [56, 60, 72, 85, 80]
marks_hypothesis = 26

# the hypothesis refers to the marks obtained by a student in various subjects, mentioned in the premise
if marks_premise[0] <= marks_hypothesis:
    # check if the 'marks_hypothesis' contradicts the first mark in the list of marks in the premise
    label = "contradiction"
else:
    # if the 'marks_hypothesis' is less than the first mark in the list of marks in the premise, we can infer entailment
    label = "entailment"

print(label)

