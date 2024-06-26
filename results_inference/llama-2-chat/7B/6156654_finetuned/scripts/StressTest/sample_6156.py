sameer_age_ratio = 5/4
anand_age_ratio = 5/4

# the hypothesis refers to the same ratios of ages of Sameer and Anand
if sameer_age_ratio!= anand_age_ratio:
    # if the ratios of ages of Sameer and Anand do not match, it's a contradiction
    label = "contradiction"
elif sameer_age_ratio < 3/4 or anand_age_ratio < 3/4:
    # if the ratios of ages of Sameer and Anand are less than 3:4, it's a contradiction
    label = "contradiction"
else:
    # if the ratios of ages of Sameer and Anand are greater than or equal to 3:4, it's entailment
    label = "entailment"

print(label)
