# Premise: Srinivas saves one coin of 5 on first day of the week, three coins of 5 on the second day of the week. Five coins of 5 on third day and so on.
# Hypothesis: Srinivas saves one coin of more than 4 on first day of the week, three coins of 5 on the second day of the week. Five coins of 5 on third day and so on.
# Golden Label: entailment

coin_value_day1_premise = 5
coin_value_day1_hypothesis = 4
coin_value_other_days_premise = 5
coin_value_other_days_hypothesis = 5

# The hypothesis refers to the value of the coin Srinivas saves every day, mentioned also in the premise
if coin_value_day1_hypothesis >= coin_value_day1_premise:
    # Checking if the value of the coin saved on the first day in the hypothesis contradicts the value of the coin saved on the first day in the premise
    label = "contradiction"
elif coin_value_other_days_hypothesis != coin_value_other_days_premise:
    # Checking if the value of the coin saved on the other days in the hypothesis contradicts the value of the coin saved on the other days in the premise
    label = "contradiction"
else:
    # If the coin values in the hypothesis do not contradict the coin values in the premise, we can infer entailment
    label = "entailment"

print(label)

