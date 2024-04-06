# Premise: The Tazewell County Sheriff's Office can be reached at 309-346-4141.
# Hypothesis: Have a tip? Call the Tazewell County Sheriff's Office at 309-346-4141.
# Golden Label: entailment

phone_number_premise = 3093464141
phone_number_hypothesis = 3093464141

# the hypothesis mentions the phone number of Tazewell County Sheriff's Office, which is also mentioned in the premise
if phone_number_hypothesis != phone_number_premise:
    # check if the phone number in the hypothesis contradicts the phone number in the premise
    label = "contradiction"
else:
    # if the phone number in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)

