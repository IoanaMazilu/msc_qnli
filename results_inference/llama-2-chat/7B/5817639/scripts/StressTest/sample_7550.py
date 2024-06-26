saving_premise = float(input_premise.split("'s saving amount is decreased ")[1].strip())
saving_hypothesis = float(input_hypothesis.split("'s saving amount is decreased ")[1].strip())

# the hypothesis talks about the percentage of decrease in saving amount, which is also mentioned in the premise
if saving_hypothesis <= saving_premise:
    # check if the hypothesis value contradicts the estimate of percentage of decrease in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of decrease, which is consistent with the hypothesis
    label = "neutral"

print(label)
