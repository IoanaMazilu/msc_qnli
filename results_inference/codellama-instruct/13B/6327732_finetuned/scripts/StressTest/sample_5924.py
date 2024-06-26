# define variables for the numerical entities in the premise and hypothesis
trip_to_beach_premise = 1/2
trip_to_beach_hypothesis = 4/2

# check if the hypothesis value contradicts the premise value
if trip_to_beach_hypothesis <= trip_to_beach_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
