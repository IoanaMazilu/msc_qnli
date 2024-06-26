economics_roster_premise = 76
economics_roster_hypothesis = 26
marketing_roster_premise = 26
marketing_roster_hypothesis = 26
statistics_roster_premise = 18
statistics_roster_hypothesis = 18

# the hypothesis refers to the number of students in each class, which is also mentioned in the premise
if economics_roster_hypothesis >= economics_roster_premise:
    # check if the number of economics class students in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif marketing_roster_hypothesis != marketing_roster_premise:
    # check if the number of marketing class students in the hypothesis contradicts the number of marketing class students reported in the premise
    label = "contradiction"
elif statistics_roster_hypothesis != statistics_roster_premise:
    # check if the number of statistics class students in the hypothesis contradicts the number of statistics class students reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
