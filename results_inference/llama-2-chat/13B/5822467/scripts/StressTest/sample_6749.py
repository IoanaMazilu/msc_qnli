butter_mixed_premise = 44
butter_mixed_hypothesis = float(input("Enter the amount of butter mixed by Raman (in kg): "))

# check if the hypothesis value contradicts the premise value
if butter_mixed_hypothesis > butter_mixed_premise:
    label = "contradiction"
elif butter_mixed_hypothesis == butter_mixed_premise:
    # the hypothesis and premise have the same value, so there is no contradiction or entailment
    label = "neutral"
else:
    # the premise gives only an estimate for the amount of butter mixed
    # any amount of butter greater than 44 kg is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
