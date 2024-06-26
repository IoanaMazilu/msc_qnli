germs_premise = 4.32 * 10 ** 6
germs_hypothesis = 4.32 * 10 ** 6
petri_dishes_premise = 10800
petri_dishes_hypothesis = 10800

# the hypothesis refers to the number of germs and Petri dishes mentioned in the premise
if germs_hypothesis > germs_premise:
    # check if the number of germs in the hypothesis contradicts the number of germs in the premise
    label = "contradiction"
elif petri_dishes_hypothesis!= petri_dishes_premise:
    # check if the number of Petri dishes in the hypothesis contradicts the number of Petri dishes in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of germs
    # any number of germs less than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
