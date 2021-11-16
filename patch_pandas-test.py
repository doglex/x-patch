import pandas as pd
from patch_pandas import patch_head
from types import FunctionType
import contextlib
from io import StringIO

patch_head()

assert isinstance(pd.DataFrame.head1, FunctionType)

temp_stdout = StringIO()
with contextlib.redirect_stdout(temp_stdout):
    ans = pd.DataFrame([[1, 2, 3], [4, 5, 6]]).head()
output = temp_stdout.getvalue().strip().replace(" ", "")
assert output == "(2,3)"
print(output)
print(ans)
