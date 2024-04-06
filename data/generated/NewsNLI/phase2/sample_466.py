# Premise: Prosecutors alleged Moustafa, a parliament member for the ruling National Democratic Party, paid el Sukkari $2 million to kill Tamim.
# Hypothesis: Prosecutors alleged Moustafa paid ex-officer el Sukkari $2M to kill Tamim.
# Golden Label: entailment

payment_premise = 2000000
payment_hypothesis = 2000000

# the hypothesis and premise both mention Moustafa paying El Sukkari the same amount to kill Tamim
if payment_premise != payment_hypothesis:
    # check if the payment value in the hypothesis contradicts the payment value in the premise
    label = "contradiction"
else:
    # if the payment value from the hypothesis does not contradict the payment value in the premise, we can infer entailment
    label = "entailment"

print(label)

