total_marks_math_physics_premise = 20
total_marks_math_physics_hypothesis = 70
more_marks_chemistry_premise = 20
more_marks_chemistry_hypothesis = 20

# the hypothesis refers to the total marks obtained in Mathematics and Physics,
# and the additional marks obtained in Chemistry over Physics, as stated in the premise
if total_marks_math_physics_hypothesis <= total_marks_math_physics_premise:
    # check if the hypothesis estimate contradicts the total marks obtained in Math and Physics in the premise
    label = "contradiction"
elif more_marks_chemistry_hypothesis != more_marks_chemistry_premise:
    # check if the additional marks in Chemistry over Physics in the hypothesis contradicts that in the premise
    label = "contradiction"
else:
    # the hypothesis estimates are consistent with the premise, but cannot be explicitly entailed
    # the hypothesis claims the total marks in Math and Physics is less than 70, which is not stated in the premise
    label = "neutral"

print(label)
