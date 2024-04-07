# Premise: David biked 16 1/3 miles in 2 hours and 20 minutes.
# Hypothesis: David biked less than 86 1/3 miles in 2 hours and 20 minutes.
# Golden Label: entailment

miles_biked_premise = 16 + 1/3
miles_biked_hypothesis = 86 + 1/3
time_premise = 2 + 20/60
time_hypothesis = 2 + 20/60

# the hypothesis refers to the miles biked and the duration mentioned in the premise
if miles_biked_hypothesis <= miles_biked_premise:
    # check if the hypothesis value contradicts the 'miles_biked_premise'
    label = "contradiction"
elif time_hypothesis != time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

