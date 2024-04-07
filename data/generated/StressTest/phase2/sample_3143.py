# Premise: If in 12 years, John will be one year younger than twice the age of Mark on that day, how old is Mark today?
# Hypothesis: If in 32 years, John will be one year younger than twice the age of Mark on that day, how old is Mark today?
# Golden Label: contradiction

years_future_premise = 12
years_future_hypothesis = 32

# The hypothesis and premise both talk about the future age relations between John and Mark
# However, the time in the future when these relations are evaluated differs
if years_future_hypothesis != years_future_premise:
    # the premise and hypothesis evaluate the age relations at different future times
    label = "contradiction"
else:
    # this condition would normally check for entailment, but it's unnecessary in this case
    # as we've already established that the time frames are different
    pass

print(label)

