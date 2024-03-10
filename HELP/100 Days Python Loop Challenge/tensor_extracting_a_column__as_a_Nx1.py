import torch

#Sample tensor of shape 5x3
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12],
                  [13, 14, 15]])
k = 1
column_as_tensor = x[:, k, None]

print(column_as_tensor)
print(column_as_tensor.shape)

# tensor([[ 2],
#         [ 5],
#         [ 8],
#         [11],
#         [14]])
# torch.Size([5, 1])

#🐍 PyTorch useful tricks while working with Tensor - Extracting a column from a tensor as a Nx1 tensor (and not as a N-dim vector) 🐍

#We can use `x[:, k, None]` to extract a column from a 2D tensor `x` as an (N times 1) tensor rather than an (N)-dimensional vector.

#Let me break it down step-by-step:

#1. **Indexing with `:`**:
#    - When you use the colon (`:`), you're essentially selecting everything along that particular dimension. So, if `x` is a 2D tensor of shape (N times M), then `x[:, k]` would select all rows and the k-th column.

#2. **Extracting as an (N)-dimensional vector**:
#    - When you use `x[:, k]`, you'll get a tensor of shape (N), which is essentially a vector.

#3. **Using `None` for new axis**:
#    - In Python (and thus in PyTorch), you can use `None` to introduce a new axis in a tensor (or numpy array). By doing this, you're essentially reshaping the tensor without changing its data.
#    - So, when you index with `x[:, k, None]`, you're introducing a new dimension to the output, changing its shape from (N) to (N times 1).

# Hence, `x[:, k, None]` will give you a column vector (an (N times 1) tensor) instead of a simple 1-dimensional tensor.
