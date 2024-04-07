# Premise: David obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained more than 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: contradiction

english_marks_premise = 76
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis talks about the marks obtained in each subject, referenced also in the premise
if english_marks_hypothesis <= english_marks_premise and mathematics_marks_hypothesis <= mathematics_marks_premise and physics_marks_hypothesis <= physics_marks_premise and chemistry_marks_hypothesis <= chemistry_marks_premise and biology_marks_hypothesis <= biology_marks_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives the exact marks for each subject
    # any number of marks greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

