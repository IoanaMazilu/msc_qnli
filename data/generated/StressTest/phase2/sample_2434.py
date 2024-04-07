# Premise: David obtained more than 60, 60, 78, 60 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 70, 60, 78, 60 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_marks_premise = 60
mathematics_marks_premise = 60
physics_marks_premise = 78
chemistry_marks_premise = 60
biology_marks_premise = 65

english_marks_hypothesis = 70
mathematics_marks_hypothesis = 60
physics_marks_hypothesis = 78
chemistry_marks_hypothesis = 60
biology_marks_hypothesis = 65

# the hypothesis refers to the marks obtained by David in different subjects, mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif mathematics_marks_hypothesis != mathematics_marks_premise:
    # check if the Mathematics marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
elif physics_marks_hypothesis != physics_marks_premise:
    # check if the Physics marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
elif chemistry_marks_hypothesis != chemistry_marks_premise:
    # check if the Chemistry marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
elif biology_marks_hypothesis != biology_marks_premise:
    # check if the Biology marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

