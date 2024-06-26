rape_cases_premise = 2
rape_cases_hypothesis = 2

# the number of rape cases that the former NFL star is involved in is mentioned in both the premise and the hypothesis
if rape_cases_hypothesis != rape_cases_premise:
    # check if the number of rape cases in the hypothesis contradicts the number of rape cases mentioned in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of rape cases which means the hypothesis can be entailed from the premise
    label = "entailment"

print(label)
