# Premise: Dacid obtained 96, 98, 99, 100 and 98 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 76, 98, 99, 100 and 98 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_marks_premise = 96
math_marks_premise = 98
physics_marks_premise = 99
chemistry_marks_premise = 100
biology_marks_premise = 98

english_marks_hypothesis = 76
math_marks_hypothesis = 98
physics_marks_hypothesis = 99
chemistry_marks_hypothesis = 100
biology_marks_hypothesis = 98

# the hypothesis refers to the marks obtained by Dacid in five subjects, which are also mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or math_marks_premise <= math_marks_hypothesis or physics_marks_premise <= physics_marks_hypothesis or chemistry_marks_premise <= chemistry_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis:
    # Check if the hypothesis contradicts the premise for any subject
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

