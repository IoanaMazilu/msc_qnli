# The hypothesis refers to the percentage of Level-1 college graduates in Amtek's sales staff, which is also mentioned in the premise
if level_1_graduates_premise < 15:
    # Check if the percentage of Level-1 college graduates in the premise contradicts the percentage in the hypothesis
    label = "contradiction"
else:
    # If the percentage of Level-1 college graduates in the premise does not contradict the percentage in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
