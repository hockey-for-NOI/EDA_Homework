# EDA 05

#### CST53 HeQi 2015011299

## Cube

Input: cube.in

line 1: Integer n, m. The number of cubes in set A and B.

line 2~n+1: Integer x0, y0, z0, x1, y1, z1, describes a cube in set A.

line n+2~n+m+1: Integer x0, y0, z0, x1, y1, z1, describes a cube in set B.

Output: cube.out

line 1: Integer k, the number of cubes in set A intersect B.

line 2~k+1: Integer x0, y0, z0, x1, y1, z1, describes a cube in set A intersect B.

## Logic

Input: logic.in

line 1: Integer n, m, k. N and m are The number of parts in set A and B, and k is the number of dimensions.

line 2~n+1: A string contains '0', '1' or 'X'. The length is equal to k. This describes a part in set A.

line n+2~n+m+1: A string contains '0', '1' or 'X'. The length is equal to k. This describes a part in set B.

Output: logic\_union.out

line 1: Integer r. The number of parts in union.

line 2~r+1: A string contains '0', '1' or 'X'. The length is equal to k (though k is not specified in output). This describes a part in set A union B.

Output: logic\_intersect.out

line 1: Integer r. The number of parts in intersect.

line 2~r+1: A string contains '0', '1' or 'X'. The length is equal to k (though k is not specified in output). This describes a part in set A intersect B.
