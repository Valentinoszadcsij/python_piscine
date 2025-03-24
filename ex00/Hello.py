# ft_list = ["Hello", "tata!"]
# ft_tuple = ("Hello", "toto!")
# ft_set = {"Hello", "tutu!"}
# ft_dict = {"Hello" : "titi!"}
# #lists in python are similar to std::vector in C++ (dynamic array)
# ft_list[1] = "World!"
# #tuples are immutable data structures (slightly faster than lists) so values can't be changed after initialization, so in this case I create a new ft_tuple
# ft_tuple = (ft_tuple[0], "Germany!")
# #sets are unordered and dont allow duplicates, no access by index
# ft_set.discard("tutu!")
# ft_set.add("Heilbronn!")
# ft_set = ["Hello", next(city for city in ft_set if city != "Hello")]
# #dictionaries are similar to std::unordered_map. since python3.7+ they guarantee order(Insertion Order Preserved) but we are using 3.10
# ft_dict["Hello"] = "42Heilbronn!"

ft_list = ["Hello", "World!"]
ft_tuple = ("Hello", "Germany!")
ft_set = {"Hello", "Heilbronn!"}
ft_dict = {"Hello" : "42Heilbronn!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)