+++
title = "[Sympy] 球座標系でのベクトル解析"
date = 2021-04-21
[taxonomies]
tags = ["Python", "SymPy"]
+++

```python
'''
球座標系でのベクトル解析

(c)2021 osanshouo https://osanshouo.github.io/blog/
Licensed under CC BY 4.0 https://creativecommons.org/licenses/by/4.0/legalcodeCreative-Commons 
'''

from sympy import symbols, cos, sin

r, theta, phi = symbols("r, theta, phi")

def dot(A, B):
    return A[0]*B[0] + A[1]*B[1] + A[2]*B[2]

def cross(A, B):
    return [
        A[1]*B[2] - A[2]*B[1],
        A[2]*B[0] - A[0]*B[2],
        A[0]*B[1] - A[1]*B[0],
    ]

def grad(f):
    return [
        f.diff(r),
        f.diff(theta)/r,
        f.diff(phi)/(r*sin(theta))
    ]

def div(A):
    return (r*r*A[0]).diff(r)/(r*r) + (A[1]*sin(theta)).diff(theta)/(r*sin(theta)) + A[2].diff(phi)/(r*sin(theta))

def rot(v):
    return [
        ( (v[2]*sin(theta)).diff(theta) - v[1].diff(phi) )/(r*sin(theta)),
        ( v[0].diff(phi)/sin(theta) - (r*v[2]).diff(r) )/r,
        ( (r*v[1]).diff(r) - v[0].diff(theta) )/r
    ]

def material_deriv(A, B):
    '''(A \cdot \nabla) B'''
    return [
        A[0]*B[0].diff(r) + A[1]*B[0].diff(theta)/r + A[2]*B[0].diff(phi)/(r*sin(theta)) - (A[1]*B[1] + A[2]*B[2])/r,
        A[0]*B[1].diff(r) + A[1]*B[1].diff(theta)/r + A[2]*B[1].diff(phi)/(r*sin(theta)) + A[1]*B[0]/r - A[2]*B[2]*cos(theta)/(r*sin(theta)),
        A[0]*B[2].diff(r) + A[1]*B[2].diff(theta)/r + A[2]*B[2].diff(phi)/(r*sin(theta)) + A[2]*B[0]/r + A[2]*B[1]*cos(theta)/(r*sin(theta))
    ]

def laplacian(f):
    return (f.diff(r)*r*r).diff(r)/(r*r) + (f.diff(theta)*sin(theta)).diff(theta)/(r*r*sin(theta)) + f.diff(phi).diff(phi)/(r*r*sin(theta)*sin(theta))

def laplacian_vec(A):
    return [
        laplacian(A[0]) - 2*A[1].diff(theta)/(r*r) - 2*A[2].diff(phi)/(r*r*sin(theta)) - 2*A[0]/(r*r) - 2*A[1]*cos(theta)/(r*r*sin(theta)),
        laplacian(A[1]) + 2*A[0].diff(theta)/(r*r) - 2*A[2].diff(phi)*cos(theta)/(r*r*sin(theta)*sin(theta)) - A[1]/(r*r*sin(theta)*sin(theta)),
        laplacian(A[2]) + 2*A[0].diff(phi)/(r*r*sin(theta)) + 2*A[1].diff(phi)*cos(theta)/(r*r*sin(theta)*sin(theta)) - A[2]/(r*r*sin(theta)*sin(theta)),
    ]

if __name__ == "__main__":
    from sympy import Function, simplify
    def simplify_vec(A):
        return [ simplify(A[0]), simplify(A[1]), simplify(A[2]) ]
    def vec_mul(psi, A):
        return [ psi*A[0], psi*A[1], psi*A[2] ]
    def vec_sum(terms):
        result = []
        for i in range(3):
            tmp = 0
            for term in terms:
                tmp += term[i]
            result.append(tmp)
        return result

    psi = symbols("psi")
    f = Function('f')(r, theta, phi)
    g = Function('g')(r, theta, phi)
    h = Function('h')(r, theta, phi)
    i = Function('i')(r, theta, phi)
    j = Function('j')(r, theta, phi)
    k = Function('k')(r, theta, phi)
    A = [ f, g, h ]
    B = [ i, j, k ]

    assert vec_sum([ A, B ]) == [ f+i, g+j, h+k ]
    assert vec_mul(psi, A) == [ psi*f, psi*g, psi*h ]
    assert simplify( dot(grad(psi), A) + psi*div(A) - div(vec_mul(psi, A))) == 0
    assert simplify(div(cross(A, B)) - dot(B, rot(A)) + dot(A, rot(B))) == 0
    assert rot(grad(psi)) == [ 0, 0, 0 ]
    assert simplify(div(rot(A))) == 0
    assert laplacian(1/r) == 0
    assert simplify_vec(vec_sum([ rot(rot(A)), vec_mul(-1, grad(div(A))), laplacian_vec(A)])) == [ 0, 0, 0 ]

    assert simplify_vec(vec_sum([
        material_deriv(B, A),
        material_deriv(A, B),
        cross(A, rot(B)),
        cross(B, rot(A)),
        vec_mul(-1, grad(dot(A, B)))
    ])) == [ 0, 0, 0 ]
```
