english_marks_premise = 86
math_marks_premise = 85
physics_marks_premise = 92
chemistry_marks_premise = 87
biology_marks_premise = 95

english_marks_hypothesis = 46
math_marks_hypothesis = 85
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 95

# the hypothesis refers to the marks Dacid obtained in each subject, which are also mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or \
   math_marks_premise != math_marks_hypothesis or \
   physics_marks_premise != physics_marks_hypothesis or \
   chemistry_marks_premise != chemistry_marks_hypothesis or \
   biology_marks_premise != biology_marks_hypothesis:
    # check if the marks mentioned in the hypothesis contradict the marks mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
