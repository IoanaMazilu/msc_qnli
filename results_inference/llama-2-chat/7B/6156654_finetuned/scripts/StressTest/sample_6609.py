age_now = 18
age_then = 7

age_now_multiplier = 6
age_now_multiplier_lower_bound = 1
age_now_multiplier_upper_bound = 88

# the hypothesis talks about the age in less than 88 years, which is not explicitly mentioned in the premise
# but it can be inferred from the premise that the age in 18 years will be six times the age in 7 years
# the premise does not provide any information about the age in less than 88 years
# therefore, the hypothesis cannot be explicitly entailed from the premise
label = "neutral"

print(label)
