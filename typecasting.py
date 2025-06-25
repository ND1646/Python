a_int = 5
b_float = 10.5
c_str = "123456"
d_bool = False

int_to_float=float(a_int)
print("int to float:",int_to_float,type(int_to_float))

float_to_int=int(b_float)
print("float to int:",float_to_int,type(float_to_int))

str_to_int=int(c_str)
print("str to int:",str_to_int,type(str_to_int))

bool_to_int=int(d_bool)
print("bool to int:",bool_to_int,type(bool_to_int))

int_to_bool=bool(a_int)
print("int to bool:",int_to_bool,type(int_to_bool))
