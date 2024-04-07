# Premise: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of less than 5:4 respectively.
# Golden Label: contradiction

sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 5/4

# the hypothesis talks about the ratio of Sameer and Anand's age, referenced also in the premise
if sameer_anand_ratio_hypothesis >= sameer_anand_ratio_premise:
    # check if the ratio in the hypothesis contradicts the ratio given in the premise
    label = "contradiction"
else:
    # the ratio in the hypothesis is less than the ratio given in the premise
    # the premise supports that the ratio is exactly 5:4, not less
    label = "neutral"

print(label)

