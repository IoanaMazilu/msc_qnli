# Premise: Arun obtained 76, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Chemistry, Biology and Physics.
# Hypothesis: Arun obtained more than 46, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Chemistry, Biology and Physics.
# Golden Label: entailment

english_marks_premise = 76
mathematics_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 46
mathematics_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in different subjects, mentioned also in the premise
if english_marks_premise <= english_marks_hypothesis or mathematics_marks_premise <= mathematics_marks_hypothesis or chemistry_marks_premise <= chemistry_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis or physics_marks_premise <= physics_marks_hypothesis:
    # check if the hypothesis values contradict the marks obtained by Arun in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

