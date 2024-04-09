range_premise = 60000
official_range_hypothesis = 37000

# the hypothesis mentions the estimated range of the rockets, which is also mentioned in the premise
# however, the hypothesis mentions a specific value of 37 miles, while the premise mentions a range of 60 km
# we can compare the two values to determine if the hypothesis contradicts or is neutral with respect to the premise

if official_range_hypothesis!= range_premise:
    # check if the estimated range in the hypothesis contradicts the estimated range in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer neutrality
    label = "neutral"

print(label)
