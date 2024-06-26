stations_premise = 28
stations_hypothesis = 18

# the hypothesis refers to the number of stations between Hyderabad and Bangalore mentioned in the premise
if stations_hypothesis >= stations_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif stations_hypothesis < stations_premise:
    # check if the hypothesis value is less than the premise value
    # this is a neutral case
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it is entailed by the premise
    label = "entailment"

print(label)
