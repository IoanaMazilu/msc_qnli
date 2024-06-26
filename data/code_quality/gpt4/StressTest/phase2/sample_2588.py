english_marks_premise = 96
mathematics_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 97
biology_marks_premise = 95

english_marks_hypothesis = 36
mathematics_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 97
biology_marks_hypothesis = 95

# The hypothesis refers to the marks Dacid obtained in different subjects, which are also mentioned in the premise.
if english_marks_hypothesis != english_marks_premise:
    # check if the English marks in the hypothesis contradicts the English marks reported in the premise
    label = "contradiction"
elif mathematics_marks_hypothesis != mathematics_marks_premise or \
    physics_marks_hypothesis != physics_marks_premise or \
    chemistry_marks_hypothesis != chemistry_marks_premise or \
    biology_marks_hypothesis != biology_marks_premise:
    # check if the marks in other subjects in the hypothesis contradicts the marks in those subjects reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
