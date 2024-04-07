# Premise: City A to city B, David drove for 1 hour at 60 mph and for 3 hours at 90 mph.
# Hypothesis: City A to city B, David drove for less than 7 hour at 60 mph and for 3 hours at 90 mph.
# Golden Label: entailment

time_driven_at_60mph_premise = 1
time_driven_at_60mph_hypothesis = 7
time_driven_at_90mph_premise = 3
time_driven_at_90mph_hypothesis = 3

# the hypothesis refers to the driving times at different speeds mentioned in the premise
if time_driven_at_60mph_hypothesis < time_driven_at_60mph_premise:
    # check if the driving time at 60 mph in the hypothesis contradicts the driving time at 60 mph in the premise
    label = "contradiction"
elif time_driven_at_90mph_hypothesis != time_driven_at_90mph_premise:
    # check if the driving time at 90 mph in the hypothesis contradicts the driving time at 90 mph in the premise
    label = "contradiction"
elif time_driven_at_60mph_hypothesis > time_driven_at_60mph_premise:
    # the hypothesis suggests that the driving time at 60 mph could be more than what was mentioned in the premise
    # thus, it cannot be fully and explicitly entailed from the premise
    label = "neutral"
else:
    # if the times driven at both speeds in the hypothesis do not contradict those in the premise and also do not suggest more than what was mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

