english_mark_premise = 76
mathematics_mark_premise = 65
physics_mark_premise = 82
chemistry_mark_premise = 67
biology_mark_premise = 85

english_mark_hypothesis = 86
mathematics_mark_hypothesis = 65
physics_mark_hypothesis = 82
chemistry_mark_hypothesis = 67
biology_mark_hypothesis = 85

# the hypothesis is referring to the marks obtained by Dacid in various subjects mentioned in the premise
if english_mark_premise >= english_mark_hypothesis or mathematics_mark_premise > mathematics_mark_hypothesis or physics_mark_premise > physics_mark_hypothesis or chemistry_mark_premise > chemistry_mark_hypothesis or biology_mark_premise > biology_mark_hypothesis:
    # check if the marks obtained in the hypothesis contradict the marks obtained in the premise
    label = "contradiction"
else:
    # if the marks in the hypothesis do not contradict the marks in the premise, we can infer entailment
    label = "entailment"

print(label)
