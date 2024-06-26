english_marks_premise = 76
english_marks_hypothesis = 86

mathematics_marks_premise = 65
mathematics_marks_hypothesis = 65

physics_marks_premise = 82
physics_marks_hypothesis = 82

chemistry_marks_premise = 67
chemistry_marks_hypothesis = 67

biology_marks_premise = 85
biology_marks_hypothesis = 85

# the hypothesis refers to the marks obtained by David in the subjects English, mathematics, physics, chemistry and biology
if english_marks_premise >= english_marks_hypothesis:
    # check if the english marks in the premise contradict the hypothesis
    label = "contradiction"
elif mathematics_marks_premise >= mathematics_marks_hypothesis:
    # check if the mathematics marks in the premise contradict the hypothesis
    label = "contradiction"
elif physics_marks_premise >= physics_marks_hypothesis:
    # check if the physics marks in the premise contradict the hypothesis
    label = "contradiction"
elif chemistry_marks_premise >= chemistry_marks_hypothesis:
    # check if the chemistry marks in the premise contradict the hypothesis
    label = "contradiction"
elif biology_marks_premise >= biology_marks_hypothesis:
    # check if the biology marks in the premise contradict the hypothesis
    label = "contradiction"
else:
    # if the english, mathematics, physics, chemistry and biology marks do not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
