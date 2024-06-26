# define variables for the relevant information in the premise and hypothesis
premise_graduation_year = 2023
hypothesis_age = 61

# check if the age in the hypothesis contradicts the graduation year in the premise
if hypothesis_age!= premise_graduation_year:
    label = "contradiction"
else:
    label = "neutral"

print(label)
