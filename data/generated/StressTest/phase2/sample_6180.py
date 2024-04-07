# Premise: David obtained 86, 85, 82, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained more than 16, 85, 82, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: entailment

# defining the marks obtained by David in different subjects
english_mark_premise = 86
math_mark_premise = 85
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 85

english_mark_hypothesis = 16
math_mark_hypothesis = 85
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 85

# hypothesis talks about the marks obtained by David in different subjects, which is also referenced in the premise
if english_mark_hypothesis > english_mark_premise:
    # check if the english mark in the hypothesis contradicts the english mark in the premise
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise:
    # check if the math mark in the hypothesis contradicts the math mark in the premise
    label = "contradiction"
elif physics_mark_hypothesis != physics_mark_premise:
    # check if the physics mark in the hypothesis contradicts the physics mark in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis != chemistry_mark_premise:
    # check if the chemistry mark in the hypothesis contradicts the chemistry mark in the premise
    label = "contradiction"
elif biology_mark_hypothesis != biology_mark_premise:
    # check if the biology mark in the hypothesis contradicts the biology mark in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

