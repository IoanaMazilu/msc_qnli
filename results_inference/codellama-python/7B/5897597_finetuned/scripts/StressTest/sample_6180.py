english_marks_premise = 86
math_marks_premise = 85
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 85

english_marks_hypothesis = 16
math_marks_hypothesis = 85
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in each subject mentioned in the premise
if english_marks_premise <= english_marks_hypothesis:
    # check if the estimate of 'english_marks_hypothesis' contradicts the English marks in the premise
    label = "contradiction"
elif math_marks_premise!= math_marks_hypothesis or physics_marks_premise!= physics_marks_hypothesis or chemistry_marks_premise!= chemistry_marks_hypothesis or biology_marks_premise!= biology_marks_hypothesis:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)