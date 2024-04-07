# Premise: David obtained 72, 60, 35, 62 and 84 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained more than 72, 60, 35, 62 and 84 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: contradiction

marks_english_premise = 72
marks_mathematics_premise = 60
marks_physics_premise = 35
marks_chemistry_premise = 62
marks_biology_premise = 84

marks_english_hypothesis = 72
marks_mathematics_hypothesis = 60
marks_physics_hypothesis = 35
marks_chemistry_hypothesis = 62
marks_biology_hypothesis = 84

# the hypothesis talks about the marks obtained by David, referenced also in the premise
if marks_english_hypothesis <= marks_english_premise or marks_mathematics_hypothesis <= marks_mathematics_premise or marks_physics_hypothesis <= marks_physics_premise or marks_chemistry_hypothesis <= marks_chemistry_premise or marks_biology_hypothesis <= marks_biology_premise:
    # check if the hypothesis value contradicts the estimate of more than the marks obtained in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained
    # any marks greater than the marks obtained in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

