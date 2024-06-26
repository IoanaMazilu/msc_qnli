johns_bank_premise = Rs.30
johns_bank_hypothesis = Rs.20

# the hypothesis refers to the percentage of decrease in the saving amount
if johns_bank_hypothesis <= johns_bank_premise:
    # check if the hypothesis value contradicts the percentage of decrease in the premise
    label = "contradiction"
elif johns_bank_premise!= johns_bank_hypothesis:
    # check if the percentage of decrease in the hypothesis contradicts the percentage of decrease in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
