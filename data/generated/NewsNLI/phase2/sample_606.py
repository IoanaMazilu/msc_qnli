# Premise: (CNN) -- More than 700 infants and 40 health care workers have been exposed to tuberculosis, commonly called TB, at a hospital in El Paso, Texas, according to the city's Department of Public Health.
# Hypothesis: 706 infants and 43 workers were exposed to TB.
# Golden Label: neutral

infants_exposed_premise = 700
infants_exposed_hypothesis = 706
workers_exposed_premise = 40
workers_exposed_hypothesis = 43

# the hypothesis mentions the exact number of infants and workers exposed to TB
# while the premise only mentions approximate numbers (more than 700 infants and 40 workers)
if infants_exposed_hypothesis <= infants_exposed_premise:
    # check if the number of infants exposed to TB in the hypothesis contradicts the number in the premise
    label = "contradiction"
elif workers_exposed_hypothesis <= workers_exposed_premise:
    # check if the number of workers exposed to TB in the hypothesis contradicts the number in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

