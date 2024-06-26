english_mark_premise = 76
math_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 86
math_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis refers to the marks obtained by David in various subjects mentioned in the premise
if english_mark_premise >= english_mark_hypothesis:
    # check if the estimate of 'english_mark_hypothesis' contradicts the mark in English in the premise
    label = "contradiction"
elif math_mark_premise!= math_mark_hypothesis or physics_mark_premise!= physics_mark_hypothesis or chemistry_mark_premise!= chemistry_mark_hypothesis or biology_mark_premise!= biology_mark_hypothesis:
    # check if the marks in other subjects in the hypothesis contradict the marks reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
