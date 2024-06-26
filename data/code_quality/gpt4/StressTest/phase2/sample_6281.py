# Define the ratio values for each individual in the premise and hypothesis
rajat_ratio_premise = 7
vikas_ratio_premise = 3
abhishek_ratio_premise = 2

rajat_ratio_hypothesis = 5
vikas_ratio_hypothesis = 3
abhishek_ratio_hypothesis = 2

# Compare the ratio values of each individual in the premise and hypothesis
if rajat_ratio_premise != rajat_ratio_hypothesis or vikas_ratio_premise != vikas_ratio_hypothesis or abhishek_ratio_premise != abhishek_ratio_hypothesis:
    label = "contradiction"
else:
    label = "entailment"

print(label)
