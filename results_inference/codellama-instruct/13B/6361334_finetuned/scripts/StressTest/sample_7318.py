stretch_time_premise = 78
stretch_time_hypothesis = 18
catch_up_time_premise = stretch_time_premise - catch_up_time_hypothesis
catch_up_time_hypothesis = stretch_time_hypothesis - catch_up_time_hypothesis

# the hypothesis refers to the time it takes for Jim to stretch and the time it takes for Jim to catch up to Cara
if stretch_time_hypothesis <= stretch_time_premise:
    # check if the hypothesis value contradicts the estimate of less than'stretch_time_premise'
    label = "contradiction"
elif catch_up_time_hypothesis!= catch_up_time_premise:
    # check if the number of minutes it takes for Jim to catch up to Cara in the hypothesis contradicts the number of minutes reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
