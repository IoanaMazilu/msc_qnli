# Premise: Plans to build a $100 million, 13-story center have sparked an emotional debate.
# Hypothesis: The project includes the construction of a $100 million, 13-story community center.
# Golden Label: entailment

cost_premise = 100000000
cost_hypothesis = 100000000
floors_premise = 13
floors_hypothesis = 13

# the hypothesis mentions the cost and the number of floors of the center, which are also referenced in the premise
# however, the hypothesis states that the center is a community center, which cannot be verified from the premise
label = "neutral"

print(label)

