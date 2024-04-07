# Premise: city A to city B, Andrew drove for 1 hour at 50 mph and for 3 hours at 60 mph.
# Hypothesis: city A to city B, Andrew drove for more than 1 hour at 50 mph and for 3 hours at 60 mph.
# Golden Label: contradiction

time_at_50mph_premise = 1
time_at_50mph_hypothesis = 1
time_at_60mph_premise = 3
time_at_60mph_hypothesis = 3

# the hypothesis refers to the time Andrew drove at 50 mph and 60 mph
if time_at_50mph_hypothesis < time_at_50mph_premise:
    # check if the hypothesis value contradicts the exact time Andrew drove at 50 mph according to the premise
    label = "contradiction"
elif time_at_60mph_hypothesis != time_at_60mph_premise:
    # check if the time Andrew drove at 60 mph in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives an exact time for Andrew driving at 50 mph
    # any time greater than 'time_at_50mph_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

