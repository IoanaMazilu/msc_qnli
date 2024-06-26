# define variables for the numerical entities in the premise and hypothesis
premise_percentage = 6
hypothesis_percentage = 4
premise_years = 4
hypothesis_years = 4

# check if the hypothesis value contradicts the premise value
if hypothesis_percentage < premise_percentage:
    label = "contradiction"
elif hypothesis_years!= premise_years:
    label = "neutral"
else:
    label = "entailment"

print(label)
