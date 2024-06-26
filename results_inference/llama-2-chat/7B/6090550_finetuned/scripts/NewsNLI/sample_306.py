us_troops_premise = 142500
uk_troops_premise = 4100

# the hypothesis refers to the number of troops in Iraq mentioned in the premise
# we compare the number of UK troops in the hypothesis with the number of UK troops in the premise
if uk_troops_hypothesis!= uk_troops_premise:
    # if the number of UK troops in the hypothesis contradicts the number of UK troops in the premise
    label = "contradiction"
else:
    # if the number of UK troops in the hypothesis and the premise are equal
    label = "entailment"

print(label)
