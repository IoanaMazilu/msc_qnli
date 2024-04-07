# Premise: Baker Ram is storing cake boxes in cartons that measure less than 45 inches by 42 inches by 60 inches.
# Hypothesis: Baker Ram is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Golden Label: neutral

carton_length_premise = 45
carton_width_premise = 42
carton_height_premise = 60

carton_length_hypothesis = 25
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis talks about the dimensions of the cartons Baker Ram is using for storing cake boxes, referenced also in the premise
if carton_length_hypothesis >= carton_length_premise or \
   carton_width_hypothesis > carton_width_premise or \
   carton_height_hypothesis > carton_height_premise:
    # check if the hypothesis values contradict the premise's estimates of less than 'carton_length_premise', 'carton_width_premise' and 'carton_height_premise'
    label = "contradiction"
elif carton_length_hypothesis < carton_length_premise and \
     carton_width_hypothesis == carton_width_premise and \
     carton_height_hypothesis == carton_height_premise:
    # if the hypothesis values are consistent with the premise's estimates and do not exceed them, we can infer entailment
    label = "entailment"
else:
    # any other possible scenario leads to a neutral relation
    label = "neutral"

print(label)

