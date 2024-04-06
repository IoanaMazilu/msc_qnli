# Premise: A former executive of Digital Equipment Corp. and two others pleaded guilty Tuesday to siphoning nearly $300,000 from the computer company.
# Hypothesis: A former executive of Digital Equipment Corp. siphoned nearly $300,000 from the company.
# Golden Label: entailment

money_siphoned_premise = 300000
money_siphoned_hypothesis = 300000

# the hypothesis talks about the money siphoned by an executive which is also mentioned in the premise
if money_siphoned_hypothesis != money_siphoned_premise:
    # check if the amount siphoned in the hypothesis contradicts the amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

