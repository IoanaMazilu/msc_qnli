# Premise: Warner Limited has 4 Senior Managing Directors and 6 Managing Directors.
# Hypothesis: Warner Limited has 8 Senior Managing Directors and 6 Managing Directors.
# Golden Label: contradiction

senior_md_premise = 4
senior_md_hypothesis = 8
md_premise = 6
md_hypothesis = 6

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors in Warner Limited mentioned in the premise
if senior_md_hypothesis != senior_md_premise:
    # check if the number of Senior Managing Directors in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
elif md_hypothesis != md_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

