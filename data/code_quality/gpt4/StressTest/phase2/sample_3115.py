corn_dinner_premise = 300
corn_dinner_hypothesis = 200

# the hypothesis talks about the amount of corn Sandy ate for dinner, also referenced in the premise
if corn_dinner_hypothesis >= corn_dinner_premise:
    # check if the amount of corn eaten for dinner in the hypothesis contradicts the premise's value of less than 'corn_dinner_premise'
    label = "contradiction"
elif corn_dinner_hypothesis == corn_dinner_premise:
    # check if the amount of corn eaten for dinner in the hypothesis exactly equals the value in the premise
    label = "contradiction"
else:
    # if the amount of corn in the hypothesis is less than 'corn_dinner_premise' and does not exactly equal 'corn_dinner_premise',
    # it is consistent with the premise and can be explicitly entailed from the premise
    label = "entailment"

print(label)
