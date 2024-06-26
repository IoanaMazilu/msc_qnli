ram_krish_bhim_premise = 30
ram_krish_bhim_hypothesis = 50

# the hypothesis talks about a faster completion time than the premise
if ram_krish_bhim_hypothesis <= ram_krish_bhim_premise:
    # check if the hypothesis value contradicts the estimate of 'ram_krish_bhim_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the completion time,
    # any faster completion time than 'ram_krish_bhim_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
