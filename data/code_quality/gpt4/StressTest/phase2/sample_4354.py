miles_premise = 6
miles_hypothesis = 4
minutes_late_premise = 4
minutes_late_hypothesis = 4

# the hypothesis refers to the bet between Karen and Tom described in the premise
if miles_hypothesis > miles_premise:
    # check if the miles by which Karen bets to beat Tom in the hypothesis contradicts the miles mentioned in the premise
    label = "contradiction"
elif minutes_late_hypothesis != minutes_late_premise:
    # check if the minutes Karen starts late in the hypothesis contradicts the minutes mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
