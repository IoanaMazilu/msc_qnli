ram_work_premise = 30
ram_work_hypothesis = 50

# the hypothesis refers to the number of days taken by Ram, Krish and Bhim to complete a work
if ram_work_hypothesis <= ram_work_premise:
    # check if the hypothesis value contradicts the estimate of 'ram_work_premise'
    label = "contradiction"
elif ram_work_hypothesis > 2 * ram_work_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the number of days taken by Ram, Krish and Bhim
    # any number of days greater than 'ram_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
