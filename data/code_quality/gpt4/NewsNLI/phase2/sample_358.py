camera_value_premise = 10000
camera_value_hypothesis = 10000

# the hypothesis mentions the value of the camera, which is also referenced in the premise
if camera_value_hypothesis != camera_value_premise:
    # check if the camera value in the hypothesis contradicts the camera value reported in the premise
    label = "contradiction"
else:
    # if the camera value from the hypothesis does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
