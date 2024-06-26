english_marks_premise = 86
math_marks_premise = 89
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 81

english_marks_hypothesis = 16
math_marks_hypothesis = 89
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 81

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or math_marks_premise != math_marks_hypothesis or physics_marks_premise != physics_marks_hypothesis or chemistry_marks_premise != chemistry_marks_hypothesis or biology_marks_premise != biology_marks_hypothesis:
    # check if the hypothesis marks contradict the premise marks in any subject
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
