mary_work_days_premise = 360
mary_work_days_hypothesis = 160
rose_work_days_premise = 240
rose_work_days_hypothesis = 240

# the hypothesis refers to the number of days Mary and Rose take to complete a piece of work, mentioned in the premise
if mary_work_days_hypothesis >= mary_work_days_premise:
    # check if the number of days Mary takes to complete a piece of work in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif rose_work_days_hypothesis != rose_work_days_premise:
    # check if the number of days Rose takes to complete a piece of work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Mary takes to complete a piece of work
    # any number of days less than 'mary_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
