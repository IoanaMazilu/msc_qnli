 exports_premise = 1.44e12
 exports_hypothesis = 1.05e10

# compare the values of the hypothesis with the premise
if exports_hypothesis!= exports_premise:
    # check if the value of exports in the hypothesis contradicts the value from the premise
    label = "contradiction"
elif exports_hypothesis < exports_premise:
    # check if the value of exports in the hypothesis is less than the value from the premise
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, we can infer neutrality
    label = "neutral"

print(label)
