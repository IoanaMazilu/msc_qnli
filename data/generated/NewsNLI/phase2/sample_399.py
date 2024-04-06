# Premise: 40,000 -- Number of people who claimed the Social Security number 078-05-1120, when they found it printed on a sample insert in wallets sold at Woolworths.
# Hypothesis: 40,000 -- People who claimed SSN 078-05-1120 after finding it on a sample wallet insert.
# Golden Label: entailment

people_premise = 40000
people_hypothesis = 40000

# the hypothesis mentions the number of people who claimed the SSN, which is also referenced in the premise
if people_hypothesis != people_premise:
    # check if the number of people in the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # if the number of people from the hypothesis does not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

