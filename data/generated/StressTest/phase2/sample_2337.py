# Premise: Dacid obtained 91, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained more than 41, 65, 82, 67 and 85 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: entailment

english_marks_premise = 91
math_marks_premise = 65
physics_marks_premise = 82
chem_marks_premise = 67
bio_marks_premise = 85

english_marks_hypothesis = 41
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chem_marks_hypothesis = 67
bio_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in each subject mentioned in the premise

if (english_marks_hypothesis >= english_marks_premise or
    math_marks_hypothesis > math_marks_premise or
    physics_marks_hypothesis > physics_marks_premise or
    chem_marks_hypothesis > chem_marks_premise or
    bio_marks_hypothesis > bio_marks_premise):

    # check if the hypothesis values contradict the premise values in any of the subjects
    label = "contradiction"
elif english_marks_hypothesis < english_marks_premise:
    # the hypothesis estimates that Dacid got more than 'english_marks_hypothesis' in English
    # since 'english_marks_hypothesis' is less than 'english_marks_premise', this is consistent with the premise
    # but it cannot be explicitly entailed from the premise because the exact marks Dacid got in English is specified in the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

