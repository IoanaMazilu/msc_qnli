premise = "Sachin Tendulkar bough a red ferrari with a strange less than 7 digit numbered plate."
hypothesis = "Sachin Tendulkar bough a red ferrari with a strange 5 digit numbered plate."

# extract the numerical entities from the premise
plate_premise = int(premise.split(" ")[-1])

# extract the numerical entities from the hypothesis
plate_hypothesis = int(hypothesis.split(" ")[-1])

# check if the hypothesis value contradicts the premise estimate
if plate_hypothesis > plate_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
