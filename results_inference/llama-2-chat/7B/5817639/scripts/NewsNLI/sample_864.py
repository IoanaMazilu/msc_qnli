cases_premise = 157
deaths_premise = 101
cases_hypothesis = 3

# the hypothesis mentions the number of suspected Ebola cases in Mali, which is not mentioned in the premise
if cases_hypothesis!= cases_premise:
    # check if the number of suspected Ebola cases in the hypothesis contradicts the number of suspected cases in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
