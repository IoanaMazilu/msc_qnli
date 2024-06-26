english_mark_premise = 86
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 76
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis talks about the marks obtained by David in different subjects, referenced also in the premise
if english_mark_hypothesis >= english_mark_premise or math_mark_hypothesis > math_mark_premise or physics_mark_hypothesis > physics_mark_premise or chemistry_mark_hypothesis > chemistry_mark_premise or biology_mark_hypothesis > biology_mark_premise:
    # check if the marks in the hypothesis contradict the maximum marks mentioned in the premise
    label = "contradiction"
else:
    # all the marks provided in the hypothesis are less than or equal to the provided marks in the premise, so we can infer entailment
    label = "entailment"

print(label)
