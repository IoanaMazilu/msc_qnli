# Define variables for the premise and hypothesis
premise_samsung_phone = 25
premise_i_phone = 70
hypothesis_samsung_phone = 75
hypothesis_i_phone = 70

# Calculate the percentage of i phone user in the premise
premise_i_phone_user = (premise_i_phone / (premise_samsung_phone + premise_i_phone)) * 100

# Calculate the percentage of i phone user in the hypothesis
hypothesis_i_phone_user = (hypothesis_i_phone / (hypothesis_samsung_phone + hypothesis_i_phone)) * 100

# Compare the percentage of i phone user in the premise and hypothesis
if hypothesis_i_phone_user <= premise_i_phone_user:
    # The hypothesis cannot be fully and explicitly entailed from the premise
    label = "neutral"
elif hypothesis_i_phone_user > premise_i_phone_user:
    # The hypothesis contradicts the premise
    label = "contradiction"
else:
    # The hypothesis is consistent with the premise
    label = "entailment"

print(label)
