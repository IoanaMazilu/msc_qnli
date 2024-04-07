# Premise: Dacid obtained more than 53, 69, 92, 64 and 82 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 73, 69, 92, 64 and 82 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_marks_premise = 53
math_marks_premise = 69
physics_marks_premise = 92
chemistry_marks_premise = 64
biology_marks_premise = 82

english_marks_hypothesis = 73
math_marks_hypothesis = 69
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 64
biology_marks_hypothesis = 82

# the hypothesis refers to the marks obtained by Dacid in different subjects (English, Mathematics, Physics, Chemistry and Biology) mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value for English marks contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the marks obtained in other subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

