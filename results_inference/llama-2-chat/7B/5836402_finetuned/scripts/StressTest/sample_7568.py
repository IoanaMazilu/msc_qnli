shifts_premise = 4
hours_per_shift_premise = 12
earnings_per_hour_premise = 40
total_earnings_premise = (shifts_premise * hours_per_shift_premise) / 60

shifts_hypothesis = 4
hours_per_shift_hypothesis = 42
earnings_per_hour_hypothesis = 40
total_earnings_hypothesis = (shifts_hypothesis * hours_per_shift_hypothesis) / 60

# the hypothesis refers to the number of shifts and hours per shift, and the earnings per hour, which are also mentioned in the premise
if shifts_hypothesis!= shifts_premise or hours_per_shift_hypothesis!= hours_per_shift_premise:
    # check if the number of shifts or hours per shift in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
