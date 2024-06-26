english_marks_premise = 76
maths_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 76
maths_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Arun in the respective subjects
if english_marks_hypothesis >= english_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in English
    label = "contradiction"
elif maths_marks_hypothesis >= maths_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Mathematics
    label = "contradiction"
elif chemistry_marks_hypothesis >= chemistry_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Chemistry
    label = "contradiction"
elif biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Biology
    label = "contradiction"
elif physics_marks_hypothesis >= physics_marks_premise:
    # check if the hypothesis value contradicts the mark obtained in Physics
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
