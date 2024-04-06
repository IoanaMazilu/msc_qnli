# Premise: The United Nations estimates that 60 percent of the people it needs to reach with emergency assistance live in areas controlled by Al-Shabaab.
# Hypothesis: U.N. estimates 60 percent of people who need aid live in militant-controlled areas.
# Golden Label: entailment

people_in_need_premise = 0.60
people_in_need_hypothesis = 0.60

# the hypothesis mentions the percentage of people who need aid and live in militant-controlled areas, which is also referenced in the premise
if people_in_need_hypothesis != people_in_need_premise:
    # check if the percentage in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
