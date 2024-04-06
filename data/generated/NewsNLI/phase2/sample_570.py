# Premise: Pakistani officials say that about 10,000 to 15,000 militants linked to the Taliban or to al Qaeda operate in South Waziristan, a harsh terrain familiar to militants but difficult for others to navigate.
# Hypothesis: Up to 10,000 militants operating in South Waziristan, officials estimate.
# Golden Label: neutral

min_militants_premise = 10000
max_militants_premise = 15000
militants_hypothesis = 10000

# the hypothesis mentions the number of militants in South Waziristan, which is also referenced in the premise
if militants_hypothesis < min_militants_premise or militants_hypothesis > max_militants_premise:
    # check if the number of militants in the hypothesis contradicts the number of militants reported in the premise
    label = "contradiction"
else:
    # if the number of militants in the hypothesis does not contradict the number of militants in the premise, we can infer entailment
    label = "entailment"

print(label)

