# Premise: Dacid obtained 96, 95, 82, 87 and 92 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 16, 95, 82, 87 and 92 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_marks_premise = 96
math_marks_premise = 95
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 92

english_marks_hypothesis = 16
math_marks_hypothesis = 95
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 92

# the hypothesis refers to the marks obtained by Dacid in several subjects, which are mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or math_marks_premise < math_marks_hypothesis or physics_marks_premise < physics_marks_hypothesis or chemistry_marks_premise < chemistry_marks_hypothesis or biology_marks_premise < biology_marks_hypothesis:
    # check if any of the marks in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
elif english_marks_premise > english_marks_hypothesis:
    # check if the English marks in the premise are more than English marks in the hypothesis
    label = "entailment"
else:
    # if the marks in the hypothesis do not contradict the premise ones, and English marks are not more than the hypothesis, it's neutral
    label = "neutral"

print(label)

