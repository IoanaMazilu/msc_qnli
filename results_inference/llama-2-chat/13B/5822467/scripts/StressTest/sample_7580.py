days_premise = 8
days_hypothesis = float(input("With the help of Pavan, they completed the work in more than 8 days and earned Rs. "))
earnings_premise = "Rs." + str(input("They earned Rs. "))
earnings_hypothesis = float(earnings_premise)

# the hypothesis talks about the number of days and earnings, referenced also in the premise
if days_hypothesis <= days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_premise'
    label = "contradiction"
elif earnings_hypothesis!= earnings_premise:
    # check if the earnings in the hypothesis contradict the earnings reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
