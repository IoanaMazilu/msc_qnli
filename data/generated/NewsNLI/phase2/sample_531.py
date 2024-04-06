# Premise: Since mid-August, the Centers for Disease Control and Prevention has confirmed more than 100 cases of Enterovirus D68 in 12 states:Alabama, Colorado, Illinois, Indiana, Iowa, Kansas, Kentucky, Louisiana, Missouri, Montana, New York and Oklahoma.
# Hypothesis: Alabama has also confirmed four cases of Enterovirus D68.
# Golden Label: neutral

cases_premise = 100
cases_alabama_hypothesis = 4

# the hypothesis mentions the number of confirmed cases of Enterovirus D68 in Alabama
# the premise mentions the total number of confirmed cases in 12 states, including Alabama
if cases_alabama_hypothesis > cases_premise:
    # check if the number of cases in Alabama from the hypothesis contradicts the total number of cases in the premise
    label = "contradiction"
else:
    # if the number of cases in Alabama does not exceed the total number of cases, we infer entailment
    label = "entailment"

print(label)

