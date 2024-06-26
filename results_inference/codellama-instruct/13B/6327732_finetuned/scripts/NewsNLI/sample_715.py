premise_phone_number = "1-800-222-TIPS (8477)"
hypothesis_phone_number = "(562)435-6711"

# the hypothesis mentions a different phone number for reporting tips, which cannot be entailed from the premise
if hypothesis_phone_number!= premise_phone_number:
    label = "contradiction"
else:
    label = "neutral"

print(label)
