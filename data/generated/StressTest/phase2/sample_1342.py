# Premise: Goldman Limited has less than 6 Senior Managing Directors and 6 Managing Directors.
# Hypothesis: Goldman Limited has 5 Senior Managing Directors and 6 Managing Directors.
# Golden Label: neutral

senior_md_premise = 6
senior_md_hypothesis = 5
md_premise = 6
md_hypothesis = 6

# the hypothesis refers to the number of Managing Directors and Senior Managing Directors at Goldman Limited mentioned in the premise
if senior_md_hypothesis >= senior_md_premise:
    # check if the number of 'senior_md_hypothesis' contradicts the estimate of less than 'senior_md_premise' in the premise
    label = "contradiction"
elif md_hypothesis != md_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number of Managing Directors in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

