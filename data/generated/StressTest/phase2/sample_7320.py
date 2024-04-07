# Premise: For the past 3 weeks, Rikki has gone to the gym an average of 2 times per week.
# Hypothesis: For the past less than 6 weeks, Rikki has gone to the gym an average of 2 times per week.
# Golden Label: entailment

weeks_premise = 3
weeks_hypothesis = 6
average_gym_visits_per_week = 2

# the hypothesis refers to the number of weeks and the average visits per week mentioned in the premise
if weeks_hypothesis <= weeks_premise:
    # check if the number of 'weeks_hypothesis' contradicts the number of weeks in the premise
    label = "contradiction"
elif average_gym_visits_per_week != average_gym_visits_per_week:
    # check if the average visits per week in the hypothesis contradicts the average visits per week reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

