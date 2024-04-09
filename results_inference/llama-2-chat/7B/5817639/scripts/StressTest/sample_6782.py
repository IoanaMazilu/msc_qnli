x_per_hour_premise = 0 # initialize variable for premise
x_per_hour_hypothesis = 0 # initialize variable for hypothesis

# the hypothesis talks about the pay per hour for a week, referenced also in the premise
if x_per_hour_hypothesis <= x_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'x_per_hour_premise'
    label = "contradiction"
elif x_per_hour_hypothesis > 2 * x_per_hour_premise:
    # check if the number of additional hours worked in the hypothesis contradicts the number of additional hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
