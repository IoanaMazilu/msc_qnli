english_marks_premise = 76
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects mentioned in the premise
if english_marks_premise >= english_marks_hypothesis:
    # check if the estimate of 'english_marks_hypothesis' contradicts the English marks in the premise
    label = "contradiction"
elif mathematics_marks_premise!= mathematics_marks_hypothesis or physics_marks_premise!= physics_marks_hypothesis or chemistry_marks_premise!= chemistry_marks_hypothesis or biology_marks_premise!= biology_marks_hypothesis:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
