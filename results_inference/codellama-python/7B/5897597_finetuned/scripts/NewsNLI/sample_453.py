range_km_premise = 60
range_miles_hypothesis = 37

# the hypothesis mentions the range of the rockets in miles, which is also referenced in the premise
# convert miles to km for comparison
range_miles_premise = range_km_premise / 1.60934

if range_miles_hypothesis!= range_miles_premise:
    # check if the range in miles from the hypothesis contradicts the range in miles reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
