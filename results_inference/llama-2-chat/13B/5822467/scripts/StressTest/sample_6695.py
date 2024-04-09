withdrawal_premise = 14000
withdrawal_hypothesis = less_than_14000

# define variables for the numerical entities in the premise and hypothesis
withdrawal_premise_amount = 14000
withdrawal_hypothesis_amount = withdrawal_hypothesis

# extract the numerical entities from the premise and hypothesis
if withdrawal_premise_amount > withdrawal_hypothesis_amount:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif withdrawal_hypothesis_amount!= withdrawal_premise_amount:
    # the hypothesis does not contradict the premise, but cannot be fully entailed from the premise
    label = "neutral"
else:
    # the hypothesis can be fully entailed from the premise
    label = "entailment"

print(label)
