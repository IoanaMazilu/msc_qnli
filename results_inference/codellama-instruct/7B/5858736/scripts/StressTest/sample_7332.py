# Define variables for the premise and hypothesis
premise_samsung_phone = 0.75
premise_i_phone = 0.25
hypothesis_samsung_phone = 0.85

# Calculate the percentage of i phone user in the premise
premise_i_phone_user = 1 - premise_samsung_phone

# Calculate the percentage of i phone user in the hypothesis
hypothesis_i_phone_user = 1 - hypothesis_samsung_phone

# Check if the hypothesis values contradict the premise values
if premise_i_phone_user!= hypothesis_i_phone_user:
    label = "contradiction"
elif premise_samsung_phone > hypothesis_samsung_phone:
    label = "entailment"
else:
    label = "neutral"

print(label)
