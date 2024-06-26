premise = "Anyone wishing to remain anonymous may call 1-800-222-TIPS (8477), or text TIPLA plus your tip to 274637 (CRIMES), or visit www.LACrimeStoppers.org."
hypothesis = "Anyone with information should call (562)435-6711, or anonymously 1-800-222-TIPS (8477)"

# extract the phone numbers from the premise and hypothesis
premise_phone_numbers = ["1-800-222-TIPS (8477)", "274637 (CRIMES)"]
hypothesis_phone_numbers = ["(562)435-6711", "1-800-222-TIPS (8477)"]

# check if the phone numbers in the hypothesis are present in the premise
if hypothesis_phone_numbers[0] in premise_phone_numbers:
    # if the first phone number in the hypothesis is present in the premise, we can infer entailment
    label = "entailment"
elif hypothesis_phone_numbers[1] in premise_phone_numbers:
    # if the second phone number in the hypothesis is present in the premise, we can infer entailment
    label = "entailment"
else:
    # if neither phone number in the hypothesis is present in the premise, we can infer neutrality
    label = "neutral"

print(label)
