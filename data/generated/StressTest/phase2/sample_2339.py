# Premise: Dacid obtained 91, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 81, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

english_mark_premise = 91
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 81
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis talks about the marks Dacid obtained in each subject, referenced also in the premise
if english_mark_premise != english_mark_hypothesis:
    # check if the English mark in the hypothesis contradicts the English mark reported in the premise
    label = "contradiction"
elif math_mark_premise != math_mark_hypothesis or physics_mark_premise != physics_mark_hypothesis or chemistry_mark_premise != chemistry_mark_hypothesis or biology_mark_premise != biology_mark_hypothesis:
    # check if the other subject marks in the hypothesis contradict the same subject marks reported in the premise
    label = "contradiction"
else:
    # if all the marks in the hypothesis match the marks in the premise, we can infer entailment
    label = "entailment"

print(label)

