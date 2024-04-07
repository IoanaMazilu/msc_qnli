# Premise: Shankar got more than 26, 83, 77, 68, 86 marks (out of 100) in English, Maths, physics, Biology and Chemistry.
# Hypothesis: Shankar got 66, 83, 77, 68, 86 marks (out of 100) in English, Maths, physics, Biology and Chemistry.
# Golden Label: neutral

english_marks_premise = 26
maths_marks_premise = 83
physics_marks_premise = 77
biology_marks_premise = 68
chemistry_marks_premise = 86

english_marks_hypothesis = 66
maths_marks_hypothesis = 83
physics_marks_hypothesis = 77
biology_marks_hypothesis = 68
chemistry_marks_hypothesis = 86

# the hypothesis refers to the marks obtained by Shankar on different subjects mentioned in the premise
if english_marks_hypothesis <= english_marks_premise:
    # check if the stated English marks in the hypothesis contradict the premise
    label = "contradiction"
elif maths_marks_hypothesis != maths_marks_premise or physics_marks_hypothesis != physics_marks_premise or biology_marks_hypothesis != biology_marks_premise or chemistry_marks_hypothesis != chemistry_marks_premise:
    # check if the marks stated in the hypothesis for Maths, Physics, Biology or Chemistry contradict the ones mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

