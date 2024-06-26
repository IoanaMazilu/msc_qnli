birds_premise = float(21.0)
birds_hypothesis = float(6.0)

# compare the number of birds in the premise and hypothesis
if birds_hypothesis > birds_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds in the premise
    label = "contradiction"
elif birds_hypothesis < birds_premise:
    # check if the number of birds in the hypothesis entails the number of birds in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer neutrality
    label = "neutral"

print(label)
