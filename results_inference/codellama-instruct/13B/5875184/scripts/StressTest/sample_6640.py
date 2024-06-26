ram_krish_work_premise = 20
ram_krish_work_hypothesis = 40
bhim_work_premise = 20
bhim_work_hypothesis = 40

# the hypothesis refers to the number of days it takes for Ram and Krish to complete the work
if ram_krish_work_hypothesis <= ram_krish_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ram_krish_work_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days it takes for Ram and Krish to complete the work
    # any number of days greater than 'ram_krish_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
