# Premise: Baker Adam is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Hypothesis: Baker Adam is storing cake boxes in cartons that measure less than 85 inches by 42 inches by 60 inches.
# Golden Label: entailment

carton_length_premise = 25
carton_width_premise = 42
carton_height_premise = 60
carton_length_hypothesis = 85

# the hypothesis makes a claim about the dimensions of the cartons in which the cake boxes are stored
if carton_length_hypothesis >= carton_length_premise:
    # check if the hypothesis value contradicts the exact measurement of 'carton_length_premise' 
    label = "contradiction"
elif carton_length_hypothesis < carton_length_premise:
    # check if the measurement in the hypothesis is less than the premise measurement
    label = "entailment"
else:
    # if the hypothesis does not contradict the premise and the measurements are exactly the same
    label = "neutral"

print(label)

