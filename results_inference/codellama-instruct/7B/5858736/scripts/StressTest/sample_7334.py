# Define variables for the premise and hypothesis
premise_samsung_phone = 75
premise_i_phone = 70
hypothesis_samsung_phone = 85

# Calculate the percentage of i phone user
i_phone_user = (premise_i_phone / (premise_samsung_phone + premise_i_phone)) * 100

# Check if the hypothesis is entailed from the premise
if i_phone_user >= 25:
    label = "entailment"
elif i_phone_user < 25:
    label = "contradiction"
else:
    label = "neutral"

print(label)
