total_pencils_premise = 75
distributed_pencils_premise = 20
remaining_pencils_premise = total_pencils_premise - distributed_pencils_premise

total_pencils_hypothesis = 55
distributed_pencils_hypothesis = 20

# Hypothesis talks about the remaining pencils with John after distributing some to his friends
# This is referenced in the premise as well
if total_pencils_hypothesis >= remaining_pencils_premise:
    # Checking if the hypothesis value contradicts the actual remaining pencils with John
    label = "contradiction"
elif distributed_pencils_hypothesis != distributed_pencils_premise:
    # Checking if the distributed pencils in the hypothesis contradicts with the premise
    label = "contradiction"
else:
    # The premise gives the exact number of remaining pencils with John
    # Any number less than 'remaining_pencils_premise' is consistent with the premise
    label = "neutral"

print(label)
