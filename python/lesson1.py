# # learning and getting used to the python's varibles and types
# import socket 

# target = "scanme.nmap.org"

# port = [ 21, 22 , 23 , 80 , 443]

# for ports in port:
#     s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
#     s.settimeout(1)
#     result  = s.connect_ex((target, port))
#     if result == 0 :
#         print(f"{port} is OPEN")
#     else :
#         print(f"{port} is CLOSED")
#     s.close()


# class shape :
#     def area(shape):
#         raise NotImplementedError
# class circle(shape) :
#     pass

# obj = circle()
# obj.area()

# a, b, *c, d = [1, 2, 3, 4, 5,6 ,7]

# print(c)
d = 4
a = [1,2,3,4,5]
a = list(map(int , a))
a = a[1:] + a[:1]
for d in a :
  print(d, end = " ")  

print(a)