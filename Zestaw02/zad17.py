line = "jakis kolejny przykladowy napis zeby bylo co posortowac"

wyrazy = line.split()

print(sorted(wyrazy))
print(sorted(wyrazy, key=len))