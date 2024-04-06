# Premise: City Manager David Watkins said 10 people were taken to a hospital with respiratory problems.
# Hypothesis: 10 taken to hospital with respiratory problems, city manager says.
# Golden Label: entailment

people_hospitalized_premise = 10
people_hospitalized_hypothesis = 10

# the hypothesis mentions the number of people taken to hospital with respiratory problems, which is also referenced in the premise
if people_hospitalized_hypothesis != people_hospitalized_premise:
    # check if the number of people hospitalized in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the number of people hospitalized in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

