time_travel_wish_premise = 0.09
time_travel_wish_hypothesis = 0.1

# the hypothesis mentions the proportion of people who would like to be able to time travel, which is also mentioned in the premise
if time_travel_wish_hypothesis > time_travel_wish_premise:
    # check if the proportion in the hypothesis contradicts the proportion reported in the premise
    label = "contradiction"
elif time_travel_wish_hypothesis < time_travel_wish_premise:
    # check if the proportion in the hypothesis is less than the proportion reported in the premise
    label = "contradiction"
else:
    # if the proportion in the hypothesis does not contradict the proportion in the premise, we can infer entailment
    label = "entailment"

print(label)
