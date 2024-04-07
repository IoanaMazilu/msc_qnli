# Premise: Jose joined him less than 8 months later, investing Rs.
# Hypothesis: Jose joined him 2 months later, investing Rs.
# Golden Label: neutral

months_joined_premise = 8
months_joined_hypothesis = 2

# Both the premise and hypothesis refer to the number of months it took for Jose to join

if months_joined_hypothesis >= months_joined_premise:
    # If the months in the hypothesis is greater than or equal to the months mentioned in the premise
    label = "contradiction"
elif months_joined_hypothesis < months_joined_premise:
    # If the months in the hypothesis is less than the months mentioned in the premise
    label = "entailment"

print(label)

