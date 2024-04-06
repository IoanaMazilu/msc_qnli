# Premise: U.S. House Passes $700 Billion Rescue Plan for Failing.
# Hypothesis: U.S. Senate Approves Revised $700 Billion Rescue Bill.
# Golden Label: entailment

rescue_plan_bill_premise = 700
rescue_plan_bill_hypothesis = 700

# the hypothesis and premise both mention the amount of the rescue bill
if rescue_plan_bill_premise != rescue_plan_bill_hypothesis:
    # check if the amount of the rescue bill in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we infer entailment
    # but in this case, the premise talks about U.S. House while the hypothesis talks about U.S. Senate
    # hence, the hypothesis cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)

