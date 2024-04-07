# Premise: present ages of Ram and Rahim are in the ratio of 4:3 respectively.
# Hypothesis: present ages of Ram and Rahim are in the ratio of more than 4:3 respectively.
# Golden Label: contradiction

ram_rahim_ratio_premise = 4/3
ram_rahim_ratio_hypothesis = 4/3

# the hypothesis talks about the ratio of ages of Ram and Rahim, referenced also in the premise
if ram_rahim_ratio_hypothesis <= ram_rahim_ratio_premise:
    # check if the hypothesis value contradicts the ratio of ages provided in the premise
    label = "contradiction"
elif ram_rahim_ratio_hypothesis > ram_rahim_ratio_premise:
    # if the hypothesis ratio is more than the premise ratio, it can be inferred as entailment
    label = "entailment"
else:
    # if the hypothesis ratio does not contradict the premise ratio, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

