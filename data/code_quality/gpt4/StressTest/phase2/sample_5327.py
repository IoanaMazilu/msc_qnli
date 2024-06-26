germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 10 ** 5
petri_dishes_premise = 36000 * 10 ** (-3)
petri_dishes_hypothesis = 36000 * 10 ** (-3)

# the hypothesis talks about the number of germs and petri dishes in the biology lab, referenced also in the premise
if germs_hypothesis <= germs_premise:
    # check if the hypothesis value contradicts the estimate of more than 'germs_premise'
    label = "contradiction"
elif petri_dishes_hypothesis != petri_dishes_premise:
    # check if the number of petri dishes in the hypothesis contradicts the number of petri dishes reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of germs
    # any number of germs greater than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
