# Premise: John was thrice as old as Tom more than 2 years ago.
# Hypothesis: John was thrice as old as Tom 6 years ago.
# Golden Label: neutral

years_ago_premise = 2
years_ago_hypothesis = 6

# The hypothesis refers to the relationship between John's and Tom's age at a certain point in the past, but at a different point than the premise.
if years_ago_hypothesis == years_ago_premise:
    # Check if the number of years ago in the hypothesis contradicts the number of years ago in the premise.
    label = "contradiction"
else:
    # The premise does not provide explicit information about John's and Tom's age more than 'years_ago_premise' years ago.
    # Therefore, any claim about their ages more than 'years_ago_premise' years ago cannot be explicitly entailed or contradicted by the premise.
    label = "neutral"

print(label)

