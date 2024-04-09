peanuts_premise = float(input("Enter the number of peanuts in the box (premise): "))
peanuts_hypothesis = float(input("Enter the number of peanuts in the box (hypothesis): "))

# Check if the hypothesis value contradicts the premise estimate
if peanuts_hypothesis < peanuts_premise:
    label = "contradiction"
elif peanuts_hypothesis > peanuts_premise:
    # Check if the hypothesis value entails the premise estimate
    if peanuts_hypothesis - peanuts_premise > 12:
        label = "entailment"
    else:
        label = "neutral"
else:
    label = "neutral"

print(label)
