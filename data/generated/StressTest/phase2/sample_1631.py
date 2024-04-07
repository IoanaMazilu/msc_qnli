# Premise: Baker Raj is storing cake boxes in cartons that measure 25 inches by 42 inches by 60 inches.
# Hypothesis: Baker Raj is storing cake boxes in cartons that measure more than 25 inches by 42 inches by 60 inches.
# Golden Label: contradiction

carton_length_premise = 25
carton_width_premise = 42
carton_height_premise = 60

carton_length_hypothesis = 25
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis refers to the dimensions of the cartons mentioned in the premise
if carton_length_hypothesis <= carton_length_premise or carton_width_hypothesis <= carton_width_premise or carton_height_hypothesis <= carton_height_premise:
    # check if the dimensions of the cartons in the hypothesis contradict the dimensions of the cartons in the premise
    label = "contradiction"
elif carton_length_hypothesis > carton_length_premise and carton_width_hypothesis > carton_width_premise and carton_height_hypothesis > carton_height_premise:
    # check if the dimensions of the cartons in the hypothesis are greater than the dimensions of the cartons in the premise
    label = "entailment"
else:
    # if the dimensions of the cartons in the hypothesis do not contradict or are not greater than the dimensions of the cartons in the premise, we can infer neutrality
    label = "neutral"

print(label)

