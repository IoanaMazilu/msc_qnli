# Premise: The ratio of Gomati’s and Rashmi’s ages is 3:5 respectively.
# Hypothesis: The ratio of Gomati’s and Rashmi’s ages is less than 3:5 respectively.
# Golden Label: contradiction

gomati_rashmi_ratio_premise = 3/5
gomati_rashmi_ratio_hypothesis = 3/5  # assuming the ratio is not less than 3:5; it is equal to 3:5

# The hypothesis refers to the ratio of Gomati’s and Rashmi’s ages mentioned in the premise
if gomati_rashmi_ratio_hypothesis > gomati_rashmi_ratio_premise:
    # Check if the ratio in the hypothesis contradicts the ratio reported in the premise
    label = "contradiction"
elif gomati_rashmi_ratio_hypothesis == gomati_rashmi_ratio_premise:
    # Check if the ratio in the hypothesis exactly matches the ratio reported in the premise
    label = "entailment"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer it's neutral
    label = "neutral"

print(label)

