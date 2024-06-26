# Define variables for the premise and hypothesis
us_parts_premise = 0.8
foreign_parts_hypothesis = 0.8

# Check if the hypothesis contradicts the premise
if foreign_parts_hypothesis!= us_parts_premise:
    # The hypothesis mentions a higher percentage of parts being manufactured in the U.S. than the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
