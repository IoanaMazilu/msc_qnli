# Premise: David obtained more than 26, 35, 42, 57 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 36, 35, 42, 57 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_marks_premise = 26
math_marks_premise = 35
physics_marks_premise = 42
chemistry_marks_premise = 57
biology_marks_premise = 55

english_marks_hypothesis = 36
math_marks_hypothesis = 35
physics_marks_hypothesis = 42
chemistry_marks_hypothesis = 57
biology_marks_hypothesis = 55

# the hypothesis refers to the marks obtained by David in different subjects as mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the premise estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the marks obtained in any of the remaining subjects contradicts the premise values
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

