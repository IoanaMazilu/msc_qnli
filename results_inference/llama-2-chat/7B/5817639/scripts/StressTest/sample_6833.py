girl_count_premise = 2
boy_count_premise = 2

# the hypothesis talks about the number of girls and boys in a group, referenced also in the premise
if girl_count_hypothesis < girl_count_premise:
    # check if the hypothesis value contradicts the estimate of 'girl_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of girls
    # any number of girls less than 'girl_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
