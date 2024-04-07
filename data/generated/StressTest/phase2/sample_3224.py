# Premise: 4200 among John, Jose & Binoy in the ration 2:4:6.
# Hypothesis: 7200 among John, Jose & Binoy in the ration 2:4:6.
# Golden Label: contradiction

total_amount_premise = 4200
total_amount_hypothesis = 7200

# the hypothesis talks about the same ratio as the premise, but with a different total amount
if total_amount_hypothesis != total_amount_premise:
    # check if the total amount in the hypothesis contradicts the total amount reported in the premise
    label = "contradiction"
else:
    # if the total amounts in the hypothesis and in the premise are the same, we can infer entailment
    label = "entailment"

print(label)

