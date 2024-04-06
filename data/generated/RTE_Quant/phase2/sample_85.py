# Premise: The average price of a gallon of gasoline has jumped a nickel over the past two weeks and is back near the record high set earlier this year, according to a national survey released Sunday.
# Hypothesis: Gas prices jumped 5 cents a gallon over the last two weeks.
# Golden Label: entailment

price_jump_premise = 0.05
price_jump_hypothesis = 0.05

# the hypothesis talks about the increase in gas prices over a certain period, which is also mentioned in the premise
if price_jump_hypothesis != price_jump_premise:
    # check if the increase in price in the hypothesis contradicts the increase in price from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

