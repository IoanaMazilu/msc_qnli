states_premise = ["Florida", "Ohio", "Pennsylvania"]
states_hypothesis = ["Ohio", "two other battleground states"]

# the hypothesis mentions the states where Obama is ahead, which are also referenced in the premise
# however, the hypothesis does not specify the exact number of states, which cannot be entailed from the premise
label = "neutral"

print(label)
