# Premise: Dacid obtained 70, 63, 80, 63 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 30, 63, 80, 63 and 65 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_mark_premise = 70
english_mark_hypothesis = 30
math_mark_premise = 63
math_mark_hypothesis = 63
physics_mark_premise = 80
physics_mark_hypothesis = 80
chemistry_mark_premise = 63
chemistry_mark_hypothesis = 63
biology_mark_premise = 65
biology_mark_hypothesis = 65

# the hypothesis refers to the marks obtained by Dacid in the premise
if english_mark_premise <= english_mark_hypothesis:
    # check if the estimate of 'english_mark_hypothesis' contradicts the mark in English in the premise
    label = "contradiction"
elif math_mark_hypothesis != math_mark_premise:
    # check if the mark in Mathematics in the hypothesis contradicts the mark in Mathematics reported in the premise
    label = "contradiction"
elif physics_mark_hypothesis != physics_mark_premise:
    # check if the mark in Physics in the hypothesis contradicts the mark in Physics reported in the premise
    label = "contradiction"
elif chemistry_mark_hypothesis != chemistry_mark_premise:
    # check if the mark in Chemistry in the hypothesis contradicts the mark in Chemistry reported in the premise
    label = "contradiction"
elif biology_mark_hypothesis != biology_mark_premise:
    # check if the mark in Biology in the hypothesis contradicts the mark in Biology reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

