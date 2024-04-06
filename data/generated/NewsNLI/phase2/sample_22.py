# Premise: Poll:Obama over 50% in Florida, Ohio and Pennsylvania.
# Hypothesis: A new poll shows Obama ahead in Ohio and two other battleground states.
# Golden Label: entailment

obama_approval_premise = 0.50
# the hypothesis does not provide a specific value, it only mentions that Obama is ahead in some states

# the hypothesis mentions Obama being ahead in Ohio and two other states, which are also mentioned in the premise
# however, the hypothesis does not provide a specific approval rating, which prevents us from confirming entailment or contradiction
label = "neutral"

print(label)
