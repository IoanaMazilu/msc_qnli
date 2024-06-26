miles_tuesday_premise = 1134.0
miles_thursday_premise = 1475.0
weeks_premise = 3.0
total_miles_hypothesis = 7827.0

# the hypothesis refers to the total number of miles flown, which is also referenced in the premise
# compute the total number of miles flown in a week and then in 'weeks_premise' weeks in the premise
total_miles_week_premise = miles_tuesday_premise + miles_thursday_premise
total_miles_premise = total_miles_week_premise * weeks_premise

if total_miles_hypothesis != total_miles_premise:
    # check if the number of miles in the hypothesis contradicts the number of miles from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
