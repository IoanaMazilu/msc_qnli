# define variables for the numerical entities in the premise and hypothesis
deaths_premise = 1
deaths_hypothesis = 1

# check if the number of deaths in the hypothesis contradicts the number of deaths in the premise
if deaths_hypothesis!= deaths_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
