english_marks_premise = 61
math_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 61
math_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in different subjects as stated in the premise
# we check if the hypothesis marks in each subject contradicts the premise marks
if english_marks_hypothesis <= english_marks_premise or math_marks_hypothesis <= math_marks_premise or physics_marks_hypothesis <= physics_marks_premise or chemistry_marks_hypothesis <= chemistry_marks_premise or biology_marks_hypothesis <= biology_marks_premise:
    label = "contradiction"
else:
    # the premise gives exact marks for each subject
    # any marks higher than 'premise_marks' in each subject is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
