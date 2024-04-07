# Premise: The total marks obtained by a student in Mathematics and Physics is 20 and his score in Chemistry is 20 marks more than that in Physics.
# Hypothesis: The total marks obtained by a student in Mathematics and Physics is less than 20 and his score in Chemistry is 20 marks more than that in Physics.
# Golden Label: contradiction

total_marks_math_physics_premise = 20
total_marks_math_physics_hypothesis = 20
score_difference_chem_physics = 20

# the hypothesis talks about the total marks in Math and Physics, and the difference in scores between Chemistry and Physics, both referenced in the premise
if total_marks_math_physics_hypothesis > total_marks_math_physics_premise:
    # check if the hypothesis value contradicts the total marks in Math and Physics from the premise
    label = "contradiction"
elif total_marks_math_physics_hypothesis == total_marks_math_physics_premise:
    # check if the total marks in Math and Physics from the hypothesis is equal to that of the premise
    label = "entailment"
else:
    # the premise gives exact total marks in Math and Physics
    # any total marks less than 'total_marks_math_physics_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

