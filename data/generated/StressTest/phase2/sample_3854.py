# Premise: The Computer Store has reduced the price of a computer by 15%. What is the original price of the computer if the sale price is $1275?
# Hypothesis: The Computer Store has reduced the price of a computer by more than 15%. What is the original price of the computer if the sale price is $1275?
# Golden Label: contradiction

sale_price = 1275
discount_premise = 15
discount_hypothesis = 15

# the hypothesis talks about the discount applied to a computer price, also mentioned in the premise
if discount_hypothesis != discount_premise:
    # check if the discount percentage in the hypothesis contradicts the discount percentage reported in the premise
    label = "contradiction"
else:
    # if the discount percentage in the hypothesis do not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

