# Premise: The Logan County Sheriff's Office can be reached at 217-732-2156.
# Hypothesis: Have a tip? Call the Tazewell County Sheriff's Office at 309-346-4141.
# Golden Label: neutral

phone_number_premise = 2177322156
phone_number_hypothesis = 3093464141

# the hypothesis mentions a phone number and a sheriff's office, which are also mentioned in the premise
# however, the offices and the phone numbers do not match
label = "contradiction"

print(label)

