# Premise: Dacid obtained more than 30, 63, 80, 63 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 70, 63, 80, 63 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_marks_premise = 30
english_marks_hypothesis = 70
math_marks_premise = 63
math_marks_hypothesis = 63
physics_marks_premise = 80
physics_marks_hypothesis = 80
chemistry_marks_premise = 63
chemistry_marks_hypothesis = 63
bio_marks_premise = 65
bio_marks_hypothesis = 65

# The hypothesis states the exact marks Dacid got in each subject, which is also referred to in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or bio_marks_hypothesis != bio_marks_premise:
    # check if any of the exact marks in the hypothesis contradicts the exact marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for English marks
    # any number of marks greater than 'english_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

