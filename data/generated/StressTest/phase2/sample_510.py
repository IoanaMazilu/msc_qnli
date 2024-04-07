# Premise: Dacid obtained 76, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 66, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_mark_premise = 76
mathematics_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 66
mathematics_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis talks about the marks obtained by Dacid in different subjects, which is also referenced in the premise
if english_mark_premise <= english_mark_hypothesis or mathematics_mark_premise <= mathematics_mark_hypothesis or physics_mark_premise <= physics_mark_hypothesis or chemistry_mark_premise <= chemistry_mark_hypothesis or biology_mark_premise <= biology_mark_hypothesis:
    # check if the hypothesis values contradict the marks obtained by Dacid in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

