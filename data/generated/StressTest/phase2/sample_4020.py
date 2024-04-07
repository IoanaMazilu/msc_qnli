# Premise: Baker Tom is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Hypothesis: Baker Tom is storing cake boxes in cartons that measure more than 15 inches by 42 inches by 60 inches.
# Golden Label: entailment

carton_length_premise = 25
carton_length_hypothesis = 15
carton_width_premise = 42
carton_width_hypothesis = 42
carton_height_premise = 60
carton_height_hypothesis = 60

# the hypothesis refers to the dimensions of the carton mentioned in the premise
if carton_length_premise <= carton_length_hypothesis or carton_width_premise != carton_width_hypothesis or carton_height_premise != carton_height_hypothesis:
    # check if any of the dimensions in the hypothesis contradicts the dimensions mentioned in the premise
    label = "contradiction"
else:
    # if the dimensions in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

