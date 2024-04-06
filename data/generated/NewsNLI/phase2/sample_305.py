# Premise: Six people were injured, four seriously, according to state-run CCTV.
# Hypothesis: Six people are injured.
# Golden Label: entailment

people_injured_premise = 6
people_injured_hypothesis = 6

# the hypothesis mentions the total number of people injured, which is also referenced in the premise
if people_injured_hypothesis != people_injured_premise:
    # check if the number of injured people in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of injured people in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

