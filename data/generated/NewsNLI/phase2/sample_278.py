# Premise: Sterling has filed a $1B suit against the NBA because it banned him for life and forced him to sell.
# Hypothesis: He also filed a $1 billion lawsuit against the NBA for its decision to ban him for life and force him to sell the franchise.
# Golden Label: neutral

suit_value_premise = 1000000000
suit_value_hypothesis = 1000000000

# the hypothesis mentions the value of the suit filed against the NBA which is also mentioned in the premise
if suit_value_hypothesis != suit_value_premise:
    # check if the suit value in the hypothesis contradicts the suit value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis suit value does not contradict the premise suit value, we can infer entailment
    label = "entailment"

print(label)

