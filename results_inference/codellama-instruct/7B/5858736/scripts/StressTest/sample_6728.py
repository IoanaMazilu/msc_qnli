apples_selected_premise = 10
oranges_selected_premise = 10
fruit_price_premise = 56

apples_selected_hypothesis = 20
oranges_selected_hypothesis = 20
fruit_price_hypothesis = 56

# the hypothesis talks about the number of apples and oranges selected and the average price of the fruit
if apples_selected_hypothesis <= apples_selected_premise and oranges_selected_hypothesis <= oranges_selected_premise and fruit_price_hypothesis <= fruit_price_premise:
    # check if the hypothesis values contradict the premise ones
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of apples and oranges selected and the average price of the fruit
    # any number of apples and oranges greater than 'apples_selected_premise' and 'oranges_selected_premise' and any average price greater than 'fruit_price_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
