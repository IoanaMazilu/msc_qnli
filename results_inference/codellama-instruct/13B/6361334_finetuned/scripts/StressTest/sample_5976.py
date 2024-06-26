germs_premise = 0.036 * 10 ** 5
germs_hypothesis = 0.036 * 80 ** 5
petri_dishes_premise = 75000 * 10 ** (-3)
petri_dishes_hypothesis = 75000 * 10 ** (-3)

# the hypothesis refers to the number of germs in the biology lab, mentioned in the premise
if germs_hypothesis >= germs_premise:
    # check if the hypothesis value contradicts the number of germs in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of germs
    # any number of germs less than 'germs_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
