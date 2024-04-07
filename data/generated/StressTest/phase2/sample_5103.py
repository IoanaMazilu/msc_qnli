# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 69, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 39, if all of them reached a shopping mall in Delhi and purchased 12 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

initial_avg_shirts_premise = 69
initial_avg_shirts_hypothesis = 39
purchased_shirts = 12

# the premise and hypothesis both talk about the average number of shirts with three people
# and the change in this average after each of them purchases a certain number of shirts
# the premise and hypothesis both assume that the average is computed evenly across the three people
final_avg_shirts_premise = initial_avg_shirts_premise + purchased_shirts
final_avg_shirts_hypothesis = initial_avg_shirts_hypothesis + purchased_shirts

if final_avg_shirts_hypothesis > final_avg_shirts_premise:
    # check if the final average number of shirts in the hypothesis contradicts the final average number of shirts in the premise
    label = "contradiction"
elif final_avg_shirts_hypothesis < final_avg_shirts_premise:
    # check if the final average number of shirts in the hypothesis is less than the final average number of shirts in the premise
    label = "entailment"
else:
    # if the final average number of shirts in the hypothesis equals the final average number of shirts in the premise
    label = "neutral"

print(label)

