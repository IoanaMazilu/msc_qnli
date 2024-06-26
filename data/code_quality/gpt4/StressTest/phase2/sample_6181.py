english_mark_premise = 16
maths_mark_premise = 85
physics_mark_premise = 82
chemistry_mark_premise = 87
biology_mark_premise = 85

english_mark_hypothesis = 86
maths_mark_hypothesis = 85
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 87
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in different subjects mentioned in the premise
if english_mark_hypothesis <= english_mark_premise or \
 maths_mark_hypothesis < maths_mark_premise or \
 physics_mark_hypothesis < physics_mark_premise or \
 chemistry_mark_hypothesis < chemistry_mark_premise or \
 biology_mark_hypothesis < biology_mark_premise:
    # checking if any of the marks in the hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
