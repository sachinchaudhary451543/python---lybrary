import pandas as pd
var = pd.DataFrame({"a":[12,23,2,34,45],"b":[21,45,33,22,56]})



var["add"] = var["a"] + var["b"]
var["sub"] = var["a"] - var["b"]
var["mult"] = var["a"] * var["b"]
var["devide"] = var["a"] / var["b"]

var["greater number (20) in col (a)"] = var["a"] <= 20
var["greater number (20) in col (b)"] = var["a"] <= 20
print(var)