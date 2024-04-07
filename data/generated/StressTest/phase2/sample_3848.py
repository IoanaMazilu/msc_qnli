# Premise: If Grady and Howard are among those 6 friends but can never sit next to each other, how many 6-person seating arrangements are possible?
# Hypothesis: If Grady and Howard are among those 5 friends but can never sit next to each other, how many 6-person seating arrangements are possible?
# Golden Label: contradiction

friends_premise = 6
friends_hypothesis = 5

# The hypothesis and premise both specify the number of friends involved in seating arrangements
if friends_hypothesis != friends_premise:
    # Check if the number of friends in the hypothesis contradicts the number stated in the premise
    label = "contradiction"
else:
    # If the number of friends in the hypothesis does not contradict with the premise, it would be an entailment
    label = "entailment"

print(label)

