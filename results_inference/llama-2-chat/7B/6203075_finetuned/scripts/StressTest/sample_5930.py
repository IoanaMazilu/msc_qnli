english_marks_premise = 86
english_marks_hypothesis = 86

mathematics_marks_premise = 85
mathematics_marks_hypothesis = 85

physics_marks_premise = 92
physics_marks_hypothesis = 92

chemistry_marks_premise = 87
chemistry_marks_hypothesis = 87

biology_marks_premise = 95
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in English, Mathematics, Physics, Chemistry and Biology
if english_marks_premise >= english_marks_hypothesis:
    # check if the English marks in the premise contradict the hypothesis that Dacid obtained less than 86 marks in English
    label = "entailment"
elif mathematics_marks_premise >= mathematics_marks_hypothesis:
    # check if the Mathematics marks in the premise contradict the hypothesis that Dacid obtained less than 85 marks in Mathematics
    label = "entailment"
elif physics_marks_premise >= physics_marks_hypothesis:
    # check if the Physics marks in the premise contradict the hypothesis that Dacid obtained less than 92 marks in Physics
    label = "entailment"
elif chemistry_marks_premise >= chemistry_marks_hypothesis:
    # check if the Chemistry marks in the premise contradict the hypothesis that Dacid obtained less than 87 marks in Chemistry
    label = "entailment"
elif biology_marks_premise >= biology_marks_hypothesis:
    # check if the Biology marks in the premise contradict the hypothesis that Dacid obtained less than 95 marks in Biology
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
