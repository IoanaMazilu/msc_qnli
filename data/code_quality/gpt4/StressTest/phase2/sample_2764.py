english_marks_premise = 51
mathematics_marks_premise = 65
physics_marks_premise = 82
chemistry_marks_premise = 67
biology_marks_premise = 85

english_marks_hypothesis = 61
mathematics_marks_hypothesis = 65
physics_marks_hypothesis = 82
chemistry_marks_hypothesis = 67
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by Dacid in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the English marks in the hypothesis contradict the estimate of more than 'english_marks_premise'
    label = "contradiction"
elif mathematics_marks_hypothesis != mathematics_marks_premise or physics_marks_hypothesis != physics_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise or biology_marks_hypothesis != biology_marks_premise:
    # check if the other marks in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the English marks
    # any number of marks in English greater than 'english_marks_premise' and the exact marks in the other subjects are consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
