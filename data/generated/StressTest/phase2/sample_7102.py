# Premise: Joe drives less than 340 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Hypothesis: Joe drives 240 miles at 60 miles per hour, and then he drives the next 120 miles at 40 miles per hour.
# Golden Label: neutral

miles_60mph_premise = 340
miles_60mph_hypothesis = 240
miles_40mph_premise = 120
miles_40mph_hypothesis = 120

# the hypothesis refers to the miles driven at both 60 mph and 40 mph mentioned in the premise
if miles_60mph_hypothesis >= miles_60mph_premise:
    # check if the miles driven at 60 mph in the hypothesis contradicts the premise
    label = "contradiction"
elif miles_40mph_hypothesis != miles_40mph_premise:
    # check if the miles driven at 40 mph in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the miles driven at both speeds in the hypothesis do not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

