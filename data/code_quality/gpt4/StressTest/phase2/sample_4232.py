departure_time_difference_premise = 120
departure_time_difference_hypothesis = 120

# the hypothesis talks about the departure time difference between Dan and Cara, also mentioned in the premise
if departure_time_difference_hypothesis < departure_time_difference_premise:
    # check if the hypothesis value contradicts the exact departure time difference stated in the premise
    label = "contradiction"
elif departure_time_difference_hypothesis == departure_time_difference_premise:
    # if the departure time difference in the hypothesis is equal to the one in the premise, we can infer entailment
    label = "entailment"
else:
    # any departure time difference greater than 'departure_time_difference_premise' cannot be explicitly entailed from the premise, hence is neutral
    label = "neutral"

print(label)
