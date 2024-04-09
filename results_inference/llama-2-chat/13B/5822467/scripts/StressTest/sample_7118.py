germs_premise = 4320000
germs_hypothesis = float(input("Enter the number of germs in the hypothesis: "))
petri_dishes_premise = 10800

# check if the hypothesis value contradicts the estimate of germs in the premise
if germs_hypothesis <= germs_premise:
    label = "contradiction"
elif germs_hypothesis > germs_premise:
    # the hypothesis value is greater than the premise value, so we can infer entailment
    label = "entailment"
else:
    # the hypothesis value is equal to the premise value, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
