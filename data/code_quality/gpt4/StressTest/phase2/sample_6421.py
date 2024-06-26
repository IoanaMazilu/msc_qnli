english_marks_premise = 66
math_marks_premise = 65
chem_marks_premise = 82
bio_marks_premise = 67
phy_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
chem_marks_hypothesis = 82
bio_marks_hypothesis = 67
phy_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in various subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the premise
    label = "contradiction"
elif math_marks_hypothesis != math_marks_premise or chem_marks_hypothesis != chem_marks_premise or bio_marks_hypothesis != bio_marks_premise or phy_marks_hypothesis != phy_marks_premise:
    # check if the marks in Mathematics, Chemistry, Biology and Physics in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
