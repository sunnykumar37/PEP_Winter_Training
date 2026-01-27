types = {'name': str, 'age': int, 'address': str}
types2 = dict(name=str, age=int, address=str)
# the "Key" ('''name''') must be hashble (immutable)
print(types['name'])
types['language']  = str
print(types)

# create a dic of that contains of 3 keys: name of movie, cast, revenue
movies = {
    'Title': {'End Game', 'Avatar', 'Titanic', 'Star Wars', 'Inception'},
    'Cast': {
        'Robert Downey Jr.',
        'Sam Worthington',
        'Leonardo DiCaprio',
        'Mark Hamill',
        'Leonardo DiCaprio'
    },
    'Revenue': [
        2797800564,
        2787965087,
        2187463944,
        2068223624,
        836848102
    ]
}

movie_name = input("Enter movie name: ").title()

titles = list(movies['Title'])
casts = list(movies['Cast'])
revenues = movies['Revenue']

if movie_name in titles:
    index = titles.index(movie_name)
    print(
        f"The movie {titles[index]} was created by {casts[index]} "
        f"and has generated a total revenue of {revenues[index]} dollars."
    )
else:
    print("Movie not found.")
