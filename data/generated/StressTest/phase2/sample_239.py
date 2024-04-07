# Premise: Alice deposited Rs 2 million in bank at 4% simple interest per year.
# Hypothesis: Alice deposited Rs 6 million in bank at 4% simple interest per year.
# Golden Label: contradiction

deposit_premise = 2
deposit_hypothesis = 6
interest_rate = 4  # both premise and hypothesis mention the same interest rate

# the hypothesis talks about the amount of money Alice deposited in the bank, which is also mentioned in the premise
if deposit_premise != deposit_hypothesis:
    # check if the amount of money Alice deposited in the bank according to the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the amount of money Alice deposited in the bank according to the hypothesis does not contradict the amount mentioned in the premise, we can infer entailment
    label = "entailment"

print(label)

