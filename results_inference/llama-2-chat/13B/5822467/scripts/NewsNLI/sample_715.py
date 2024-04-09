tips_premise = "1-800-222-TIPS (8477)"
tips_hypothesis = "(562)435-6711, or anonymously 1-800-222-TIPS (8477)"

# extract the phone numbers from the premise and hypothesis
phone_premise = tips_premise.split(",")
phone_hypothesis = tips_hypothesis.split(",")

# compare the phone numbers in the premise and hypothesis
if phone_premise!= phone_hypothesis:
    # if the phone numbers in the premise and hypothesis are different, we have a contradiction
    label = "contradiction"
elif phone_premise == phone_hypothesis:
    # if the phone numbers in the premise and hypothesis are the same, we have neutrality
    label = "neutral"
else:
    # if the phone numbers in the premise and hypothesis are the same, but the wording is different, we have entailment
    label = "entailment"

print(label)
