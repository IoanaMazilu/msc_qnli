# Premise: Present ages of Sameer and Anand are in the ratio of 5:4 respectively.
# Hypothesis: Present ages of Sameer and Anand are in the ratio of 8:4 respectively.
# Golden Label: contradiction

sameer_anand_ratio_premise = 5/4
sameer_anand_ratio_hypothesis = 8/4

# the hypothesis proposes a different ratio of ages for Sameer and Anand than the premise
if sameer_anand_ratio_hypothesis != sameer_anand_ratio_premise:
    # if the ratios do not match, we have a contradiction
    label = "contradiction"
else:
    # if the ratios match, we have entailment
    label = "entailment"

print(label)

