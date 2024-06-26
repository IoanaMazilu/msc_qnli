# Defining the variables for premise
carton_length_premise = 25
carton_width_premise = 42
carton_height_premise = 60

# Defining the variables for hypothesis
carton_length_hypothesis = 25
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# Check if the dimensions of the carton mentioned in the hypothesis are more than the dimensions mentioned in the premise
if carton_length_hypothesis <= carton_length_premise and carton_width_hypothesis <= carton_width_premise and carton_height_hypothesis <= carton_height_premise:
    # If the dimensions are equal, then the statements are contradicting
    label = "contradiction"
else:
    # If the dimensions are not more than the ones in the premise, then the relationship is neutral
    label = "neutral"

print(label)
