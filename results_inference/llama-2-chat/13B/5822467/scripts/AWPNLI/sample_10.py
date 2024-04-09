cake_lunch_premise = 5.0
cake_dinner_premise = 6.0
total_cake_premise = cake_lunch_premise + cake_dinner_premise
cake_yesterday_premise = 3.0

# define variables for the hypothesis
total_cake_hypothesis = 14.0

# compare the total number of cakes served in the premise and the hypothesis
if total_cake_hypothesis!= total_cake_premise:
    # check if the total number of cakes in the hypothesis contradicts the premise
    label = "contradiction"
elif total_cake_hypothesis > total_cake_premise:
    # check if the total number of cakes in the hypothesis entails the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
