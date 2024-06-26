plate_digits_premise = 7
plate_digits_hypothesis = 5

if plate_digits_hypothesis > plate_digits_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif plate_digits_hypothesis < plate_digits_premise:
    # check if the hypothesis value is consistent with the premise
    label = "neutral"

print(label)
