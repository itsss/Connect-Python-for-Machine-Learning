import numpy as np

def n_size_ndarray_creation(n, dtype=np.int):
    return np.array(range(n**2), dtype = dtype).reshape(n,n)

def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    if type == 0:
        a = np.zeros((shape))
        return a.astype(np.int32)
    elif type == 1:
        a = np.ones((shape))
        return a.astype(np.int32)
    elif type == 99:
        a = np.empty((shape))
        return a.astype(np.int32)

def change_shape_of_ndarray(X, n_row):
    return X.flatten() if n_row == 1 else X.reshape(n_row, -1)

def concat_ndarray(X_1, X_2, axis):
    try:
        if X_1.ndim == 1:
            X_1 = X_1.reshape(1, -1)
        if X_2.ndim == 1:
            X_2 = X_2.reshape(1, -1)
        return np.concatenate((X_1, X_2), axis=axis)
    except ValueError as e:
        return False

def normalize_ndarray(X, axis=99, dtype=np.float32):
    X = X.astype(np.float32)
    n_row, n_column = X.shape
    if axis == 99:
        x_mean = np.mean(X)
        x_std = np.std(X)
        Z = (X-x_mean)/x_std
    if axis == 0:
        x_mean = np.mean(X, 0).reshape(1, -1)
        x_std = np.std(X, 0).reshape(1, -1)
        Z = (X-x_mean)/x_std
    if axis == 1:
        x_mean = np.mean(X, 1).reshape(n_row, -1)
        x_std = np.std(X, 1).reshape(n_row, -1)
        Z = (X-x_mean)/x_std
    return Z
    X = np.arrange(12, dtype=np.float32).reshape(4,3)
    np.mean(X, 1).reshape(len(X), -1)
    normalize_ndarray(X,1)

def save_ndarray(X, filename="test.npy"):
    file_test = open(filename, "wb")
    np.save(X, file_test)

def boolean_index(X, condition):
    condition = eval(str("X")+condition)
    return np.where(condition)

def find_nearest_value(X, target_value):
    return X[np.argmin(np.abs(X-target_value))]

def get_n_largest_values(X, n):
    return X[np.argsort(X[::-1])[:n]]
    # -1 > 역순으로 데이터를 뽑음
