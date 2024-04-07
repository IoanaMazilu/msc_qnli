# Premise: Chang Li has pet cockroaches that multiply at the same rate every week. The first week he had less than 7, the next week he had 10, the second week he had 20, and the fourth week he had 80.
# Hypothesis: Chang Li has pet cockroaches that multiply at the same rate every week. The first week he had 5, the next week he had 10, the second week he had 20, and the fourth week he had 80.
# Golden Label: neutral

first_week_premise = 7
first_week_hypothesis = 5
next_weeks_premise = [10, 20, 80]
next_weeks_hypothesis = [10, 20, 80]

# the hypothesis refers to the number of pet cockroaches Chang Li had each week, mentioned in the premise as well
if first_week_hypothesis >= first_week_premise:
    # check if the number of cockroaches in the first week in the hypothesis contradicts the premise
    label = "contradiction"
elif next_weeks_hypothesis != next_weeks_premise:
    # check if the numbers of cockroaches in the next weeks in the hypothesis contradict the numbers mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

