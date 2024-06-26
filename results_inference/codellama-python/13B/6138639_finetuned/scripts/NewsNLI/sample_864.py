cases_premise = 157
deaths_premise = 101
cases_hypothesis = 3

# the hypothesis mentions the number of suspected cases in Mali, which is not mentioned in the premise
# therefore, we cannot infer entailment, contradiction, or neutrality
label = "neutral"

print(label)
