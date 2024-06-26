# define variables for numerical entities in the premise and hypothesis
book_price_premise = 20
book_count_premise = 6

# define variables for numerical entities in the hypothesis
book_price_hypothesis = 60
book_count_hypothesis = 6

# calculate the arithmetic mean of the book prices in the premise
book_price_mean_premise = book_price_premise * book_count_premise / 6

# calculate the arithmetic mean of the book prices in the hypothesis
book_price_mean_hypothesis = book_price_hypothesis * book_count_hypothesis / 6

# compare the arithmetic means of the book prices in the premise and hypothesis
if book_price_mean_hypothesis <= book_price_mean_premise:
    # the hypothesis does not contradict the premise, so the label is neutral
    label = "neutral"
elif book_price_mean_hypothesis > book_price_mean_premise:
    # the hypothesis contradicts the premise, so the label is contradiction
    label = "contradiction"
else:
    # the hypothesis is consistent with the premise, so the label is entailment
    label = "entailment"

print(label)
