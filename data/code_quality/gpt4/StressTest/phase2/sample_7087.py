dan_work_hours_premise = 8
dan_work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works, also mentioned in the premise
if dan_work_hours_hypothesis >= dan_work_hours_premise:
    # check if the hypothesis value contradicts the estimate of less than 'dan_work_hours_premise'
    label = "contradiction"
elif dan_work_hours_hypothesis < dan_work_hours_premise:
    # the hypothesis and premise are consistent, but the premise provides only an upper limit not a specific number 
    label = "neutral"

print(label)
