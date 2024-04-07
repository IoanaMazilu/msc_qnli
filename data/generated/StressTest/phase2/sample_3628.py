# Premise: David biked less than 86 1/3 miles in 2 hours and 20 minutes.
# Hypothesis: David biked 16 1/3 miles in 2 hours and 20 minutes.
# Golden Label: neutral

miles_biked_premise = 86.33
miles_biked_hypothesis = 16.33
time_biked_premise = 2.33
time_biked_hypothesis = 2.33

# the hypothesis refers to the miles biked and time spent biking mentioned in the premise
if miles_biked_hypothesis > miles_biked_premise:
    # check if the 'miles_biked_hypothesis' contradicts the upper limit of miles biked in the premise
    label = "contradiction"
elif time_biked_hypothesis != time_biked_premise:
    # check if the time of biking in the hypothesis contradicts the time of biking reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

