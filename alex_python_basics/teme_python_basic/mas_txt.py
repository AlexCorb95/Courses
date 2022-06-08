# sa se masoare lungimea unui text dat pentru un referat
# daca are 0-800 cuvinte, sa se afiseze "insuficient"
# daca are 800-1000 cuvinte, sa se afiseze "acceptat"
# daca are peste 1000 de cuvinte, sa se afiseze "prea mult"
referat = """Python is an interpreted high-level general-purpose programming language. 
Its design philosophy emphasizes code readability with its use of significant indentation. 
Its language constructs as well as its object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.[30]

Python is dynamically-typed and garbage-collected. It supports multiple programming paradigms, including structured (particularly, procedural), object-oriented and functional programming. It is often described as a "batteries included" language due to its comprehensive standard library.[31][32]

Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.[33] Python 2.0 was released in 2000 and introduced new features, such as list comprehensions and a cycle-detecting garbage collection system (in addition to reference counting). Python 3.0 was released in 2008 and was a major revision of the language that is not completely backward-compatible. Python 2 was discontinued with version 2.7.18 in 2020.[34]

Python consistently ranks as one of the most popular programming languages"""
ref_count = referat.count(" ")
if ref_count < 800:
    print(f"{ref_count} de cuviente -> insuficent")
elif ref_count <= 1000:
    print(f"{ref_count} de cuviente -> acceptat")
else:
    print(f"{ref_count} de cuviente -> prea mult")
