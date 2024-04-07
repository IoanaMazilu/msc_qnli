# Premise: Mary purchased Brand X pens for $2 apiece and brand Y for $1 apiece.
# Hypothesis: Mary purchased Brand X pens for $more than 2 apiece and brand Y for $1 apiece.
# Golden Label: contradiction

brand_x_price_premise = 2
brand_x_price_hypothesis = 2
brand_y_price_premise = 1
brand_y_price_hypothesis = 1

# The hypothesis talks about the price of Brand X and Brand Y pens, which is also referred in the premise
if brand_x_price_hypothesis > brand_x_price_premise:
    # check if the price of Brand X pens in the hypothesis contradicts the price of Brand X pens in the premise
    label = "contradiction"
elif brand_y_price_hypothesis != brand_y_price_premise:
    # check if the price of Brand Y pens in the hypothesis contradicts the price of Brand Y pens in the premise
    label = "contradiction"
else:
    # If the prices of Brand X and Brand Y pens in the hypothesis do not contradict the prices in the premise, we can infer entailment
    label = "entailment"

print(label)

