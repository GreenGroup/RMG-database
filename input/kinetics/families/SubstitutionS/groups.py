#!/usr/bin/env python
# encoding: utf-8

name = "SubstitutionS/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Root"], products=["S-RR_or_RRrad", "YJ"], ownReverse=True)

reversible = True

reverseMap = {'*2': '*3', '*3': '*2'}

recipe(actions=[
    ['BREAK_BOND', '*1', 1, '*2'],
    ['FORM_BOND', '*1', 1, '*3'],
    ['GAIN_RADICAL', '*2', '1'],
    ['LOSE_RADICAL', '*3', '1'],
])

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *1 S2s       u0     p2 c0 {2,S} {3,S}
2 *2 R         u[0,1] {1,S}
3    R         u0     {1,S}
4 *3 [C,O,S,H] u[1,2]
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_4CCCCHHHHOOOOSSSS->H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 R   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 H   u1    
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 C   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 H   u1    
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,[S,D,T,B]}
3    R   u0 {1,S}
4 *3 H   u1
5    R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,D}
3    R   u0 {1,S}
4 *3 H   u1
5    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,D}
3    R   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,D}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,D} {6,S}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,D}
6    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,D}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,D} {6,S}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,D}
6    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,D}
3    R   u0 r0 {1,S}
4 *3 H   u1 r0
5    O   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    R   u0 {1,S}
4 *3 H   u1
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S}
3    R   u0 r0 {1,S} {6,[S,D,T,B]}
4 *3 H   u1 r0
5    C   u0 {2,S}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 H   u1
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    O   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,D}
6    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {7,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,D}
6    C   u0 {5,D}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S} {6,D}
6    C   u0 r0 {5,D}
7    R!H ux {2,[S,D,T,B]}
8    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,T}
6    C   u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {7,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,T}
6    C   u0 {5,T}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S} {6,T}
6    C   u0 r0 {5,T}
7    R!H ux {2,[S,D,T,B]}
8    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {6,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S}
6    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S}
6    R!H ux {2,[S,D,T,B]}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,D}
6    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {7,[S,D,T,B]}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,D}
6    C   u0 {5,D}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S} {6,D}
6    C   u0 r0 {5,D}
7    R!H ux {2,[S,D,T,B]}
8    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,T}
6    C   u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {7,[S,D,T,B]}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S} {6,T}
6    C   u0 {5,T}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S} {6,T}
6    C   u0 r0 {5,T}
7    R!H ux {2,[S,D,T,B]}
8    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {6,[S,D,T,B]}
3    C   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S}
6    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S}
6    R!H ux {2,[S,D,T,B]}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 C     u[0,1] {1,S}
3    [S,C] u0     {1,S}
4 *3 H     u1    
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 C     u0 {1,S}
3    [S,C] u0 {1,S} {5,[S,D,T,B]}
4 *3 H     u1
5    R!H   ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
4 *3 H   u1
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S} {5,S} {6,[S,D,T,B]}
4 *3 H   u1
5    C   u0 {3,S} {7,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S} {5,S} {6,[S,D,T,B]}
4 *3 H   u1
5    C   u0 {3,S} {7,D}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {8,[S,D,T,B]}
4 *3 H   u1 r0
5    C   u0 r0 {3,S} {7,D}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {5,D}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S} {5,S} {6,[S,D,T,B]}
4 *3 H   u1
5    C   u0 {3,S} {7,T}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {8,[S,D,T,B]}
4 *3 H   u1 r0
5    C   u0 r0 {3,S} {7,T}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {5,T}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
4 *3 H   u1 r0
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,D} {6,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,D}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S} {6,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,S}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S} {5,S}
4 *3 H   u1
5    C   u0 {3,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,S} {6,D}
6    C   u0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,S} {6,T}
6    C   u0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 C     u0 {1,S}
3    [S,C] u0 {1,S} {5,[S,D,T,B]}
4 *3 H     u1
5    C     u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    C   u0 {1,S} {5,[S,D,T,B]}
4 *3 H   u1
5    C   u0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,D}
4 *3 H   u1 r0
5    C   u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 H   u1 r0
5    S   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S}
4 *3 H   u1 r0
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 C   u[0,1] {1,S}
3    C   u0     {1,S}
4 *3 H   u1     r0
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    R   u0 {1,S}
4 *3 H   u1
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    H   u0 {1,S}
4 *3 H   u1
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 H   u1
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    H   u0 r0 {1,S}
4 *3 H   u1 r0
5    S   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 S     u0 {1,S}
3    [S,C] u0 {1,S}
4 *3 H     u1
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 S     u0 {1,S} {5,S}
3    [S,C] u0 {1,S}
4 *3 H     u1
5    R!H   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 S     u0 {1,S} {5,S}
3    [S,C] u0 {1,S}
4 *3 H     u1
5    C     u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S} {5,S}
3    S   u0 {1,S}
4 *3 H   u1
5    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    S   u0 r0 {1,S} {6,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
5    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
5    S   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    S   u0 {1,S}
4 *3 H   u1
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 H   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 H   u1 r0
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 R       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1    
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 H       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1    
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 H       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,[S,D,T,B]}
5    R!H     u0     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S}
5    C   u0     {4,S} {6,[S,D,T,B]}
6    C   u0     {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S} {7,[S,D,T,B]}
5    C   u0     {4,S} {6,[S,D,T,B]}
6    C   u0     {5,[S,D,T,B]}
7    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0     {4,S} {6,[S,D,T,B]}
6    C   u0     {5,[S,D,T,B]}
7    R!H ux     {4,[S,D,T,B]}
8    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0     {4,S} {6,D}
6    C   u0     {5,D}
7    R!H ux     {4,[S,D,T,B]}
8    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0     r0 {4,S} {6,D}
6    C   u0     r0 {5,D}
7    R!H ux     {4,[S,D,T,B]}
8    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 r0 {4,S} {6,D}
6    C   u0 r0 {5,D}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0     {4,S} {6,T}
6    C   u0     {5,T}
7    R!H ux     {4,[S,D,T,B]}
8    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0     r0 {4,S} {6,T}
6    C   u0     r0 {5,T}
7    R!H ux     {4,[S,D,T,B]}
8    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 r0 {4,S} {6,T}
6    C   u0 r0 {5,T}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     {5,S} {7,S}
5    C   u0     {4,S} {6,[S,D,T,B]}
6    C   u0     {5,[S,D,T,B]}
7    C   u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S} {7,S}
5    C   u0     r0 {4,S} {6,D}
6    C   u0     r0 {5,D}
7    C   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S} {7,S}
5    C   u0     r0 {4,S} {6,T}
6    C   u0     r0 {5,T}
7    C   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S}
4 *3 C   u1 {5,S} {7,S}
5    C   u0 {4,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
7    C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,S}
5    C   u0 r0 {4,S} {6,D}
6    C   u0 r0 {5,D}
7    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,S}
5    C   u0 r0 {4,S} {6,T}
6    C   u0 r0 {5,T}
7    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S}
5    C   u0     {4,S} {6,D}
6    C   u0     {5,D}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S}
5    C   u0     r0 {4,S} {6,D}
6    C   u0     r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S} {6,D}
6    C   u0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S}
5    C   u0     {4,S} {6,T}
6    C   u0     {5,T}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S}
5    C   u0     r0 {4,S} {6,T}
6    C   u0     r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S} {6,T}
6    C   u0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 S   u1     {5,S}
5    S   u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 S   u1     r0 {5,S}
5    S   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 S   u1 r0 {5,S}
5    S   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 H       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,[S,D,T,B]}
5    [C,O]   u0     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 H     u[0,1] {1,S}
3    R     u0     {1,S}
4 *3 C     u1     {5,D}
5    [C,O] u0     {4,D}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 H     u[0,1] {1,S}
3    H     u0     {1,S}
4 *3 C     u1     {5,D}
5    [C,O] u0     {4,D}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     {5,D}
5    C   u0     {4,D}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,D} {6,S}
5    C   u0     r0 {4,D}
6    C   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,D}
5    O   u0     r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S}
4 *3 C   u1 {5,D}
5    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,D} {6,S}
5    C   u0 r0 {4,D}
6    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 H       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,S}
5    [C,O]   u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 H     u[0,1] {1,S}
3    R     u0     {1,S}
4 *3 C     u1     {5,S} {6,[S,D,T,B]}
5    [C,O] u0     {4,S}
6    R!H   ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    R   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {6,S}
5    O   u0 r0 {4,S}
6    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S} {6,[S,D,T,B]}
5    C   u0     {4,S}
6    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     {5,S} {6,[S,D,T,B]}
5    C   u0     {4,S}
6    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
5    C   u0     r0 {4,S}
6    R!H ux     {4,[S,D,T,B]}
7    R!H ux     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S}
4 *3 C   u1 {5,S} {6,[S,D,T,B]}
5    C   u0 {4,S}
6    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
5    C   u0 r0 {4,S}
6    R!H ux {4,[S,D,T,B]}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 C   u1     {5,S}
5    C   u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    R   u0 r0 {1,S} {6,[S,D,T,B]}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0 {5,S}
5    C   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 S   u1     {5,S}
5    C   u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S   u0 {1,S}
4 *3 S   u1 {5,S}
5    C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    S   u0 r0 {1,S} {6,S}
4 *3 S   u1 r0 {5,S}
5    C   u0 r0 {4,S}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 H     u[0,1] {1,S}
3    [H,C] u0     {1,S}
4 *3 S     u1     {5,S}
5    C     u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 S   u1     r0 {5,S}
5    C   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 S   u1 r0 {5,S}
5    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S",
    group = 
