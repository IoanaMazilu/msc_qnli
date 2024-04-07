# Premise: Dacid obtained more than 46, 85, 92, 87 and 95 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Hypothesis: Dacid obtained 86, 85, 92, 87 and 95 marks (out of 100) in English, Mathematics, Physics, Chemistry and Biology.
# Golden Label: neutral

english_marks_premise = 46
math_marks_premise = 85
physics_marks_premise = 92
chem_marks_premise = 87
bio_marks_premise = 95

english_marks_hypothesis = 86
math_marks_hypothesis = 85
physics_marks_hypothesis = 92
chem_marks_hypothesis = 87
bio_marks_hypothesis = 95

# the hypothesis talks about the marks obtained by Dacid in different subjects, which is also mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the premise that Dacid scored more than 'english_marks_premise' 
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or physics_marks_hypothesis != physics_marks_premise or chem_marks_hypothesis != chem_marks_premise or bio_marks_hypothesis != bio_marks_premise:
    # check if the marks in any other subject in the hypothesis contradict the marks mentioned in the premise
    label = "contradiction"
else:
    # if the marks mentioned in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

