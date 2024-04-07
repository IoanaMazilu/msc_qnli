# Premise: Dacid obtained 45, 35, 52, 47 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 15, 35, 52, 47 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: contradiction

english_marks_premise = 45
math_marks_premise = 35
physics_marks_premise = 52
chemistry_marks_premise = 47
biology_marks_premise = 55

english_marks_hypothesis = 15
math_marks_hypothesis = 35
physics_marks_hypothesis = 52
chemistry_marks_hypothesis = 47
biology_marks_hypothesis = 55

# the hypothesis talks about the marks obtained by Dacid in various subjects, mentioned also in the premise
if english_marks_hypothesis != english_marks_premise or math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if any of the marks in the hypothesis contradict the corresponding marks given in the premise
    label = "contradiction"
else:
    # if all the marks in the hypothesis match with the premise ones, we can infer entailment
    label = "entailment"

print(label)

