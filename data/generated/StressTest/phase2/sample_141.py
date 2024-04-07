# Premise: David obtained 76, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: David obtained less than 86, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_marks_premise = 76
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 86
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects mentioned in the premise
if english_marks_premise >= english_marks_hypothesis:
    # check if the value of 'english_marks_hypothesis' contradicts the number of marks obtained in English in the premise
    label = "contradiction"
elif math_marks_premise != math_marks_hypothesis or physics_marks_premise != physics_marks_hypothesis or chemistry_marks_premise != chemistry_marks_hypothesis or biology_marks_premise != biology_marks_hypothesis:
    # check if the number of marks obtained in any of the other subjects in the hypothesis contradicts the respective number of marks obtained reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

