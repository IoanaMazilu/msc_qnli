# Premise: WASHINGTON (CNN) -- Washington souvenirs worth $100,000 -- including images of the Capitol dome and printings of the U.S. Constitution -- are locked in storage, blocked from sale in the new U.S. Capitol Visitors Center because the items are made in China.
# Hypothesis: House committee bars sale of $100,000 in souvenirs because of their origin.
# Golden Label: neutral

souvenirs_value_premise = 100000
souvenirs_value_hypothesis = 100000

# the hypothesis mentions the value of the souvenirs, which is also mentioned in the premise
if souvenirs_value_hypothesis != souvenirs_value_premise:
    # check if the value of the souvenirs in the hypothesis contradicts the value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)

