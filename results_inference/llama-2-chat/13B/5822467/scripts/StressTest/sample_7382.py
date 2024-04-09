# define variables for the numerical entities in the premise and hypothesis
book_price_premise = 20
book_count_premise = 6

# define variables for the numerical entities in the hypothesis
book_price_hypothesis = float(input("Enter the average price of the books (less than 20 $): "))
book_count_hypothesis = 6

# calculate the total cost of the books in the premise
total_cost_premise = book_count_premise * book_price_premise

# calculate the total cost of the books in the hypothesis
total_cost_hypothesis = book_count_hypothesis * book_price_hypothesis

# compare the total cost of the books in the premise and hypothesis
if total_cost_hypothesis < total_cost_premise:
    # the hypothesis is less than the premise, so we have entailment
    label = "entailment"
elif total_cost_hypothesis > total_cost_premise:
    # the hypothesis is greater than the premise, so we have contradiction
    label = "contradiction"
else:
    # the hypothesis and premise have the same total cost, so we have neutrality
    label = "neutral"

print(label)
