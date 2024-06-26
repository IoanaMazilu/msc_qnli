english_marks_premise = 45
math_marks_premise = 35
physics_marks_premise = 52
chemistry_marks_premise = 47
biology_marks_premise = 55

english_marks_hypothesis = 35
math_marks_hypothesis = 35
physics_marks_hypothesis = 52
chemistry_marks_hypothesis = 47
biology_marks_hypothesis = 55

# hypothesis mentions that Dacid scored more than the marks mentioned in hypothesis in all subjects
if english_marks_premise <= english_marks_hypothesis or math_marks_premise <= math_marks_hypothesis or physics_marks_premise <= physics_marks_hypothesis or chemistry_marks_premise <= chemistry_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis:
    # check if Dacid's marks in the premise are less than or equal to the marks mentioned in the hypothesis. If yes, this is a contradiction
    label = "contradiction"
else:
    # if Dacid's marks in the premise are more than the marks mentioned in the hypothesis in all subjects, this is an entailment
    label = "entailment"

print(label)
