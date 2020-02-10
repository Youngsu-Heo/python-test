a = [1, 2, 3, 4, 5]

# recommend to use list comprehension rather than map
s_lc = [x**2 for x in a]
print(s_lc)

# not recommended
s_lb = map(lambda x: x**2, a)
print(list(s_lb))

# recommand to use lc + condition
even_squares = [x**2 for x in a if x%2 == 0]
print(even_squares)

alt = map(lambda x: x**2, filter(lambda x:x%2==0, a))
print(list(alt))

#assert even_squares == list(alt)

# list comprehension for dictionary
chile_ranks = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
rank_dict = {rank: name for name, rank in chile_ranks.items()}
chile_len_set = {len(name) for name in rank_dict.values()}
print(chile_ranks)
print(rank_dict)
print(chile_len_set)

