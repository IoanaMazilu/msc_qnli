# Premise: Dacid obtained more than 41, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 91, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

# Define variables for the premise
marks_english_premise = 41
marks_mathematics_premise = 65
marks_physics_premise = 82
marks_chemistry_premise = 67
marks_biology_premise = 85

# Define variables for the hypothesis
marks_english_hypothesis = 91
marks_mathematics_hypothesis = 65
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 67
marks_biology_hypothesis = 85

# the hypothesis talks about the marks obtained by Dacid in various subjects, which are also referenced in the premise
# Check if the marks in the hypothesis are lower or equal to the marks in the premise, which would contradict the premise's claim of 'more than' the stated marks
if marks_english_hypothesis <= marks_english_premise or marks_mathematics_hypothesis <= marks_mathematics_premise or marks_physics_hypothesis <= marks_physics_premise or marks_chemistry_hypothesis <= marks_chemistry_premise or marks_biology_hypothesis <= marks_biology_premise:
    label = "contradiction"
elif marks_english_hypothesis == marks_english_premise+1 and marks_mathematics_hypothesis == marks_mathematics_premise+1 and marks_physics_hypothesis == marks_physics_premise+1 and marks_chemistry_hypothesis == marks_chemistry_premise+1 and marks_biology_hypothesis == marks_biology_premise+1:
    # if the hypothesis values are exactly one mark more than the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the number of marks
    # any number of marks greater than the premise's ones is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

