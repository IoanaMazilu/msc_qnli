english_marks_premise = 35
math_marks_premise = 35
phys_marks_premise = 52
chem_marks_premise = 47
bio_marks_premise = 55

english_marks_hypothesis = 45
math_marks_hypothesis = 35
phys_marks_hypothesis = 52
chem_marks_hypothesis = 47
bio_marks_hypothesis = 55

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or phys_marks_hypothesis != phys_marks_premise or chem_marks_hypothesis != chem_marks_premise or bio_marks_hypothesis != bio_marks_premise:
    # check if the marks obtained in other subjects in the hypothesis contradicts the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
