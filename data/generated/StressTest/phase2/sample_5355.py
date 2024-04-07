# Premise: The average number of shirts with Salman, Ambani and Dalmiya is 60, if all of them reached a shopping mall in Delhi and purchased 4 shirts each of them then average number of shirt each of them now has.
# Hypothesis: The average number of shirts with Salman, Ambani and Dalmiya is more than 20, if all of them reached a shopping mall in Delhi and purchased 4 shirts each of them then average number of shirt each of them now has.
# Golden Label: entailment

average_shirts_premise = 60
average_shirts_hypothesis = 20
shirts_bought_each = 4

# the hypothesis talks about the average number of shirts with Salman, Ambani and Dalmiya
# considering they all purchased additional shirts
average_shirts_premise += shirts_bought_each
average_shirts_hypothesis += shirts_bought_each

if average_shirts_hypothesis >= average_shirts_premise:
    # check if the hypothesis number contradicts the premise average number of shirts
    label = "contradiction"
elif average_shirts_hypothesis < average_shirts_premise:
    # check if the hypothesis number is less than the premise average number of shirts
    label = "entailment"
else:
    label = "neutral"

print(label)

