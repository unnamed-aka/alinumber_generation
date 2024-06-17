# alinumber_generation
Most Slowest Number Generator

!!! WARNING !!!

END OF CYCLE IN THIS GENERATOR IS TECHNICALLY IMPOSSIBLE

## How its works?
Lets say, we have a seq (sequence) like this:

`1 [n = 2, k = 3]`

If LT (last seq number) equales 0, then replace LT to n-1 (n, if LT = 1) copyes of LT-1

```
1 [2, 3]
0,0 [2, 3]
```

Else replace n to n^seq_length+1 and all 0 in the end to 1,1

```
0,0[2, 3]
1,1 [10, 3]
```

If last k numbers in seq equales, then replace them to 2 copies of LT+1. If LT+1 was never on seq, then replace k to n

```
2,2,2 [13, 3]
3,3 [13, 13]
```

