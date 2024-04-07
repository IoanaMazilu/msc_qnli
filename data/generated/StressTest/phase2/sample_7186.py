# Premise: Catherina works more than 2 hours per day on Monday, Wednesday and Friday, and 10 hours per day on Tuesday and Thursday.
# Hypothesis: Catherina works 5 hours per day on Monday, Wednesday and Friday, and 10 hours per day on Tuesday and Thursday.
# Golden Label: neutral

work_hours_mwf_premise = 2
work_hours_mwf_hypothesis = 5
work_hours_tt_premise = 10
work_hours_tt_hypothesis = 10

# the hypothesis talks about the work hours of Catherina on the same days mentioned in the premise
if work_hours_mwf_hypothesis <= work_hours_mwf_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_hours_mwf_premise' on Monday, Wednesday and Friday
    label = "contradiction"
elif work_hours_tt_hypothesis != work_hours_tt_premise:
    # check if the work hours on Tuesday and Thursday in the hypothesis contradicts the work hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the work hours on Monday, Wednesday and Friday
    # any number of hours greater than 'work_hours_mwf_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

