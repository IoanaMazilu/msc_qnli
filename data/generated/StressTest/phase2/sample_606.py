# Premise: Mary purchased Brand X pens for $2 apiece and brand Y for $1 apiece.
# Hypothesis: Mary purchased Brand X pens for $less than 5 apiece and brand Y for $1 apiece.
# Golden Label: entailment

brand_x_price_premise = 2
brand_x_price_hypothesis = 5
brand_y_price_premise = 1
brand_y_price_hypothesis = 1

# the hypothesis refers to the price of Brand X and Brand Y pens mentioned in the premise
if brand_x_price_premise >= brand_x_price_hypothesis:
    # check if the price estimate for 'brand_x_price_hypothesis' contradicts the actual price of Brand X pens in the premise
    label = "contradiction"
elif brand_y_price_premise != brand_y_price_hypothesis:
    # check if the price of Brand Y pens in the hypothesis contradicts the actual price of Brand Y pens reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

