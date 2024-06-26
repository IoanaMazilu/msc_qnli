english_marks_premise = 86
math_marks_premise = 85
physics_marks_premise = 92
chemistry_marks_premise = 87
biology_marks_premise = 95

english_marks_hypothesis = 86
math_marks_hypothesis = 85
physics_marks_hypothesis = 92
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 95

# the hypothesis refers to the marks obtained by Dacid in different subjects mentioned in the premise
if english_marks_hypothesis >= english_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'english_marks_premise'
    label = "contradiction"
elif math_marks_hypothesis >= math_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than'math_marks_premise'
    label = "contradiction"
elif physics_marks_hypothesis >= physics_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'physics_marks_premise'
    label = "contradiction"
elif chemistry_marks_hypothesis >= chemistry_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'chemistry_marks_premise'
    label = "contradiction"
elif biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'biology_marks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the marks obtained by Dacid
    # any marks less than 'english_marks_premise','math_marks_premise', 'physics_marks_premise', 'chemistry_marks_premise' and 'biology_marks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
