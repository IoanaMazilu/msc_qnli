saving_amount_premise = float(input_premise.split("due to loan payment and current balance is ")[1])
saving_amount_hypothesis = float(input_hypothesis.split("due to loan payment and current balance is ")[1])

if saving_amount_hypothesis <= saving_amount_premise:
    label = "contradiction"
elif saving_amount_hypothesis / saving_amount_premise > 1.4:
    label = "entailment"
else:
    label = "neutral"

print(label)
