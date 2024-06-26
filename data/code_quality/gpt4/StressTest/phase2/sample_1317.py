# Defining the variables from the premise and hypothesis sentences
english_marks_premise = 76
mathematics_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 56
mathematics_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# Comparing the marks in each subject from the hypothesis with those from the premise
if english_marks_premise <= english_marks_hypothesis or mathematics_marks_premise <= mathematics_marks_hypothesis or chemistry_marks_premise <= chemistry_marks_hypothesis or biology_marks_premise <= biology_marks_hypothesis or physics_marks_premise <= physics_marks_hypothesis:
    # If the marks in any subject from the hypothesis are less than or equal to those from the premise, this is a contradiction
    label = "contradiction"
elif english_marks_premise > english_marks_hypothesis and mathematics_marks_premise > mathematics_marks_hypothesis and chemistry_marks_premise > chemistry_marks_hypothesis and biology_marks_premise > biology_marks_hypothesis and physics_marks_premise > physics_marks_hypothesis:
    # If the marks in all subjects from the hypothesis are greater than those from the premise, this is an entailment
    label = "entailment"
else:
    # If neither of the above conditions are met, the relationship is neutral
    label = "neutral"

print(label)
