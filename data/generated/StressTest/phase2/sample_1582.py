# Premise: City A to city B, Michael drove for less than 4 hour at 80 mph and for 3 hours at 60 mph.
# Hypothesis: City A to city B, Michael drove for 1 hour at 80 mph and for 3 hours at 60 mph.
# Golden Label: neutral

drive_80mph_premise = 4
drive_80mph_hypothesis = 1
drive_60mph_premise = 3
drive_60mph_hypothesis = 3

# the hypothesis talks about the time Michael drove at certain speeds, which is also mentioned in the premise
if drive_80mph_hypothesis > drive_80mph_premise:
    # check if the hypothesis value contradicts the estimate of less than 'drive_80mph_premise'
    label = "contradiction"
elif drive_60mph_hypothesis != drive_60mph_premise:
    # check if the time Michael drove at 60 mph in the hypothesis contradicts that reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values are consistent with the premise ones, we can infer entailment
    label = "entailment"

print(label)

