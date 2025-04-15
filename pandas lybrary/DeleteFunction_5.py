# when we wants to delete any column we will use the var.pop("colummn name")
# also we can use del var("col name")

import pandas as pd
var = pd.DataFrame({"a":[1,2,3,4,5],"b":[1,2,3,4,5],"c":[1,2,3,4,5]})



print(var)
var.pop("b")
print(var)

del var["a"]
print(var)