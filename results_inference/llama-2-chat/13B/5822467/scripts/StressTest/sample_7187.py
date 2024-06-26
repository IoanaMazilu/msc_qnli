monday_hours_premise = 5
monday_hours_hypothesis = 6
wednesday_hours_premise = 5
wednesday_hours_hypothesis = 6
friday_hours_premise = 5
friday_hours_hypothesis = 6
tuesday_hours_premise = 10
tuesday_hours_hypothesis = 10
thursday_hours_premise = 10
thursday_hours_hypothesis = 10

# the hypothesis talks about the number of hours Catherina works on each day
if monday_hours_hypothesis <= monday_hours_premise:
    # check if the hypothesis value contradicts the estimate of'monday_hours_premise'
    label = "contradiction"
elif wednesday_hours_hypothesis!= wednesday_hours_premise:
    # check if the number of hours Catherina works on Wednesday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
elif friday_hours_hypothesis!= friday_hours_premise:
    # check if the number of hours Catherina works on Friday in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Catherina works on each day
    # any number of hours greater than or equal to the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
