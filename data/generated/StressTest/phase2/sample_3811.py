# Premise: David obtained more than 46, 95, 82, 97 and 95 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained 96, 95, 82, 97 and 95 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: neutral

english_marks_premise = 46
math_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 97
biology_marks_premise = 95

english_marks_hypothesis = 96
math_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 97
biology_marks_hypothesis = 95

# the hypothesis talks about the marks obtained in different subjects, which are also mentioned in the premise
if english_marks_hypothesis <= english_marks_premise or math_marks_hypothesis < math_marks_premise or physics_marks_hypothesis < physics_marks_premise or chemistry_marks_hypothesis < chemistry_marks_premise or biology_marks_hypothesis < biology_marks_premise:
    # check if the marks obtained in the hypothesis contradict the premise
    label = "contradiction"
elif english_marks_hypothesis > english_marks_premise and math_marks_hypothesis == math_marks_premise and physics_marks_hypothesis == physics_marks_premise and chemistry_marks_hypothesis == chemistry_marks_premise and biology_marks_hypothesis == biology_marks_premise:
    # check if the marks obtained in the hypothesis are consistent with the premise. If yes, then the hypothesis can be fully entailed from the premise
    label = "entailment"
else:
    # if the marks obtained in the hypothesis do not contradict the premise but also cannot be fully and explicitly entailed from the premise, we infer neutrality
    label = "neutral"

print(label)

