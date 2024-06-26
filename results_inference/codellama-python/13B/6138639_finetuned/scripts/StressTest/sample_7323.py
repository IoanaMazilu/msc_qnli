weeks_premise = 1
weeks_hypothesis = 2
average_times_premise = 3
average_times_hypothesis = 3

# the hypothesis talks about the number of times Rikki goes to the gym after a certain number of weeks, referenced also in the premise
if weeks_hypothesis < weeks_premise:
    # check if the hypothesis value contradicts the estimate of 'weeks_premise'
    label = "contradiction"
elif average_times_hypothesis!= average_times_premise:
    # check if the number of times Rikki goes to the gym in the hypothesis contradicts the number of times reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
