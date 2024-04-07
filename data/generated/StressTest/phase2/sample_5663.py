# Premise: City A to city B, David drove for 1 hour at 60 mph and for 3 hours at 90 mph.
# Hypothesis: City A to city B, David drove for less than 1 hour at 60 mph and for 3 hours at 90 mph.
# Golden Label: contradiction

drive_hours_60mph_premise = 1
drive_hours_60mph_hypothesis = 1
drive_hours_90mph_premise = 3
drive_hours_90mph_hypothesis = 3

# The hypothesis refers to the hours David drove at 60 mph and 90 mph, which are also mentioned in the premise
if drive_hours_60mph_hypothesis >= drive_hours_60mph_premise:
    # Check if the hypothesis value contradicts the premise of David driving for 1 hour at 60 mph
    label = "contradiction"
elif drive_hours_90mph_hypothesis != drive_hours_90mph_premise:
    # Check if the hours David drove at 90 mph in the hypothesis contradicts the hours mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

