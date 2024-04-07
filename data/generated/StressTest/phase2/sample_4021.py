# Premise: Baker Tom is storing cake boxes in cartons that measure more than 15 inches by 42 inches by 60 inches.
# Hypothesis: Baker Tom is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Golden Label: neutral

carton_length_premise = 15
carton_width_premise = 42
carton_height_premise = 60

carton_length_hypothesis = 25
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis refers to the dimensions of the cartons mentioned in the premise
if carton_length_hypothesis <= carton_length_premise:
    # check if the length in the hypothesis contradicts the estimate of more than 'carton_length_premise'
    label = "contradiction"
elif carton_width_hypothesis != carton_width_premise or carton_height_hypothesis != carton_height_premise:
    # check if the width or height in the hypothesis contradicts the width or height mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the length of the cartons
    # any length greater than 'carton_length_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

