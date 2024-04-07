# Premise: Jones gave 40% of the money he had to his wife.
# Hypothesis: Jones gave more than 10% of the money he had to his wife.
# Golden Label: entailment

money_given_premise = 40
money_given_hypothesis = 10

# the hypothesis talks about the percentage of money Jones gave to his wife, stated also in the premise
if money_given_premise <= money_given_hypothesis:
    # check if the hypothesis value contradicts the 'money_given_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)

