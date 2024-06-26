future_age_premise = 15
future_age_hypothesis = 75
past_age = 15
quadrice = 4

# The hypothesis and premise both refer to Karthik's age at different points in the future
# 4 times as old as he was 15 years ago
# If Karthik's age 15 years ago is x, then his current age is x+15, and his age 15 years hence will be x+15+15
# We can set up the equation 4*x = x+30, to find his age
# Similarly, we can set up the equation 4*x = x+60 for the hypothesis

# Solving these equations gives us his age as per the premise and hypothesis
age_premise = (future_age_premise - past_age) / (quadrice - 1)
age_hypothesis = (future_age_hypothesis - past_age) / (quadrice - 1)

# We compare these ages to determine the relationship between the premise and hypothesis
if age_premise != age_hypothesis:
    # if the computed ages are different, then there is a contradiction
    label = "contradiction"
elif age_premise == age_hypothesis:
    # if the computed ages are the same, then the hypothesis is entailed by the premise
    label = "entailment"

print(label)
