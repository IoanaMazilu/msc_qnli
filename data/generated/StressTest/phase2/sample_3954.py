# Premise: Dacid obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 56, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_mark_premise = 76
mathematics_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 56
mathematics_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in each subject mentioned in the premise
if english_mark_premise <= english_mark_hypothesis:
    # check if the mark estimated in 'english_mark_hypothesis' contradicts the mark obtained in English in the premise
    label = "contradiction"
elif mathematics_mark_premise != mathematics_mark_hypothesis:
    # check if the mark estimated in 'mathematics_mark_hypothesis' contradicts the mark obtained in Mathematics in the premise
    label = "contradiction"
elif physics_mark_premise != physics_mark_hypothesis:
    # check if the mark estimated in 'physics_mark_hypothesis' contradicts the mark obtained in Physics in the premise
    label = "contradiction"
elif chemistry_mark_premise != chemistry_mark_hypothesis:
    # check if the mark estimated in 'chemistry_mark_hypothesis' contradicts the mark obtained in Chemistry in the premise
    label = "contradiction"
elif biology_mark_premise != biology_mark_hypothesis:
    # check if the mark estimated in 'biology_mark_hypothesis' contradicts the mark obtained in Biology in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

