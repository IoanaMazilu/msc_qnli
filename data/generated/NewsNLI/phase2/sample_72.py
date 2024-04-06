# Premise: Cholera has ravaged Zimbabwe, causing nearly 800 deaths and infecting more than 16,000 people, the World Health Organization says.
# Hypothesis: WHO says cholera outbreak has killed almost 800, infected 16,000.
# Golden Label: entailment

deaths_premise = 800
infected_premise = 16000
deaths_hypothesis = 800
infected_hypothesis = 16000

# the hypothesis mentions the number of deaths and infected people from cholera in Zimbabwe, which are also mentioned in the premise
if deaths_hypothesis != deaths_premise:
    # check if the number of deaths in the hypothesis contradicts the number of deaths reported in the premise
    label = "contradiction"
elif infected_hypothesis != infected_premise:
    # check if the number of infected people from the hypothesis contradicts the number of infected people in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

