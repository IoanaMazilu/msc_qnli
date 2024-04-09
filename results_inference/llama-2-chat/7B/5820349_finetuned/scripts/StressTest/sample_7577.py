work_days_premise = 25
work_days_hypothesis = 25

# the hypothesis talks about the number of days Sreedhar and Sravan can do a work, referenced also in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of days
    # any number of days greater than 'work_days_premise' contradicts the premise
    label = "contradiction"

print(label)
