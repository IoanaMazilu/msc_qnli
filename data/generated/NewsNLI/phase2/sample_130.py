# Premise: It also caused the cancellation of at least 486 flights at Denver International Airport.
# Hypothesis: 486 flights are canceled at Denver's airport.
# Golden Label: entailment

flights_cancelled_premise = 486
flights_cancelled_hypothesis = 486

# the hypothesis mentions the number of cancelled flights at Denver's airport, which is also referenced in the premise
if flights_cancelled_hypothesis != flights_cancelled_premise:
    # check if the number of cancelled flights in the hypothesis contradicts the number of cancelled flights reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

