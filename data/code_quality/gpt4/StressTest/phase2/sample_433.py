reinvestment_premise = 35000
reinvestment_hypothesis = 35000
reinvestment_months_premise = 4
reinvestment_months_hypothesis = 8

# the hypothesis talks about the amount and duration of Reena's investment, which are also mentioned in the premise
if reinvestment_hypothesis != reinvestment_premise:
    # check if the amount of Reena's investment in the hypothesis contradicts the amount of Reena's investment in the premise
    label = "contradiction"
elif reinvestment_months_hypothesis <= reinvestment_months_premise:
    # check if the duration of Reena's investment in the hypothesis contradicts the estimate of more than 'reinvestment_months_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of Reena's investment
    # any duration longer than 'reinvestment_months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
