english_marks_premise = 76
math_marks_premise = 65
chemistry_marks_premise = 82
biology_marks_premise = 67
physics_marks_premise = 85

english_marks_hypothesis = 76
math_marks_hypothesis = 65
chemistry_marks_hypothesis = 82
biology_marks_hypothesis = 67
physics_marks_hypothesis = 85

# the hypothesis references the marks obtained by Arun in each subject mentioned in the premise
if english_marks_hypothesis <= english_marks_premise or \
   math_marks_hypothesis <= math_marks_premise or \
   chemistry_marks_hypothesis <= chemistry_marks_premise or \
   biology_marks_hypothesis <= biology_marks_premise or \
   physics_marks_hypothesis <= physics_marks_premise:
    # check if the hypothesis values contradict the premise ones
    label = "entailment"
else:
    # if the hypothesis values do not contradict the premise ones, but are expected to be more, we infer neutral
    label = "neutral"

print(label)
