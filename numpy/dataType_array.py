# data types as function
# list of characters that are used to represent dtype in numpy:
# i=integer
# b= boolean
# u= unsigned integer
# f= float
# c = complex float
# m = timedelta
# M = datetime
# O= object
# S= String 
# U= unicode string 
# V= the fixed chunk of memory for other types(void)


# data types numpy arrays
# bool_ - boolean(true or false) stored as a byte 
# int_  - Default integer type (same as c long; nrmally either int64 or int32)
# Intc - indentical to c int (normally int 32 or int 64)
# Intp - integer used for indexing (sameas c size_t; normally either int32 or int64)
# int8 - Byte (-128 to 127)
# int16 - integer(-32768 to 32767)
# int32 - integer(-2147483648 to 2147483647)
# int64 - integer(-922372036854775808 to 92233720368547758077)
# unit8 - unsigned integer (0 to 255)
# unnit16 - unsigned integer (0 to 65535)
# unit32 - unsigned integer (0 to 4294967295)
# float_ - shaothand for float64
# float16 - half precision float:sign bit,5 bits exponent, 10 bits mantissa
# float32 - single precision float: sign bit,8 bits expon





import numpy as np
var = np.array([1,2,3,45,88,8,55,88,55,5])
var1 = np.array(["sachin","ramesh","xyz"])
print("data type is: ", var.dtype )
print("data type is: ", var1.dtype )


x = np.array([1,2,3,4], dtype= "f")
print("data type: ", x.dtype)
print(x)