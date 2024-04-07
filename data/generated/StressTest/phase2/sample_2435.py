# Premise: David obtained 70, 60, 78, 60 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained more than 70, 60, 78, 60 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: contradiction

english_marks_premise = 70
mathematics_marks_premise = 60
physics_marks_premise = 78
chemistry_marks_premise = 60
biology_marks_premise = 65

english_marks_hypothesis = 70
mathematics_marks_hypothesis = 60
physics_marks_hypothesis = 78
chemistry_marks_hypothesis = 60
biology_marks_hypothesis = 65

# the hypothesis refers to the marks obtained by David, mentioned in the premise
if english_marks_hypothesis <= english_marks_premise or mathematics_marks_hypothesis <= mathematics_marks_premise or physics_marks_hypothesis <= physics_marks_premise or chemistry_marks_hypothesis <= chemistry_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives exact marks for each subject
    # any marks greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

