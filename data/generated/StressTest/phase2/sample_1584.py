# Premise: 20000 after 8 months, Sravan advances Rs.
# Hypothesis: less than 30000 after 8 months, Sravan advances Rs.
# Golden Label: entailment

advance_premise = 20000
advance_hypothesis = 30000

# the hypothesis refers to the amount advanced by Sravan after 8 months, as mentioned in the premise
if advance_premise >= advance_hypothesis:
    # check if the premise contradicts the less than 'advance_hypothesis' statement in the hypothesis
    label = "contradiction"
else:
    # the premise confirms the hypothesis that the advanced amount is less than 'advance_hypothesis'
    label = "entailment"

print(label)