"""
1 *1 S2s     u0 p2 c0 {2,S} {3,S}
2 *2 H       u0 {1,S}
3    S       u0 {1,S}
4 *3 [O,S,C] u1
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S   u0 {1,S}
4 *3 C   u1
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S   u0 {1,S} {5,S}
4 *3 C   u1
5    R!H u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 C   u1 r0
5    S   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    S   u0 {1,S}
4 *3 S   u1
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 S   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 H       u[0,1] {1,S}
3    [H,C]   u0     {1,S}
4 *3 [O,S,C] u1    
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S} {5,[S,D,T,B]}
4 *3 C   u1
5    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
4 *3 C   u1
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S} {5,S} {6,[S,D,T,B]}
4 *3 C   u1
5    C   u0 {3,S} {7,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S} {5,S} {6,[S,D,T,B]}
4 *3 C   u1
5    C   u0 {3,S} {7,D}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {8,[S,D,T,B]}
4 *3 C   u1 r0
5    C   u0 r0 {3,S} {7,D}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {5,D}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S} {5,S} {6,[S,D,T,B]}
4 *3 C   u1
5    C   u0 {3,S} {7,T}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {8,[S,D,T,B]}
4 *3 C   u1 r0
5    C   u0 r0 {3,S} {7,T}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {5,T}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
4 *3 C   u1 r0
5    R!H ux {3,[S,D,T,B]}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,D} {6,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,D}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S} {6,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,S}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 H   u0 {1,S}
3    C   u0 {1,S} {5,S}
4 *3 C   u1
5    C   u0 {3,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,S} {6,D}
6    C   u0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,S} {6,T}
6    C   u0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S} {5,D}
4 *3 C   u1 r0
5    C   u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 H     u[0,1] {1,S}
3    [H,C] u0     {1,S}
4 *3 C     u1    
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 C   u1     r0
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C",
    group = 
"""
1 *1 S2s   u0     p2 c0 {2,S} {3,S}
2 *2 H     u[0,1] {1,S}
3    [H,C] u0     {1,S}
4 *3 S     u1    
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 H   u[0,1] {1,S}
3    H   u0     {1,S}
4 *3 S   u1     r0
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 H   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 S   u1 r0
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 [S,C]   u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1    
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    R   u0 {1,S}
4 *3 C   u1
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,S}
5    C   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S} {6,[S,D,T,B]}
6    R!H ux {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S} {6,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 C   u1 {5,S}
5    C   u0 {4,S}
6    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    S   u0 {1,S}
4 *3 C   u1
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    S   u0 {1,S} {5,S}
4 *3 C   u1
5    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {6,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 C   u1 r0
5    C   u0 r0 {3,S}
6    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    S   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 S     u0 {1,S}
3    [H,C] u0 {1,S}
4 *3 C     u1
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 C   u1
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    S   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S}
3    C   u0 {1,S}
4 *3 C   u1
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 S   u0 {1,S} {5,S}
3    C   u0 {1,S}
4 *3 C   u1
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 S   u0 r0 {1,S} {5,S}
3    C   u0 r0 {1,S}
4 *3 C   u1 r0
5    S   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 C       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1    
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 C       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,[S,D,T,B]}
5    R!H     u0     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,S}
5    C   u0 {4,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,S} {7,[S,D,T,B]}
5    C   u0 {4,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 {4,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 r0 {4,S} {6,D}
6    C   u0 r0 {5,D}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
5    C   u0 r0 {4,S} {6,T}
6    C   u0 r0 {5,T}
7    R!H ux {4,[S,D,T,B]}
8    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,S}
5    C   u0 r0 {4,S} {6,D}
6    C   u0 r0 {5,D}
7    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {7,S}
5    C   u0 r0 {4,S} {6,T}
6    C   u0 r0 {5,T}
7    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S} {6,D}
6    C   u0 r0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S} {6,T}
6    C   u0 r0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    R   u0 {1,S}
4 *3 S   u1 {5,S}
5    S   u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 S   u1 r0 {5,S}
5    S   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    C   u0 r0 {1,S}
4 *3 S   u1 r0 {5,S}
5    S   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 C       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,[S,D,T,B]}
5    [C,O]   u0     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,[S,D,T,B]}
5    O   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {6,S}
5    O   u0 r0 {4,S}
6    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 C       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,[S,D,T,B]}
5    C       u0     {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,[S,D,T,B]} {6,[S,D,T,B]}
5    C   u0 {4,[S,D,T,B]}
6    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,D} {6,S}
5    C   u0 r0 {4,D}
6    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1 {5,S} {6,[S,D,T,B]}
5    C   u0 {4,S}
6    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
5    C   u0 r0 {4,S}
6    R!H ux {4,[S,D,T,B]}
7    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS",
    group = 
