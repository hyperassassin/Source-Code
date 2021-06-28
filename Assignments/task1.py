#Solution of Q.1
movies = ["Serenity","The Great Escape","The Martian","West Side Story","In the Heights","M*A*S*H","The Scarlet Pimpernel"]
television_show = ["Sports Night","Have Gun, Will Travel","The Closer","Major Crimes","Then Came Bronson","Northern Exposure","M*A*S*H"]

#Solution of Q.2
print("No of Movies : " , len(movies))
print("\n")

print("No of Television shows : " , len(television_show))
print("\n")

#Solution of Q.3
m = len(movies)
print("------Movies------")
for i in range(m):
    print(movies[i])

print("\n")

t = len(television_show)
print("------Television Shows------")
for i in range(t):
    print(television_show[i])

print("\n")

#Solution of Q.4
movie = sorted(movies)
print("Movie Names in Sorted manner :- ", movie)

print("\n")

#Solution of Q.5
print("Last item in Television show list : ",str(television_show[len(television_show)-1]))

print("\n")

#Solution of Q.6
remove_last = television_show.pop()
print("Removed Item of the list : ",remove_last)
print("List after Removed item : ",television_show)

print("\n")

#Solution of Q.7
name = input("Enter the movie name : ")
try:
    movies.remove(name)
except:
    print("List does not contain the entered movie")
print("List after remove item : ",movies)

print("\n")

#Solution of Q.8
print("Original List : ",television_show)
television_show.reverse()
print("Reversed List : ",television_show)

print("\n")

#Solution of Q.9
television_show.append("F.R.I.E.N.D.S")
print("List after show update : ",television_show)
