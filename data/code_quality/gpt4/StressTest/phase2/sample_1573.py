english_mark_premise = 26
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 76
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis gives exact marks for each subject, while the premise provides only a lower boundary
if english_mark_hypothesis <= english_mark_premise or math_mark_hypothesis <= math_mark_premise or physics_mark_hypothesis <= physics_mark_premise or chemistry_mark_hypothesis <= chemistry_mark_premise or biology_mark_hypothesis <= biology_mark_premise:
    # check if the hypothesis marks contradict the premise lower boundary for any subject
    label = "contradiction"
else:
    # the premise gives only a lower boundary for the marks
    # any marks greater than the premise's lower boundary are consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
