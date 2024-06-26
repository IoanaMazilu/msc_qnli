england_members_last_year = 26
france_members_last_year = 26
italy_members_last_year = 32
total_members_last_year = england_members_last_year + france_members_last_year + italy_members_last_year

# the hypothesis refers to the number of members who traveled to England, France and Italy last year
if england_members_last_year >= total_members_last_year - 56:
    label = "contradiction"
elif france_members_last_year!= 26:
    label = "contradiction"
elif italy_members_last_year!= 32:
    label = "contradiction"
else:
    label = "neutral"

print(label)