"""
1 *1 S2s     u0     p2 c0 {2,S} {3,S}
2 *2 C       u[0,1] {1,S}
3    R       u0     {1,S}
4 *3 [O,S,C] u1     {5,S}
5    C       u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,S}
5    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 C   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 S   u1     {5,S}
5    C   u0     {4,S}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 C   u[0,1] {1,S}
3    C   u0     {1,S}
4 *3 S   u1     r0 {5,S}
5    C   u0     r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 C     u0 {1,S}
3    [S,H] u0 {1,S}
4 *3 S     u1 {5,S}
5    C     u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S} {6,S}
4 *3 S   u1 r0 {5,S}
5    C   u0 r0 {4,S}
6    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 C     u0 {1,S} {6,[S,D,T,B]}
3    [S,H] u0 {1,S}
4 *3 S     u1 {5,S}
5    C     u0 {4,S}
6    R!H   ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S}
4 *3 S   u1 r0 {5,S}
5    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 S   u1 r0 {5,S}
5    C   u0 r0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0 {5,D}
5    C   u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S}
3    H   u0 {1,S}
4 *3 C   u1
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 C   u1
5    R!H u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,D}
3    H   u0 {1,S}
4 *3 C   u1
5    R!H u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,D}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,D} {6,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,D}
6    C   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,D}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    O   u0 {2,D}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 C   u1
5    R!H u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    O   u0 r0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S} {6,[S,D,T,B]}
6    C   u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S} {6,D}
6    C   u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {7,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S} {6,D}
6    C   u0 {5,D}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,S} {6,D}
6    C   u0 r0 {5,D}
7    R!H ux {2,[S,D,T,B]}
8    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S} {6,T}
6    C   u0 {5,T}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {7,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S} {6,T}
6    C   u0 {5,T}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,S} {6,T}
6    C   u0 r0 {5,T}
7    R!H ux {2,[S,D,T,B]}
8    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,S} {6,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 C   u1
5    C   u0 {2,S}
6    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S} {5,S} {6,[S,D,T,B]} {7,[S,D,T,B]}
3    H   u0 r0 {1,S}
4 *3 C   u1 r0
5    C   u0 r0 {2,S}
6    R!H ux {2,[S,D,T,B]}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C",
    group = 
"""
1 *1 S2s u0     p2 c0 {2,S} {3,S}
2 *2 C   u[0,1] {1,S}
3    R   u0     {1,S}
4 *3 S   u1    
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S} {5,S}
4 *3 S   u1 r0
5    C   u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C",
    group = 
