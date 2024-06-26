english_marks_premise = 76
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the exact scores mentioned in the premise
if english_marks_hypothesis >= english_marks_premise or math_marks_hypothesis >= math_marks_premise or physics_marks_hypothesis >= physics_marks_premise or chemistry_marks_hypothesis >= chemistry_marks_premise or biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis contradicts the premise by suggesting that the scores are less than they actually are
    label = "contradiction"
else:
    # if the hypothesis does not contradict any of the premise scores, we can infer entailment
    label = "entailment"

print(label)
