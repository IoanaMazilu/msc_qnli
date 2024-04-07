# Premise: David obtained 76, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: David obtained more than 66, 65, 82, 67 and 85 marks (out in 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

# define variables for David's marks in various subjects in premise and hypothesis
english_marks_premise = 76
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 66
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in various subjects mentioned in the premise
# check if the marks in hypothesis are more than the marks in premise for each subject
if english_marks_premise <= english_marks_hypothesis or mathematics_marks_premise <= mathematics_marks_hypothesis or physics_marks_premise <= physics_marks_hypothesis or chemistry_marks_premise <= chemistry_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis:
    # if the marks in hypothesis for any subject are more than the marks in premise, it's a contradiction
    label = "contradiction"
elif english_marks_premise == english_marks_hypothesis and mathematics_marks_premise == mathematics_marks_hypothesis and physics_marks_premise == physics_marks_hypothesis and chemistry_marks_premise == chemistry_marks_hypothesis and biology_marks_premise == biology_marks_hypothesis:
    # if the marks in hypothesis for all subjects are equal to the marks in premise, it's an entailment
    label = "entailment"
else:
    # if the marks in hypothesis for any subject are less than the marks in premise but not equal to, it's neutral
    label = "neutral"

print(label)

