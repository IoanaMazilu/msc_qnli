carton_length_premise = 25
carton_width_premise = 42
carton_height_premise = 60

carton_length_hypothesis = 45
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis refers to the measurements of the cartons mentioned in the premise
if carton_length_hypothesis >= carton_length_premise:
    # check if the 'carton_length_hypothesis' contradicts the length of cartons mentioned in the premise
    label = "contradiction"
elif carton_width_hypothesis != carton_width_premise or carton_height_hypothesis != carton_height_premise:
    # check if the width or height in the hypothesis contradicts the width or height mentioned in the premise
    label = "contradiction"
else:
    # if the measurements in the hypothesis do not contradict the ones from the premise, we can infer entailment
    label = "entailment"

print(label)
