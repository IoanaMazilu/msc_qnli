# Premise: Rajat, Vikas and Abhishek are submitting questions in the ratio less than 8:3:2.
# Hypothesis: Rajat, Vikas and Abhishek are submitting questions in the ratio 7:3:2.
# Golden Label: neutral

rajat_vikas_abhishek_premise = [8, 3, 2]
rajat_vikas_abhishek_hypothesis = [7, 3, 2]

# The hypothesis refers to the ratio of questions submitted by Rajat, Vikas, and Abhishek, also mentioned in the premise
if rajat_vikas_abhishek_hypothesis[0] >= rajat_vikas_abhishek_premise[0]:
    # Check if the ratio for Rajat in the hypothesis contradicts the estimate of less than 'rajat_vikas_abhishek_premise[0]'
    label = "contradiction"
elif rajat_vikas_abhishek_hypothesis[1] != rajat_vikas_abhishek_premise[1] or rajat_vikas_abhishek_hypothesis[2] != rajat_vikas_abhishek_premise[2]:
    # Check if the ratios for Vikas and Abhishek in the hypothesis contradict the ratios for Vikas and Abhishek in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the ratio of questions submitted by Rajat
    # The exact ratio in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

