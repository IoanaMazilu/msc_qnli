# Premise: Dacid obtained 51, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained less than 81, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

marks_english_premise = 51
marks_mathematics_premise = 65
marks_physics_premise = 82
marks_chemistry_premise = 67
marks_biology_premise = 85

marks_english_hypothesis = 81
marks_mathematics_hypothesis = 65
marks_physics_hypothesis = 82
marks_chemistry_hypothesis = 67
marks_biology_hypothesis = 85

# hypothesis refers to the marks obtained by Dacid in English, Mathematics, Physics, Chemistry and Biology mentioned in the premise
if marks_english_premise > marks_english_hypothesis:
    # check if the marks obtained in English in the premise contradicts the marks in English hypothesized
    label = "contradiction"
elif marks_mathematics_premise != marks_mathematics_hypothesis or marks_physics_premise != marks_physics_hypothesis or marks_chemistry_premise != marks_chemistry_hypothesis or marks_biology_premise != marks_biology_hypothesis:
    # check if the marks obtained in Mathematics, Physics, Chemistry and Biology in the premise contradicts the marks in these subjects hypothesized
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