"""
1 *1 S2s u0     p2 c0 r0 {2,S} {3,S}
2 *2 C   u[0,1] {1,S}
3    C   u0     {1,S}
4 *3 S   u1     r0
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C",
    group = 
"""
1 *1 S2s   u0 p2 c0 {2,S} {3,S}
2 *2 C     u0 {1,S}
3    [S,H] u0 {1,S}
4 *3 S     u1
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 S   u1
5    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R",
    group = 
"""
1 *1 S2s u0 p2 c0 {2,S} {3,S}
2 *2 C   u0 {1,S} {5,[S,D,T,B]} {6,[S,D,T,B]}
3    H   u0 {1,S}
4 *3 S   u1
5    R!H ux {2,[S,D,T,B]}
6    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    S   u0 r0 {1,S}
4 *3 S   u1 r0
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S",
    group = 
"""
1 *1 S2s u0 p2 c0 r0 {2,S} {3,S}
2 *2 C   u0 r0 {1,S}
3    H   u0 r0 {1,S}
4 *3 S   u1 r0
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_4CCCCHHHHOOOOSSSS->H
        L3: Root_4CCCCHHHHOOOOSSSS->H_2R->C
            L4: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R
                L5: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_3R->H_Ext-2C-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_N-3R->H_Ext-2C-R
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
                L5: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_Ext-3R-R
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_5R!H->O
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
                                    L10: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
                                        L11: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
                                    L10: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
                                        L11: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_3R->H_N-5R!H->O_Ext-2C-R_Ext-2C-R
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R
                                    L10: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R
                                    L10: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-5R!H-R_N-Sp-6R!H=5R!H_Ext-2C-R_Ext-2C-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_Ext-2C-R_N-Sp-5R!H=2C_N-3R->H_Ext-2C-R_Ext-2C-R
            L4: Root_4CCCCHHHHOOOOSSSS->H_2R->C_3R->H
            L4: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H
                L5: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CS-R
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
                                L9: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CS-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Ext-3CS-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_Sp-5R!H=3CCSS
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-3CS-R_N-Sp-5R!H=3CCSS
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_3CS->S
                        L7: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_Sp-5C-3C
                            L8: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_5R!H->C_N-3CS->S_N-Sp-5C-3C
                    L6: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_Ext-3CS-R_N-5R!H->C
                L5: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_3CS->S
                L5: Root_4CCCCHHHHOOOOSSSS->H_2R->C_N-3R->H_N-3CS->S
        L3: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C
            L4: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H
                L5: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R
                    L6: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_5R!H->C
                    L6: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_3R->H_Ext-2HS-R_N-5R!H->C
            L4: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H
                L5: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R
                    L6: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C
                        L7: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S
                            L8: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_3CS->S_Ext-3S-R
                        L7: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_5R!H->C_N-3CS->S
                    L6: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_Ext-2HS-R_N-5R!H->C
                L5: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S
                    L6: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_3CS->S_Ext-3S-R
                L5: Root_4CCCCHHHHOOOOSSSS->H_N-2R->C_N-3R->H_N-3CS->S
    L2: Root_N-4CCCCHHHHOOOOSSSS->H
        L3: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H
            L4: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_3R->H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H_N-3R->H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_3R->H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H_N-3R->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_Sp-6R!H=5R!H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_3R->H_N-Sp-6R!H=5R!H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_Sp-6R!H=5R!H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-3R->H_N-Sp-6R!H=5R!H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_3R->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H_N-3R->H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_3R->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H_N-3R->H
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_3R->H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_5R!H->S_N-3R->H
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_5CO->C_Ext-4COS-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_3R->H_N-5CO->C
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_Sp-5CCCOOOS=4CCCCOOOOSS_N-3R->H_Ext-4COS-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_5CCOO->O
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_3R->H_Ext-4COS-R
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_Ext-4COS-R_N-5CCOO->O_N-3R->H_Ext-4COS-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_Ext-3R-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_3R->H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_4COS->C_N-3R->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_3R->S_Ext-3S-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_3CH->H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_Ext-4COS-R_N-5R!H->S_N-Sp-5CCCOOOS=4CCCCOOOOSS_N-4COS->C_N-3R->S_N-3CH->H
            L4: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_5R!H->C
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_4COS->C_Ext-3S-R_N-5R!H->C
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_3R->S_N-4COS->C_Ext-3S-R
            L4: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_Sp-7R!H=5R!H_Ext-3CH-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-5R!H-R_N-Sp-7R!H=5R!H_Ext-3CH-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Ext-3CH-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_Sp-5R!H=3CCHH
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-3CH-R_N-Sp-5R!H=3CCHH
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_Sp-5R!H-3CH
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_Ext-3CH-R_N-Sp-5R!H-3CH
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_3CH->H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_4COS->C_N-3CH->H
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_3CH->H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_2R->H_N-3R->S_N-4COS->C_N-3CH->H
        L3: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H
            L4: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-5R!H-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_Ext-4COS-R_Ext-2S-R
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-3S-R_Ext-2S-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_3R->S_Ext-2S-R
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_5R!H->C
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_3CH->H_Ext-2S-R_N-5R!H->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_5R!H->C
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_2CS->S_N-3R->S_N-3CH->H_Ext-2S-R_N-5R!H->C
            L4: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_Sp-6R!H=5R!H
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Ext-4COS-R_N-Sp-6R!H=5R!H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_Sp-6R!H=5R!H
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Ext-4COS-R_N-Sp-6R!H=5R!H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_Sp-6R!H=5R!H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_Ext-5R!H-R_N-Sp-6R!H=5R!H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_3R->H
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_5R!H->S_N-3R->H
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_5CCOO->O_Ext-4COS-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_Sp-5C=4CCOOSS
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Ext-4COS-R_N-Sp-5C=4CCOOSS_Ext-4COS-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_4COS->C
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_3R->C
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C
                                        L11: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-3HS-R
                                        L11: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_Ext-2C-R
                                        L11: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_3HS->S
                                        L11: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_Sp-5C-4COS_N-4COS->C_N-3R->C_N-3HS->S
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_Ext-4COS-R_N-5R!H->S_N-5CCOO->O_N-Sp-5C-4COS
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_5R!H->C_Ext-2C-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_Sp-5R!H=2C_N-5R!H->C
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_5R!H->O
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C
                                        L11: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R
                                            L12: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C
                                        L11: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R
                                            L12: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-5C-R_N-Sp-6R!H=5C_Ext-2C-R_Ext-2C-R
                                L9: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R
                                    L10: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_4COS->C_Ext-2C-R_N-Sp-5R!H=2C_N-5R!H->O_Ext-2C-R_Ext-2C-R
                L5: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_Ext-3R-R
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_3R->C
                    L6: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R
                            L8: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_Ext-2C-R_Ext-2C-R
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_3HS->S
                        L7: Root_N-4CCCCHHHHOOOOSSSS->H_N-2R->H_N-2CS->S_N-4COS->C_N-3R->C_N-3HS->S
"""
)

