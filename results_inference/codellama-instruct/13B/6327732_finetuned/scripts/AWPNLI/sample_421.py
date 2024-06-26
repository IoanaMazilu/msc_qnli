# define variables for the numerical entities in the premise
joined_school_band_premise = 1
bought_trumpet_premise = 145.16
sold_song_book_premise = 5.84

# define variables for the numerical entities in the hypothesis
net_amount_spent_hypothesis = 134.7

# compute the total amount spent by Mike at the music store
total_amount_spent_premise = bought_trumpet_premise + sold_song_book_premise

# check if the net amount spent by Mike contradicts the estimate in the hypothesis
if net_amount_spent_hypothesis!= total_amount_spent_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
