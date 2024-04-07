# Premise: Edward earns $7.00 per hour for the first less than 70 hours he works per week, and twice this rate for overtime.
# Hypothesis: Edward earns $7.00 per hour for the first 40 hours he works per week, and twice this rate for overtime.
# Golden Label: neutral

regular_hours_premise = 70
regular_hours_hypothesis = 40
rate_regular_hours = 7.00

# the hypothesis talks about the number of regular hours Edward works per week, compared to the premise
if regular_hours_hypothesis > regular_hours_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'regular_hours_premise'
    label = "contradiction"
elif regular_hours_hypothesis == regular_hours_premise:
    # check if the regular hours worked in the hypothesis matches the premise, which is not possible as per the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of regular hours
    # any number of hours lesser than 'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

