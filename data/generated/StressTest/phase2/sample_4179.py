# Premise: present ages of Ram and Rahim are in the ratio of 4:3 respectively.
# Hypothesis: present ages of Ram and Rahim are in the ratio of more than 1:3 respectively.
# Golden Label: entailment

ram_rahim_ratio_premise = 4/3
ram_rahim_ratio_hypothesis = 1/3

# the hypothesis talks about the ratio of ages of Ram and Rahim, similarly mentioned in the premise
if ram_rahim_ratio_hypothesis >= ram_rahim_ratio_premise:
    # check if the ratio in hypothesis contradicts the ratio given in the premise
    label = "contradiction"
elif ram_rahim_ratio_hypothesis < ram_rahim_ratio_premise:
    # check if the ratio in hypothesis entails the ratio given in the premise
    label = "entailment"
else:
    # if the hypothesis ratio and estimate do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)

