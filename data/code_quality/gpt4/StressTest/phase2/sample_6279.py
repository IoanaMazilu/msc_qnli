rajat_vikas_abhishek_premise = (7, 3, 2)
rajat_vikas_abhishek_hypothesis = (8, 3, 2)

# the hypothesis refers to the ratio of questions submitted by Rajat, Vikas and Abhishek, mentioned also in the premise
if rajat_vikas_abhishek_hypothesis[0] <= rajat_vikas_abhishek_premise[0]:
    # check if the hypothesis value contradicts the premise's ratio for Rajat
    label = "contradiction"
elif rajat_vikas_abhishek_hypothesis[1:] != rajat_vikas_abhishek_premise[1:]:
    # check if the ratios for Vikas and Abhishek in the hypothesis contradict the premise's ratios
    label = "contradiction"
else:
    # premise's ratio is less than the hypothesis's ratio for Rajat, and the ratios for Vikas and Abhishek are the same
    # thus, the hypothesis does not contradict the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
