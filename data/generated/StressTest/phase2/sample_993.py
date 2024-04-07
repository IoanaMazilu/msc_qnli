# Premise: Shankar got 66, 83, 77, 68, 86 marks (out of 100) in English, Maths, physics, Biology and Chemistry.
# Hypothesis: Shankar got more than 26, 83, 77, 68, 86 marks (out of 100) in English, Maths, physics, Biology and Chemistry.
# Golden Label: entailment

english_marks_premise = 66
maths_marks_premise = 83
physics_marks_premise = 77
biology_marks_premise = 68
chemistry_marks_premise = 86

english_marks_hypothesis = 26
maths_marks_hypothesis = 83
physics_marks_hypothesis = 77
biology_marks_hypothesis = 68
chemistry_marks_hypothesis = 86

# the hypothesis refers to the marks Shankar got in English, Maths, physics, Biology and Chemistry, mentioned also in the premise

if english_marks_premise <= english_marks_hypothesis or maths_marks_premise != maths_marks_hypothesis or physics_marks_premise != physics_marks_hypothesis or biology_marks_premise != biology_marks_hypothesis or chemistry_marks_premise != chemistry_marks_hypothesis:
    # check if the marks in hypothesis contradict the marks in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

