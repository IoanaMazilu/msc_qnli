work_days_premise = 40
work_days_hypothesis = 20
rajesh_days_premise = 30
rajesh_days_hypothesis = 30

# the hypothesis refers to the number of days he worked and Rajesh worked, mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the number of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif rajesh_days_hypothesis!= rajesh_days_premise:
    # check if the number of Rajesh's work days in the hypothesis contradicts the number of Rajesh's work days reported in the premise
    label = "contradiction"
else:
    # the premise gives an upper limit for the number of work days
    # any number of work days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
