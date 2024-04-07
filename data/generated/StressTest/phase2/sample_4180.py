# Premise: present ages of Ram and Rahim are in the ratio of more than 1:3 respectively.
# Hypothesis: present ages of Ram and Rahim are in the ratio of 4:3 respectively.
# Golden Label: neutral

# The premise provides the ratio of ages of Ram and Rahim
# The hypothesis also provides a ratio of their ages 

ram_rahim_ratio_premise = 1/3
ram_rahim_ratio_hypothesis = 4/3

# the hypothesis talks about the ratio of ages of Ram and Rahim, referenced also in the premise
if ram_rahim_ratio_hypothesis <= ram_rahim_ratio_premise:
    # check if the ratio in the hypothesis contradicts the premise's statement of the ratio being more than 1:3
    label = "contradiction"
else:
    # the premise gives only a lower limit for the ratio of ages
    # any ratio greater than 'ram_rahim_ratio_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

