english_marks_premise = 86
math_marks_premise = 85
physics_marks_premise = 82
chemistry_marks_premise = 87
biology_marks_premise = 85

english_marks_hypothesis = 86
math_marks_hypothesis = 85
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 87
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects as mentioned in the premise
if english_marks_hypothesis >= english_marks_premise or math_marks_hypothesis >= math_marks_premise or physics_marks_hypothesis >= physics_marks_premise or chemistry_marks_hypothesis >= chemistry_marks_premise or biology_marks_hypothesis >= biology_marks_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
elif english_marks_hypothesis < english_marks_premise and math_marks_hypothesis < math_marks_premise and physics_marks_hypothesis < physics_marks_premise and chemistry_marks_hypothesis < chemistry_marks_premise and biology_marks_hypothesis < biology_marks_premise:
    # check if the hypothesis values are less than the premise ones
    label = "entailment"
else:
    # if the hypothesis values do not contradict or are not less than the premise ones, we can infer neutrality
    label = "neutral"

print(label)
