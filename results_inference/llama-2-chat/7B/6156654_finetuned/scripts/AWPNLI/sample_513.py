miles_flown_premise = 256.0
flights_premise = 32.0
miles_flown_hypothesis = 8191.0

# the hypothesis refers to the number of miles Lisa flew, which are also mentioned in the premise
# compute the total number of miles Lisa flew in the premise
total_miles_flown_premise = miles_flown_premise * flights_premise

# check if the total number of miles in the hypothesis contradicts the total number of miles in the premise
if total_miles_flown_hypothesis!= total_miles_flown_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
