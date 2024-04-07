# Premise: city A to city B, Andrew drove for 1 hour at 50 mph and for 3 hours at 60 mph.
# Hypothesis: city A to city B, Andrew drove for less than 2 hour at 50 mph and for 3 hours at 60 mph.
# Golden Label: entailment

driving_hours_50mph_premise = 1
driving_hours_50mph_hypothesis = 2
driving_hours_60mph_premise = 3
driving_hours_60mph_hypothesis = 3

# the hypothesis refers to the driving hours at different speeds mentioned in the premise
if driving_hours_50mph_hypothesis <= driving_hours_50mph_premise:
    # check if the hypothesis value contradicts the driving hours at 50 mph in the premise
    label = "contradiction"
elif driving_hours_60mph_hypothesis != driving_hours_60mph_premise:
    # check if the driving hours at 60 mph in the hypothesis contradicts the driving hours at 60 mph reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

