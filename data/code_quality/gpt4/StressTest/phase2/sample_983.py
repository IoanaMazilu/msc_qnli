english_mark_premise = 72
math_mark_premise = 45
physics_mark_premise = 72
chemistry_mark_premise = 77
biology_mark_premise = 75

english_mark_hypothesis = 62
math_mark_hypothesis = 45
physics_mark_hypothesis = 72
chemistry_mark_hypothesis = 77
biology_mark_hypothesis = 75

# the hypothesis refers to the marks obtained by Dacid for each subject mentioned in the premise
if english_mark_hypothesis != english_mark_premise or math_mark_hypothesis != math_mark_premise or physics_mark_hypothesis != physics_mark_premise or chemistry_mark_hypothesis != chemistry_mark_premise or biology_mark_hypothesis != biology_mark_premise:
    # check if any of the marks in the hypothesis contradicts the corresponding mark reported in the premise
    label = "contradiction"
else:
    # if all the marks in the hypothesis are the same as the ones in the premise, we can infer entailment
    label = "entailment"

print(label)
