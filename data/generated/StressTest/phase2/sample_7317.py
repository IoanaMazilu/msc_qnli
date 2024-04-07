# Premise: If it takes Jim 18 minutes to stretch and Cara continues to run during this time, how many minutes will it take Jim to catch up to Cara?
# Hypothesis: If it takes Jim less than 78 minutes to stretch and Cara continues to run during this time, how many minutes will it take Jim to catch up to Cara?
# Golden Label: entailment

stretch_time_premise = 18
stretch_time_hypothesis = 78

# the hypothesis refers to the stretching time of Jim mentioned in the premise
if stretch_time_premise >= stretch_time_hypothesis:
    # check if the estimate of 'stretch_time_hypothesis' contradicts the actual stretching time in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

