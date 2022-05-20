# addition of vector
def v_add(a, b):
    n = len(a)
    res = []

    for i in range(n):
        val = a[i] + b[i]
        res.append(val)

    return res

# subtraction of vector
def v_sub(a, b):
    n = len(a)
    res = []

    for i in range(n):
        val = a[i] - b[i]
        res.append(val)

    return res

# scalar multiplication of vector
def v_smul(n, a):
    n = len(a)
    res = []

    for i in range(n):
        val = n * a[i]
        res.append(val)

    return res

# hadamard product of vector
def v_hmul(a, b):
    n = len(a)
    res = []

    for i in range(n):
        val = a[i] * b[i]
        res.append(val)

    return res

# hadamard division of vector
def v_hdiv(a, b):
    n = len(a)
    res = []

    for i in range(n):
        val = a[i] / b[i]
        res.append(val)

    return res

# addition of matrix
def mat_add(a, b):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            val = a[i][j] + b[i][j]
            row.append(val)
        res.append(row)

    return res

# subtraction of matrix
def mat_sub(a, b):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            val = a[i][j] - b[i][j]
            row.append(val)
        res.append(row)

    return res

# scalar multiplication of matrix
def mat_smul(b, a):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            val = b * a[i][j]
            row.append(val)
        res.append(row)

    return res

# hadamard product of matrix
def mat_hmul(a, b):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            val = a[i][j] * b[i][j]
            row.append(val)
        res.append(row)

    return res

# hadamard division of matrix
def mat_hdiv(a, b):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            val = a[i][j] / b[i][j]
            row.append(val)
        res.append(row)

    return res

# multiplication of matrix
def mat_mul(a, b):
    n = len(a)
    m1 = len(a[0])
    m2 = len(b[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m2):
            val = 0
            for k in range(m1):
                val += a[i][k] * b[k][j]
            row.append(val)
        res.append(row)

    return res

# trace of matrix
def mat_tr(a):
    n = len(a)
    val = 0

    for i in range(n):
        val += a[i][i]

    return val

# transposed matrix
def mat_transpose(a):
    n = len(a)
    m = len(a[0])
    At = []

    for i in range(m):
        row = []
        for j in range(n):
            val = a[j][i]
            row.append(val)
        At.append(row)

    return At

# symmetric matrix check
def symmetric_check(a):
    At = mat_transpose(a)

    return a == At

# elements of diagonal matrix
def diag_ele(a):
    n = len(a)
    d = []

    for i in range(n):
        d.append(a[i][i])

    return d

# diagonal matrix
def mat_diag(a):
    d = diag_ele(a)
    n = len(d)
    D = []

    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(d[i])
            else:
                row.append(0)
        D.append(row)

    return D

# upper bidiagonal matrix
def mat_bidiag_u(a):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            if i > j or j-i > 1:
                row.append(0)
            else:
                row.append(a[i][j])
        res.append(row)

    return res

# lower bidiagonal matrix
def mat_bidiag_l(a):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            if i < j or i-j > 1:
                row.append(0)
            else:
                row.append(a[i][j])
        res.append(row)

    return res

# identity matrix
def mat_identity(size):
    I = []

    for i in range(size):
        row = []
        for j in range(size):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        I.append(row)

    return I

# zero matrix
def mat_zeros(row, col):
    Z = []

    for i in range(row):
        row = []
        for j in range(col):
            row.append(0)
        Z.append(row)

    return Z

# upper triangular matrix
def mat_tri_u(a):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            if i > j:
                row.append(0)
            else:
                row.append(a[i][j])
        res.append(row)

    return res

# lower triangular matrix
def mat_tri_l(a):
    n = len(a)
    m = len(a[0])
    res = []

    for i in range(n):
        row = []
        for j in range(m):
            if i < j:
                row.append(0)
            else:
                row.append(a[i][j])
        res.append(row)

    return res

# toeplitz matrix
def mat_toeplitz(a, b):
    n1 = len(a)
    n2 = len(b)
    T = []

    for i in range(n1):
        row = []
        for j in range(n2):
            if i >= j:
                row.append(a[i-j])
            else:
                row.append(b[j-i])
        T.append(row)

    return T

# outer product
def mat_outer(a, b):
    n1 = len(a)
    n2 = len(b)
    res = []

    for i in range(n1):
        row = []
        for j in range(n2):
            val = a[i] * b[j]
            row.append(val)
        res.append(row)

    return res

# inner product
def mat_inner(a, b):
    n = len(a)
    res = 0

    for i in range(n):
        res += a[i] * b[i]

    return res

# householder matrix
def householder(v):
    n = len(v)
    v_outer = mat_outer(v, v)
    v_inner = mat_inner(v, v)

    V1 = mat_smul(1/v_inner, v_outer)
    V2 = mat_smul(2, V1)

    H = mat_sub(mat_identity(n), V2)

    return H

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [2, 4, 8]

    print(f'\na = {a}\nb = {b}')
    print(f'\naddition of vector: {v_add(a, b)}')
    print(f'\nsubtraction of vector: {v_sub(a, b)}')
    print(f'\nscalar multiplication of vector: {v_smul(3, a)}')
    print(f'\nhadamard product of vector: {v_hmul(a, b)}')
    print(f'\nhadamard division of vector: {v_hdiv(a, b)}')

    c = [[1, 2], [3, 4]]
    d = [[5, 6], [7, 8]]

    print(f'\nc = {c}\nd = {d}')
    print(f'\naddition of matrix: {mat_add(c, d)}')
    print(f'\nsubtraction of matrix: {mat_sub(c, d)}')
    print(f'\nscalar multiplication of matrix: {mat_smul(3, c)}')
    print(f'\nhadamard product of matrix: {mat_hmul(c, d)}')
    print(f'\nhadamard division of matrix: {mat_hdiv(c, d)}')
    print(f'\nmultiplication of matrix: {mat_mul(c, d)}')

    e = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print(f'\ne = {e}')
    print(f'\ntrace of matrix: {mat_tr(e)}')
    print(f'\ntransposed matrix: {mat_transpose(e)}')

    f = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]

    print(f'\nsymmetric matrix check: {symmetric_check(f)}')
    print(f'\ndiagonal matrix elements: {diag_ele(e)}')
    print(f'\ndiagonal matrix: {mat_diag(e)}')

    print(f'\nupper bidiagonal matrix: {mat_bidiag_u(f)}')
    print(f'\nlower bidiagonal matrix: {mat_bidiag_l(f)}')

    print(f'\nidentity matrix: {mat_identity(3)}')
    print(f'\nzero matrix: {mat_zeros(2, 3)}')
    print(f'\nupper triangular matrix: {mat_tri_u(e)}')
    print(f'\nlower triangular matrix: {mat_tri_l(e)}')

    g = [1, 2, 3, 4]
    h = [5, 6, 7, 8]

    print(f'\ntoeplitz matrix: {mat_toeplitz(g, h)}')

    i = [1, 2, 3, 4]

    print(f'\nhouseholder matrix: {householder(i)}')