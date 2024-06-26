range_km_premise = 60
range_miles_premise = 37
range_miles_hypothesis = 37

# the hypothesis mentions the estimated range of the rockets in miles, which is also mentioned in the premise
if range_miles_hypothesis!= range_miles_premise:
    # check if the range in miles from the hypothesis contradicts the range in miles mentioned in the premise
    label = "contradiction"
else:
    # if the range in miles from the hypothesis does not contradict the range in miles mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)
