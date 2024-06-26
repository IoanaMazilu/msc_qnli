premise = "Arun purchased less than 40 kg of wheat at the rate of Rs."
hypothesis = "Arun purchased 30 kg of wheat at the rate of Rs."

# define variables for the numerical entities in the premise and hypothesis
kg_wheat_premise = float(premise.split()[1])
kg_wheat_hypothesis = float(hypothesis.split()[1])

# extract the numerical values from the premise and hypothesis
if kg_wheat_premise <= kg_wheat_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'kg_wheat_premise'
    label = "contradiction"
elif kg_wheat_hypothesis!= kg_wheat_premise:
    # check if the number of kg of wheat in the hypothesis contradicts the number of kg of wheat reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
