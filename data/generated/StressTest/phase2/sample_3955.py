# Premise: Dacid obtained more than 56, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_mark_premise = 56
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 76
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# The hypothesis talks about the marks Dacid obtained in various subjects, which is also referenced in the premise
if english_mark_hypothesis <= english_mark_premise:
    # Check if the English mark in the hypothesis contradicts the estimate of 'more than english_mark_premise'
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise or physics_mark_hypothesis != physics_mark_premise or chemistry_mark_hypothesis != chemistry_mark_premise or biology_mark_hypothesis != biology_mark_premise:
    # Check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # The premise provides an estimate for the English mark and exact marks for other subjects
    # The marks in the hypothesis do not contradict the premise ones, but the English mark cannot be explicitly entailed from the premise 
    label = "neutral"

print(label)

