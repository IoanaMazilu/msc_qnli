purse_premise = 8
gift_premise = 3

# define variables for the hypothesis
purse_hypothesis = float(input("Enter the number of purses Faiza has: "))
gift_hypothesis = float(input("Enter the number of purses Faiza gives as gift: "))

# compare the values of the premise and hypothesis
if purse_hypothesis > purse_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif gift_hypothesis!= gift_premise:
    # the number of purses given as gift in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones
    label = "neutral"

print(label)
