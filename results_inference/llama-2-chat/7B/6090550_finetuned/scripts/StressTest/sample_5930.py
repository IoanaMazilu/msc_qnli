english_marks_premise = 86
mathematics_marks_premise = 85
physics_marks_premise = 92
chemistry_marks_premise = 87
biology_marks_premise = 95

english_marks_hypothesis = 86
mathematics_marks_hypothesis = 85
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in different subjects
if english_marks_hypothesis >= english_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in English
    label = "contradiction"
elif mathematics_marks_hypothesis >= mathematics_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Mathematics
    label = "contradiction"
elif physics_marks_hypothesis >= physics_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Physics
    label = "contradiction"
elif chemistry_marks_hypothesis >= chemistry_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Chemistry
    label = "contradiction"
elif biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Biology
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
