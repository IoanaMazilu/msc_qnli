# Premise: Dacid obtained 73, 69, 92, 64 and 82 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 53, 69, 92, 64 and 82 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_marks_premise = 73
math_marks_premise = 69
physics_marks_premise = 92
chemistry_marks_premise = 64
biology_marks_premise = 82

english_marks_hypothesis = 53
math_marks_hypothesis = 69
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 64
biology_marks_hypothesis = 82

# the hypothesis refers to the marks obtained by Dacid in English, Mathematics, Physics, Chemistry and Biology, mentioned in the premise
if english_marks_premise <= english_marks_hypothesis or \
   math_marks_premise <= math_marks_hypothesis or \
   physics_marks_premise <= physics_marks_hypothesis or \
   chemistry_marks_premise <= chemistry_marks_hypothesis or \
   biology_marks_premise <= biology_marks_hypothesis:
    # check if any of the marks in the hypothesis contradict the marks Dacid obtained in the premise
    label = "contradiction"
elif english_marks_premise > english_marks_hypothesis and \
     math_marks_premise == math_marks_hypothesis and \
     physics_marks_premise == physics_marks_hypothesis and \
     chemistry_marks_premise == chemistry_marks_hypothesis and \
     biology_marks_premise == biology_marks_hypothesis:
    # check if all the marks in the hypothesis are either less than or equal to the marks Dacid obtained in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones and they are not all less than or equal to the premise ones, we can infer neutrality
    label = "neutral"

print(label)

