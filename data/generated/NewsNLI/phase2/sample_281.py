# Premise: 8 -- Number of Ohioans who have been elected president.
# Hypothesis: 8 -- Number of Buckeye State residents who have been elected president.
# Golden Label: entailment

presidents_premise = 8
presidents_hypothesis = 8

# the hypothesis mentions the number of presidents from Ohio (also known as the Buckeye State), which is also referenced in the premise
if presidents_hypothesis != presidents_premise:
    # check if the number of presidents in the hypothesis contradicts the number of presidents reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

