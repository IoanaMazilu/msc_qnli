# Premise: Dacid obtained 90, 92, 85, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 20, 92, 85, 87 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_mark_premise = 90
math_mark_premise = 92
physics_mark_premise = 85
chemistry_mark_premise = 87
biology_mark_premise = 85

english_mark_hypothesis = 20
math_mark_hypothesis = 92
physics_mark_hypothesis = 85
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 85

# the hypothesis refers to Dacid's marks in five subjects mentioned in the premise
if english_mark_premise <= english_mark_hypothesis:
    # check if the estimate of 'english_mark_hypothesis' contradicts the mark in English in the premise
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise or physics_mark_hypothesis != physics_mark_premise or chemistry_mark_hypothesis != chemistry_mark_premise or biology_mark_hypothesis != biology_mark_premise:
    # check if the mark in any of the subjects in the hypothesis contradicts the mark reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

