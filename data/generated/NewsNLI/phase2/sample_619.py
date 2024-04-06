# Premise: Delhi (CNN) An international human rights group is calling for an independent investigation of the killings by police of 20 suspected red sandalwood smugglers in southeastern India.
# Hypothesis: Amnesty calls for probe of India police shooting of 20 suspected smugglers.
# Golden Label: neutral

killings_premise = 20
killings_hypothesis = 20

# the hypothesis mentions the number of suspected smugglers killed by police in India, which is also mentioned in the premise
if killings_hypothesis != killings_premise:
    # check if the number of killings in the hypothesis contradicts the number of killings reported in the premise
    label = "contradiction"
else:
    # if the number of killings in the hypothesis does not contradict the number in the premise, we can infer entailment
    label = "entailment"

print(label)

