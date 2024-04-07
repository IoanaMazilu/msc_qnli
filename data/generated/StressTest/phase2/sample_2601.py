# Premise: David obtained 36, 35, 42, 57 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Hypothesis: David obtained more than 26, 35, 42, 57 and 55 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology What are his average marks?
# Golden Label: entailment

marks_english_premise = 36
marks_english_hypothesis = 26
marks_math_premise = 35
marks_math_hypothesis = 35
marks_physics_premise = 42
marks_physics_hypothesis = 42
marks_chem_premise = 57
marks_chem_hypothesis = 57
marks_bio_premise = 55
marks_bio_hypothesis = 55

# the hypothesis refers to the marks obtained by David in different subjects mentioned in the premise
if marks_english_hypothesis >= marks_english_premise:
    # check if the estimate of 'marks_english_hypothesis' contradicts the marks obtained in English in the premise
    label = "contradiction"
elif marks_math_hypothesis != marks_math_premise or marks_physics_hypothesis != marks_physics_premise or marks_chem_hypothesis != marks_chem_premise or marks_bio_hypothesis != marks_bio_premise:
    # check if the marks obtained in any of the other subjects in the hypothesis contradicts the marks obtained in the same subjects in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

