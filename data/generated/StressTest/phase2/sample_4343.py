# Premise: Pooja is selling her books at puzzles land at a strange price as * she sells her book '' Vanity'' at $30 * she sells her book '' Sybil'' at $25 * she sells her book '' xmen'' at $20 At what price does she sell her book '' twilight''?
# Hypothesis: Pooja is selling her books at puzzles land at a strange price as * she sells her book '' Vanity'' at $80 * she sells her book '' Sybil'' at $25 * she sells her book '' xmen'' at $20 At what price does she sell her book '' twilight''?
# Golden Label: contradiction

vanity_book_price_premise = 30
vanity_book_price_hypothesis = 80
sybil_book_price_premise = 25
sybil_book_price_hypothesis = 25
xmen_book_price_premise = 20
xmen_book_price_hypothesis = 20

# the hypothesis refers to the price of the books mentioned in the premise

if vanity_book_price_premise != vanity_book_price_hypothesis:
    # check if the price of the book 'Vanity' in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
elif sybil_book_price_premise != sybil_book_price_hypothesis:
    # check if the price of the book 'Sybil' in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
elif xmen_book_price_premise != xmen_book_price_hypothesis:
    # check if the price of the book 'xmen' in the hypothesis contradicts the price mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

