english_marks_premise = 86
english_marks_hypothesis = 86

mathematics_marks_premise = 85
mathematics_marks_hypothesis = 85

physics_marks_premise = 92
physics_marks_hypothesis = 92

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 95
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in the five subjects
if english_marks_premise <= english_marks_hypothesis or mathematics_marks_premise <= mathematics_marks_hypothesis or physics_marks_premise <= physics_marks_hypothesis or chemistry_marks_premise <= chemistry_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis:
    label = "contradiction"
else:
    label = "neutral"

print(label)
