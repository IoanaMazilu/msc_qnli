# Premise: After less than 2 more week, the average number of times Rikki goes to the gym increases to 3 times per week.
# Hypothesis: After 1 more week, the average number of times Rikki goes to the gym increases to 3 times per week.
# Golden Label: neutral

weeks_premise = 2
weeks_hypothesis = 1
gym_frequency_premise = 3
gym_frequency_hypothesis = 3

# the hypothesis refers to the number of weeks and frequency of gym visits mentioned in the premise
if weeks_hypothesis > weeks_premise:
    # check if the hypothesis value contradicts the estimate of less than 'weeks_premise'
    label = "contradiction"
elif gym_frequency_hypothesis != gym_frequency_premise:
    # check if the frequency of gym visits in the hypothesis contradicts the frequency reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

