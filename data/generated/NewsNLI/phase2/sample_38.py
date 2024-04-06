# Premise: Nadya Suleman, a single mother of 14 children, has set up a Web site asking for donations.
# Hypothesis: Nadya Suleman has created Web site to solicit donations to help support 14 kids.
# Golden Label: entailment

children_premise = 14
children_hypothesis = 14

# the hypothesis mentions the number of children Nadya Suleman has, which is also mentioned in the premise
if children_hypothesis != children_premise:
    # check if the number of children in the hypothesis contradicts the number of children reported in the premise
    label = "contradiction"
else:
    # if the number of children in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

