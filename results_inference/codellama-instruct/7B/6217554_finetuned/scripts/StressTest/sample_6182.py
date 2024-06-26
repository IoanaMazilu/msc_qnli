# define variables for each mark obtained in each subject
english_mark_premise = 86
mathematics_mark_premise = 85
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 85

english_mark_hypothesis = 86
mathematics_mark_hypothesis = 85
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 85

# check if the marks obtained in each subject in the hypothesis contradict the premise ones
if english_mark_hypothesis >= english_mark_premise:
    label = "contradiction"
elif mathematics_mark_hypothesis >= mathematics_mark_premise:
    label = "contradiction"
elif physics_mark_hypothesis >= physics_mark_premise:
    label = "contradiction"
elif chemistry_mark_hypothesis >= chemistry_mark_premise:
    label = "contradiction"
elif biology_mark_hypothesis >= biology_mark_premise:
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
