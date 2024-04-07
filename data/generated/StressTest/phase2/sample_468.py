# Premise: If an outfit consists of 1 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Hypothesis: If an outfit consists of less than 3 shirt, 1 pair of jeans, and 1 pair of sneakers, how many different outfits does Jordan have?
# Golden Label: entailment

shirt_premise = 1
shirt_hypothesis = 3

# the hypothesis refers to the number of shirts in an outfit mentioned in the premise
if shirt_premise >= shirt_hypothesis:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
elif shirt_premise < shirt_hypothesis:
    # the premise does not provide enough information to explicitly entail the hypothesis
    label = "neutral"

print(label)

