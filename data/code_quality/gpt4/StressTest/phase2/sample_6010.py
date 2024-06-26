miles_premise = 5
miles_hypothesis = 4
late_start_premise = 4
late_start_hypothesis = 4

# the hypothesis talks about the number of miles and minutes late in a bet, referenced also in the premise
if miles_hypothesis > miles_premise:
    # check if the hypothesis value contradicts the premise's estimate of less than 'miles_premise'
    label = "contradiction"
elif late_start_hypothesis != late_start_premise:
    # check if the number of minutes late in the hypothesis contradicts the number of minutes late reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
