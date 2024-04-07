# Premise: Baker Donley is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Hypothesis: Baker Donley is storing cake boxes in cartons that measure less than 35 inches by 42 inches by 60 inches.
# Golden Label: entailment

carton_length_premise = 25
carton_width_premise = 42
carton_height_premise = 60

carton_length_hypothesis = 35
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis refers to the dimensions of the cartons used by Baker Donley as mentioned in the premise
if carton_length_hypothesis >= carton_length_premise:
    # check if the hypothesis length contradicts the length of the carton in the premise
    label = "contradiction"
elif carton_width_hypothesis != carton_width_premise or carton_height_hypothesis != carton_height_premise:
    # check if the hypothesis width or height contradicts the width or height of the carton in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

