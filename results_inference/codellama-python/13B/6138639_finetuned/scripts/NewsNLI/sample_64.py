# The premise mentions the suspect's name and age, and the number of charges
# The hypothesis mentions the suspect's name and the number of deaths

suspect_age_premise = 33
suspect_age_hypothesis = 33
deaths_hypothesis = 6

# The hypothesis mentions the suspect's name and the number of deaths, which are also mentioned in the premise
# However, the hypothesis does not mention the number of charges, which is mentioned in the premise
label = "neutral"

print(label)
