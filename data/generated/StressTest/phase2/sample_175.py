# Premise: Baker Donley is storing cake boxes in cartons that measure less than 35 inches by 42 inches by 60 inches.
# Hypothesis: Baker Donley is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Golden Label: neutral

carton_length_premise = 35
carton_width_premise = 42
carton_height_premise = 60
carton_length_hypothesis = 25
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis refers to the dimensions of the cartons mentioned in the premise
if carton_length_hypothesis >= carton_length_premise or carton_width_hypothesis > carton_width_premise or carton_height_hypothesis > carton_height_premise:
    # check if the dimensions in the hypothesis contradict the maximum dimensions in the premise
    label = "contradiction"
elif carton_length_hypothesis > carton_length_premise and carton_width_hypothesis == carton_width_premise and carton_height_hypothesis == carton_height_premise:
    # check if the dimensions in the hypothesis are exactly as in the premise, which would mean entailment
    label = "entailment"
else:
    # if the hypothesis dimensions do not contradict the premise ones, but are not the same either, we can infer neutrality
    label = "neutral"

print(label)

