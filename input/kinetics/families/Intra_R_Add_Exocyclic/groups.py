#!/usr/bin/env python
# encoding: utf-8

name = "Intra_R_Add_Exocyclic/groups"
shortDesc = u""
longDesc = u"""

"""

template(reactants=["Root"], products=["RnCycle"], ownReverse=False)

reverse = "Ring_Open_Exo_Cycli_Radical"
reversible = True

recipe(actions=[
    ['CHANGE_BOND', '*2', -1, '*3'],
    ['FORM_BOND', '*1', 1, '*2'],
    ['LOSE_RADICAL', '*1', '1'],
    ['GAIN_RADICAL', '*3', '1'],
])

boundaryAtoms = ["*1", "*2"]

entry(
    index = 0,
    label = "Root",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]}
3 *1 R!H                          u1
""",
    kinetics = None,
)

entry(
    index = 1,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                          u1
4    C                            u0 {2,[S,D,T,B]} {5,[S,D,T,B]}
5    C                            u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 2,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3 *1 R!H                          u1
4    C                            u0 {2,S} {5,D}
5    C                            u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 3,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S} {6,[S,D,T,B]}
3 *1 C                            u1
4    C                            u0 {2,S} {5,D}
5    C                            u0 {4,D}
6    C                            u0 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 4,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 r1 {1,[D,T,B]} {4,S} {6,[S,D,T,B]}
3 *1 C                            u1 {4,[S,D,T,B]}
4    C                            u0 {2,S} {3,[S,D,T,B]} {5,D}
5    C                            u0 {4,D}
6    C                            u0 r1 {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 5,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 r1 {1,[D,T,B]} {4,S} {6,[S,D,T,B]}
3 *1 C                            u1 {8,[S,D,T,B]}
4    C                            u0 {2,S} {5,D}
5    C                            u0 {4,D} {7,S}
6    C                            u0 r1 {2,[S,D,T,B]}
7    C                            u0 {5,S}
8    R!H                          ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 6,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S} {6,S}
3 *1 C  u1
4    C  u0 {2,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 7,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r1 {1,D} {4,S} {6,S}
3 *1 C  u1 r1
4    C  u0 r1 {2,S} {5,D}
5    C  u0 r1 {4,D}
6    C  u0 r1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 8,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r1 {1,D} {4,S} {6,S}
3 *1 C  u1 r0
4    C  u0 r1 {2,S} {5,D}
5    C  u0 r1 {4,D}
6    C  u0 r1 {2,S}
""",
    kinetics = None,
)

entry(
    index = 9,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Cb u0 c0 r1 {2,B}
2 *2 Cb u0 r1 {1,B} {4,S} {6,B}
3 *1 C  u1 r0
4    C  u0 r0 {2,S} {5,D}
5    C  u0 r0 {4,D}
6    C  u0 r1 {2,B}
""",
    kinetics = None,
)

entry(
    index = 10,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd",
    group = 
"""
1 *3 Cdd                    u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 {1,[D,T,B]} {4,S}
3 *1 R!H                    u1
4    C                      u0 {2,S} {5,D}
5    C                      u0 r0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 11,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd",
    group = 
"""
1 *3 [Ct,Cb,Cd]             u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 {1,[D,T,B]} {4,S}
3 *1 C                      u1
4    C                      u0 {2,S} {5,D}
5    C                      u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 12,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R",
    group = 
"""
1 *3 [Ct,Cb,Cd]             u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 {1,[D,T,B]} {4,S}
3 *1 C                      u1
4    C                      u0 {2,S} {5,D}
5    C                      u0 {4,D} {6,[S,D,T,B]}
6    C                      u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 13,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 {2,S} {5,D}
5    C  u0 {4,D} {6,[S,D,T,B]}
6    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 14,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 {2,S} {5,D}
5    C  u0 {4,D} {6,S}
6    C  u0 {5,S}
7    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 15,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing",
    group = 
"""
1 *3 Cd u0 c0 r1 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 {2,S} {5,D}
5    C  u0 r0 {4,D} {6,S}
6    C  u0 {5,S}
7    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 16,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {7,S}
4    C  u0 r0 {2,S} {5,D}
5    C  u0 r0 {4,D} {6,S}
6    C  u0 r0 {5,S}
7    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 17,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0
4    C  u0 r0 {2,S} {5,D}
5    C  u0 r0 {4,D} {6,S}
6    C  u0 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 18,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 r0 {2,S} {5,D}
5    C  u0 {4,D} {6,D}
6    C  u0 {5,D}
""",
    kinetics = None,
)

entry(
    index = 19,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd",
    group = 
"""
1 *3 Ct                     u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 {1,[D,T,B]} {4,S}
3 *1 C                      u1
4    C                      u0 {2,S} {5,D}
5    C                      u0 r0 {4,D} {6,[S,D,T,B]}
6    C                      u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 20,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                          u1
4    C                            u0 {2,[S,D,T,B]} {5,[B,S,T]}
5    C                            u0 {4,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 21,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                          u1
4    C                            u0 {2,[S,D,T,B]} {5,[B,S,T]}
5    C                            u0 {4,[B,S,T]}
6    R!H                          ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 22,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                          u1
4    C                            u0 {2,[S,D,T,B]} {5,[B,S,T]}
5    C                            u0 {4,[B,S,T]}
6    R!H                          ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 23,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r1 {2,D} {6,[S,D,T,B]} {7,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 24,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H",
    group = 
"""
1 *3 Cb u0 c0 r1 {2,B} {6,B}
2 *2 Cb u0 {1,B} {4,B}
3 *1 C  u1 {8,D}
4    C  u0 {2,B} {5,B}
5    C  u0 {4,B}
6    C  u0 {1,B} {7,B}
7    C  u0 {6,B}
8    C  u0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 25,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cb u0 c0 r1 {2,B} {6,B}
2 *2 Cb u0 {1,B} {4,B}
3 *1 C  u1 {8,D} {9,S}
4    C  u0 {2,B} {5,B}
5    C  u0 {4,B}
6    C  u0 {1,B} {7,B}
7    C  u0 {6,B}
8    C  u0 {3,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 26,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R",
    group = 
"""
1  *3 Cb  u0 c0 r1 {2,B} {6,B}
2  *2 Cb  u0 r1 {1,B} {4,B}
3  *1 C   u1 {8,D} {9,S}
4     C   u0 r1 {2,B} {5,B}
5     C   u0 r1 {4,B}
6     C   u0 r1 {1,B} {7,B}
7     C   u0 r1 {6,B}
8     C   u0 r0 {3,D}
9     C   u0 r0 {3,S} {10,[S,D,T,B]}
10    R!H ux {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 27,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN",
    group = 
"""
1 *3 Cb u0 c0 r1 {2,B} {6,B}
2 *2 Cb u0 r1 {1,B} {4,B} {8,[S,D,T,B]}
3 *1 C  u1 {8,D} {9,S}
4    C  u0 r1 {2,B} {5,B}
5    C  u0 r1 {4,B}
6    C  u0 r1 {1,B} {7,B}
7    C  u0 r1 {6,B}
8    C  u0 {2,[S,D,T,B]} {3,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 28,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R",
    group = 
"""
1  *3 Cb  u0 c0 r1 {2,B} {6,B}
2  *2 Cb  u0 r1 {1,B} {4,B} {8,S}
3  *1 C   u1 {8,D}
4     C   u0 r1 {2,B} {5,B}
5     C   u0 r1 {4,B}
6     C   u0 r1 {1,B} {7,B}
7     C   u0 r1 {6,B}
8     C   u0 {2,S} {3,D} {9,S}
9     C   u0 r0 {8,S} {10,[S,D,T,B]}
10    R!H ux {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 29,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,[S,D,T,B]}
3 *1 R!H                          u1 {8,S}
4    C                            u0 {2,[S,D,T,B]} {5,[B,S,T]}
5    C                            u0 {4,[B,S,T]}
6    C                            u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    C                            u0 {6,[S,D,T,B]}
8    R!H                          u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 30,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3 *1 C                            u1 {8,S}
4    C                            u0 {2,S} {5,S}
5    C                            u0 {4,S} {9,[S,D,T,B]}
6    C                            u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7    C                            u0 {6,[S,D,T,B]}
8    C                            u0 {3,S}
9    C                            u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 31,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2  *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 r1 {1,[D,T,B]} {4,S}
3  *1 C                            u1 {8,S} {10,[S,D,T,B]}
4     C                            u0 {2,S} {5,S}
5     C                            u0 r0 {4,S} {9,[S,D,T,B]}
6     C                            u0 r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     C                            u0 r1 {6,[S,D,T,B]}
8     C                            u0 r0 {3,S}
9     C                            u0 r0 {5,[S,D,T,B]}
10    R!H                          ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 32,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R",
    group = 
"""
1  *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2  *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3  *1 C                            u1 {8,S}
4     C                            u0 {2,S} {5,S}
5     C                            u0 {4,S} {9,[S,D,T,B]}
6     C                            u0 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     C                            u0 {6,[S,D,T,B]}
8     C                            u0 {3,S} {10,[S,D,T,B]}
9     C                            u0 {5,[S,D,T,B]}
10    C                            u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 33,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H",
    group = 
"""
1  *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2  *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 r1 {1,[D,T,B]} {4,S}
3  *1 C                            u1 r0 {8,S}
4     C                            u0 {2,S} {5,S} {10,[S,D,T,B]}
5     C                            u0 r0 {4,S} {9,[S,D,T,B]}
6     C                            u0 r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     C                            u0 r1 {6,[S,D,T,B]}
8     C                            u0 r0 {3,S} {10,[S,D,T,B]}
9     C                            u0 r0 {5,[S,D,T,B]}
10    C                            u0 r0 {4,[S,D,T,B]} {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 34,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1  *3 Cd                     u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2  *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 r1 {1,[D,T,B]} {4,S}
3  *1 C                      u1 {8,S}
4     C                      u0 {2,S} {5,S}
5     C                      u0 {4,S} {9,[S,D,T,B]}
6     C                      u0 r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     C                      u0 r1 {6,[S,D,T,B]}
8     C                      u0 {3,S} {10,[S,D,T,B]}
9     C                      u0 {5,[S,D,T,B]}
10    C                      u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 35,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1  *3 Cb                     u0 c0 r1 {2,[D,T,B]} {6,[S,D,T,B]}
2  *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 r1 {1,[D,T,B]} {4,S}
3  *1 C                      u1 {8,S}
4     C                      u0 {2,S} {5,S}
5     C                      u0 {4,S} {9,[S,D,T,B]}
6     C                      u0 r1 {1,[S,D,T,B]} {7,[S,D,T,B]}
7     C                      u0 r1 {6,[S,D,T,B]}
8     C                      u0 {3,S} {10,[S,D,T,B]}
9     C                      u0 {5,[S,D,T,B]}
10    C                      u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 36,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R",
    group = 
"""
1  *3 Cb  u0 c0 r1 {2,B} {6,B}
2  *2 Cb  u0 r1 {1,B} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 r0 {2,S} {5,S} {10,[S,D,T,B]}
5     C   u0 {4,S} {9,S}
6     C   u0 r1 {1,B} {7,B}
7     C   u0 r1 {6,B}
8     C   u0 {3,S}
9     C   u0 {5,S}
10    R!H ux {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 37,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R",
    group = 
"""
1 *3 Cb u0 c0 r1 {2,B} {6,B}
2 *2 Cb u0 {1,B} {4,B}
3 *1 C  u1 {8,S}
4    C  u0 {2,B} {5,B}
5    C  u0 {4,B}
6    C  u0 {1,B} {7,B}
7    C  u0 {6,B}
8    C  u0 {3,S} {9,S}
9    C  u0 {8,S}
""",
    kinetics = None,
)

entry(
    index = 38,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1  *3 Cb u0 c0 r1 {2,B} {6,B}
2  *2 Cb u0 {1,B} {4,B} {10,S}
3  *1 C  u1 {8,S}
4     C  u0 {2,B} {5,B}
5     C  u0 {4,B}
6     C  u0 {1,B} {7,B}
7     C  u0 {6,B}
8     C  u0 {3,S} {9,S}
9     C  u0 {8,S}
10    C  u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 39,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cb  u0 c0 r1 {2,B} {6,B}
2  *2 Cb  u0 r1 {1,B} {4,B} {10,S}
3  *1 C   u1 {8,S} {11,[S,D,T,B]}
4     C   u0 r1 {2,B} {5,B}
5     C   u0 r1 {4,B}
6     C   u0 r1 {1,B} {7,B}
7     C   u0 r1 {6,B}
8     C   u0 {3,S} {9,S}
9     C   u0 {8,S}
10    C   u0 {2,S}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 40,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R",
    group = 
"""
1  *3 Cb  u0 c0 r1 {2,B} {6,B}
2  *2 Cb  u0 r1 {1,B} {4,B}
3  *1 C   u1 {8,S}
4     C   u0 r1 {2,B} {5,B}
5     C   u0 r1 {4,B}
6     C   u0 r1 {1,B} {7,B}
7     C   u0 r1 {6,B}
8     C   u0 {3,S} {9,S}
9     C   u0 {8,S} {10,[S,D,T,B]}
10    R!H ux {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 41,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 Cb  u0 c0 r1 {2,B} {6,B}
2 *2 Cb  u0 r1 {1,B} {4,B} {9,[S,D,T,B]}
3 *1 R!H u1 {8,S}
4    C   u0 r1 {2,B} {5,B}
5    C   u0 r1 {4,B}
6    C   u0 r1 {1,B} {7,B}
7    C   u0 r1 {6,B}
8    R!H u0 {3,S}
9    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 42,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 43,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 44,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    C   u0 {1,S} {7,[S,D,T,B]}
7    C   u0 {6,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 45,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 46,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {9,S}
6    C  u0 {1,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {3,S} {9,S}
9    C  u0 {5,S} {8,S}
""",
    kinetics = None,
)

entry(
    index = 47,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,[S,D,T,B]}
7     C   u0 {6,[S,D,T,B]}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 48,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,[S,D,T,B]}
11    C  u0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 49,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,[S,D,T,B]}
11    C  u0 {10,[S,D,T,B]}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 50,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 51,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 52,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {13,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S} {12,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    C   u0 r0 {3,S} {11,D}
11    C   u0 {10,D}
12    C   u0 r0 {3,S}
13    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 53,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 54,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {13,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S} {12,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    C   u0 r0 {3,S} {11,D}
11    C   u0 {10,D}
12    C   u0 r0 {3,S}
13    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 55,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 56,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 57,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {13,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S} {12,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    C   u0 r0 {3,S} {11,T}
11    C   u0 {10,T}
12    C   u0 r0 {3,S}
13    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 58,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {12,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 59,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {13,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S} {12,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    C   u0 r0 {3,S} {11,T}
11    C   u0 {10,T}
12    C   u0 r0 {3,S}
13    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 60,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,[S,D,T,B]}
11    C  u0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 61,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
""",
    kinetics = None,
)

entry(
    index = 62,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    C   u0 {3,S} {11,D}
11    C   u0 {10,D}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 63,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
""",
    kinetics = None,
)

entry(
    index = 64,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    C   u0 {3,S} {11,T}
11    C   u0 {10,T}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 65,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,[S,D,T,B]}
11    C  u0 {10,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 66,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {12,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,[S,D,T,B]}
11    C  u0 {10,[S,D,T,B]}
12    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 67,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {12,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 68,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {12,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
12    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 69,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,D}
11    C  u0 {10,D}
""",
    kinetics = None,
)

entry(
    index = 70,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S} {11,T}
11    C  u0 {10,T}
""",
    kinetics = None,
)

entry(
    index = 71,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,[S,D,T,B]}
7     C   u0 {6,[S,D,T,B]}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 72,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 73,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 74,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 75,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,[S,D,T,B]} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,S}
9     C   u0 {5,S} {8,S}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 76,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 77,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,S}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    C   u0 r0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 78,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {9,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,S}
9     C  u0 {5,S} {8,S}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 79,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,S}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    C   u0 r0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 80,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {9,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,S}
9    C  u0 {5,S} {8,S}
""",
    kinetics = None,
)

entry(
    index = 81,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,S}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 82,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {9,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {9,S}
9    C  u0 {5,S} {8,S}
""",
    kinetics = None,
)

entry(
    index = 83,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,S}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {9,S}
9     C   u0 r0 {5,S} {8,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 84,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,[S,D,T,B]}
9     C  u0 {8,[S,D,T,B]}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 85,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 86,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {3,S} {4,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 87,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {3,S} {4,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 88,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {3,S} {4,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 89,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {3,S} {4,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 90,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {3,S} {4,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 91,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 92,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 93,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 94,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S} {5,S}
11    C   u0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 95,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 96,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S} {5,S}
11    C   u0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 97,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 98,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {10,S}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S} {5,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 99,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 100,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {10,S}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S} {5,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 101,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 102,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 103,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 104,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,D}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S} {5,D}
11    C   u0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 105,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 106,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,D}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    C   u0 {3,S} {5,D}
11    C   u0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 107,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 108,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {10,D}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S} {5,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 109,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 110,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {10,D}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {9,D}
9     C   u0 r0 {8,D}
10    C   u0 r0 {3,S} {5,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 111,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 112,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {3,S} {4,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 113,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {3,S} {4,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 114,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {3,S} {4,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 115,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {5,S} {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {3,S} {4,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 116,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {5,S} {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {3,S} {4,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 117,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 118,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 119,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,S}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 120,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,S}
11    C   u0 r0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 121,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 122,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 123,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {11,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,S}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 124,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {12,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,S}
11    C   u0 r0 {1,S}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 125,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,S}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 126,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,[S,D,T,B]}
7     C  u0 {6,[S,D,T,B]}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 127,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 128,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S} {11,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,D}
7     C  u0 {6,D}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,D}
11    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 129,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {12,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,D}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,D}
11    C   u0 r0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 130,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,D}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 131,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 132,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {11,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {10,D}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 {3,S} {5,D}
11    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 133,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {12,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,D}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,D}
11    C   u0 r0 {1,S}
12    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 134,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {10,S} {11,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {10,D}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    C   u0 {3,S} {5,D}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 135,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 136,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 137,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,D}
9     C   u0 {8,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 138,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 139,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {9,T}
9     C   u0 {8,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 140,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {9,[S,D,T,B]}
9    C  u0 {8,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 141,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {10,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,[S,D,T,B]}
9     C  u0 {8,[S,D,T,B]}
10    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 142,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {10,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,D}
9     C  u0 {8,D}
10    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 143,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S} {10,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {8,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {1,S} {7,T}
7     C  u0 {6,T}
8     C  u0 {3,S} {9,T}
9     C  u0 {8,T}
10    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 144,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {9,D}
9    C  u0 {8,D}
""",
    kinetics = None,
)

entry(
    index = 145,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {9,T}
9    C  u0 {8,T}
""",
    kinetics = None,
)

entry(
    index = 146,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    C   u0 {1,S} {7,[S,D,T,B]}
7    C   u0 {6,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 147,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    C   u0 {1,S} {7,[S,D,T,B]}
7    C   u0 {6,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 148,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    C   u0 {1,S} {7,D}
7    C   u0 {6,D}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 149,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {3,S} {4,S}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 150,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    C   u0 {1,S} {7,T}
7    C   u0 {6,T}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 151,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {5,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {3,S} {4,S}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 152,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {5,S} {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {3,S} {4,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 153,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {5,S} {8,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {3,S} {4,S}
6    C   u0 r0 {1,S} {7,D}
7    C   u0 r0 {6,D}
8    C   u0 r0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 154,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {5,S} {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {3,S} {4,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 155,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {5,S} {8,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {3,S} {4,S}
6    C   u0 r0 {1,S} {7,T}
7    C   u0 r0 {6,T}
8    C   u0 r0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 156,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,S}
6    C  u0 {1,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 157,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {8,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {8,S}
6    C   u0 {1,S} {7,[S,D,T,B]}
7    C   u0 {6,[S,D,T,B]}
8    C   u0 {3,S} {5,S}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 158,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     C   u0 {1,S} {7,[S,D,T,B]}
7     C   u0 {6,[S,D,T,B]}
8     C   u0 {3,S} {5,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 159,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {5,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 160,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {5,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 161,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {5,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 162,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {5,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 163,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S} {9,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {5,S}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 164,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {5,S}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 165,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S} {9,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {5,S}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 166,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {5,S}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 167,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 168,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {8,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S} {8,S}
6    C   u0 r0 {1,S} {7,D}
7    C   u0 r0 {6,D}
8    C   u0 r0 {3,S} {5,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 169,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 170,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {8,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S} {8,S}
6    C   u0 r0 {1,S} {7,T}
7    C   u0 r0 {6,T}
8    C   u0 r0 {3,S} {5,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 171,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,D}
6    C  u0 {1,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
8    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 172,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {8,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {8,D}
6    C   u0 {1,S} {7,[S,D,T,B]}
7    C   u0 {6,[S,D,T,B]}
8    C   u0 {3,S} {5,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 173,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,D}
6     C   u0 {1,S} {7,[S,D,T,B]}
7     C   u0 {6,[S,D,T,B]}
8     C   u0 {3,S} {5,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 174,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,D}
6     C   u0 {1,S} {7,D}
7     C   u0 {6,D}
8     C   u0 {3,S} {5,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 175,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,D}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {5,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 176,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,D}
6     C   u0 {1,S} {7,T}
7     C   u0 {6,T}
8     C   u0 {3,S} {5,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 177,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,D}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {5,D}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 178,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S} {9,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,D}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {5,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 179,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,D}
6     C   u0 r0 {1,S} {7,D}
7     C   u0 r0 {6,D}
8     C   u0 r0 {3,S} {5,D}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 180,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S} {9,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,D}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {5,D}
9    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 181,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {8,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,D}
6     C   u0 r0 {1,S} {7,T}
7     C   u0 r0 {6,T}
8     C   u0 r0 {3,S} {5,D}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 182,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,D}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
8    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 183,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {8,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S} {8,D}
6    C   u0 r0 {1,S} {7,D}
7    C   u0 r0 {6,D}
8    C   u0 r0 {3,S} {5,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 184,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {8,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {8,D}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 185,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {8,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S} {8,D}
6    C   u0 r0 {1,S} {7,T}
7    C   u0 r0 {6,T}
8    C   u0 r0 {3,S} {5,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 186,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 187,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {8,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S}
6    C   u0 r0 {1,S} {7,D}
7    C   u0 r0 {6,D}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 188,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 189,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {8,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S}
6    C   u0 r0 {1,S} {7,T}
7    C   u0 r0 {6,T}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 190,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 191,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,[S,D,T,B]}
8    C   u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 192,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {8,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,S}
8    C   u0 {5,S} {7,S}
""",
    kinetics = None,
)

entry(
    index = 193,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {8,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,S}
8    C   u0 {5,S} {7,S}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 194,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,[S,D,T,B]}
10    C   u0 {9,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 195,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,[S,D,T,B]}
10    C   u0 {9,[S,D,T,B]}
11    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 196,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,D}
10    C   u0 {9,D}
11    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 197,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {12,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S} {11,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,D}
10    C   u0 r0 {9,D}
11    C   u0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 198,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {11,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,T}
10    C   u0 {9,T}
11    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 199,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {12,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S} {11,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,T}
10    C   u0 r0 {9,T}
11    C   u0 {3,S}
12    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 200,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {11,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S} {10,[S,D,T,B]}
10    C   u0 {9,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 201,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 r0 {5,S} {7,S}
9     C   u0 r0 {3,S} {10,D}
10    C   u0 r0 {9,D}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 202,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 r0 {5,S} {7,S}
9     C   u0 r0 {3,S} {10,T}
10    C   u0 r0 {9,T}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 203,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {8,S}
6     C  u0 {1,S}
7     C  u0 {3,S} {8,S}
8     C  u0 {5,S} {7,S}
9     C  u0 {3,S} {10,D}
10    C  u0 {9,D}
""",
    kinetics = None,
)

entry(
    index = 204,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D} {6,S}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {7,S} {9,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S} {8,S}
6     C  u0 {1,S}
7     C  u0 {3,S} {8,S}
8     C  u0 {5,S} {7,S}
9     C  u0 {3,S} {10,T}
10    C  u0 {9,T}
""",
    kinetics = None,
)

entry(
    index = 205,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 206,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,[S,D,T,B]} {10,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,S}
8     C   u0 r0 {5,S} {7,S}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {3,[S,D,T,B]}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 207,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {8,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,S}
8     C   u0 {5,S} {7,S}
9     C   u0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 208,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {8,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,S}
8    C   u0 {5,S} {7,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 209,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,[S,D,T,B]}
8    C   u0 {7,[S,D,T,B]}
9    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 210,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,D}
8    C   u0 {7,D}
9    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 211,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,D}
8    C   u0 {7,D}
9    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 212,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {5,S} {7,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {3,S} {4,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 213,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {9,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,D}
8    C   u0 {7,D}
9    C   u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 214,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {5,S}
10    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 215,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     C   u0 r0 {3,S} {5,S}
10    C   u0 r0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 216,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {5,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 217,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {9,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,D}
8    C   u0 {7,D}
9    C   u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 218,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {10,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,D}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {5,D}
10    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 219,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {11,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S} {10,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,D}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,D}
8     C   u0 r0 {7,D}
9     C   u0 r0 {3,S} {5,D}
10    C   u0 r0 {3,S}
11    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 220,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,D}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,D}
8     C   u0 {7,D}
9     C   u0 {3,S} {5,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 221,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,T}
8    C   u0 {7,T}
9    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 222,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,T}
8    C   u0 {7,T}
9    C   u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 223,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {5,S} {7,S} {9,S}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {3,S} {4,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     C   u0 r0 {3,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 224,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {9,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,T}
8    C   u0 {7,T}
9    C   u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 225,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {3,S} {5,S}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 226,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     C   u0 r0 {3,S} {5,S}
10    R!H ux {1,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 227,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,S}
6     C   u0 {1,S}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {3,S} {5,S}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 228,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {9,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {9,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,T}
8    C   u0 {7,T}
9    C   u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 229,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,D}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {3,S} {5,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 230,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {4,S}
3  *1 C   u1 r0 {7,S} {9,S} {11,[S,D,T,B]}
4     C   u0 r0 {2,S} {5,S}
5     C   u0 r0 {4,S} {9,D}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 r0 {3,S} {8,T}
8     C   u0 r0 {7,T}
9     C   u0 r0 {3,S} {5,D}
10    R!H ux {1,[S,D,T,B]}
11    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 231,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {9,S} {10,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {9,D}
6     C   u0 {1,S}
7     C   u0 {3,S} {8,T}
8     C   u0 {7,T}
9     C   u0 {3,S} {5,D}
10    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 232,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {8,[S,D,T,B]}
8    C   u0 {7,[S,D,T,B]}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 233,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {7,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 r0 {3,S} {8,D}
8    C   u0 r0 {7,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 234,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {4,S}
3 *1 C   u1 r0 {7,S}
4    C   u0 r0 {2,S} {5,S}
5    C   u0 r0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 r0 {3,S} {8,T}
8    C   u0 r0 {7,T}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 235,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,D}
8    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 236,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {1,S}
7    C  u0 {3,S} {8,[S,T]}
8    C  u0 {7,[S,T]}
""",
    kinetics = None,
)

entry(
    index = 237,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 238,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 239,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,[S,D,T,B]} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 240,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {8,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {5,S} {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,S} {4,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 241,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 242,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 243,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,S}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 244,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {7,S}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {5,S}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 245,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,S}
8    C   u0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 246,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {8,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,S}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 247,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 248,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,D}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 249,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,D}
8    R!H ux {3,[S,D,T,B]}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 250,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {10,[S,D,T,B]}
2  *2 Cd  u0 {1,D} {4,S}
3  *1 C   u1 {7,S} {8,[S,D,T,B]} {9,[S,D,T,B]}
4     C   u0 {2,S} {5,S}
5     C   u0 {4,S} {7,D}
6     R!H ux {1,[S,D,T,B]}
7     C   u0 {3,S} {5,D}
8     R!H ux {3,[S,D,T,B]}
9     R!H ux {3,[S,D,T,B]}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 251,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S} {8,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,D}
8    C   u0 {3,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 252,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {8,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S} {5,D}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 253,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {7,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 254,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3 *1 R!H                          u1 {6,[S,D,T,B]}
4    C                            u0 {2,S} {5,[B,S,T]}
5    C                            u0 {4,[B,S,T]}
6    R!H                          ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 255,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 256,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    C   u0 {3,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 257,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {6,S} {7,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    C   u0 {3,S} {8,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {6,S}
""",
    kinetics = None,
)

entry(
    index = 258,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,S} {8,S}
7    C  u0 {3,S} {9,[S,D,T,B]}
8    C  u0 {6,S}
9    C  u0 {7,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 259,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R",
    group = 
"""
1  *3 Cd u0 c0 {2,D}
2  *2 Cd u0 {1,D} {4,S}
3  *1 C  u1 {6,S} {7,S} {10,S}
4     C  u0 {2,S} {5,S}
5     C  u0 {4,S}
6     C  u0 {3,S} {8,S}
7     C  u0 {3,S} {9,[S,D,T,B]}
8     C  u0 {6,S}
9     C  u0 {7,[S,D,T,B]}
10    C  u0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 260,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D}
2  *2 Cd u0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {6,S} {7,S} {10,S}
4     C  u0 r0 {2,S} {5,S}
5     C  u0 r0 {4,S}
6     C  u0 r0 {3,S} {8,S}
7     C  u0 r0 {3,S} {9,D}
8     C  u0 r0 {6,S}
9     C  u0 {7,D}
10    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 261,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H",
    group = 
"""
1  *3 Cd u0 c0 r0 {2,D}
2  *2 Cd u0 r0 {1,D} {4,S}
3  *1 C  u1 r0 {6,S} {7,S} {10,S}
4     C  u0 r0 {2,S} {5,S}
5     C  u0 r0 {4,S}
6     C  u0 r0 {3,S} {8,S}
7     C  u0 r0 {3,S} {9,T}
8     C  u0 r0 {6,S}
9     C  u0 {7,T}
10    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 262,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,S} {8,S}
7    C  u0 {3,S} {9,D}
8    C  u0 {6,S}
9    C  u0 {7,D}
""",
    kinetics = None,
)

entry(
    index = 263,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,S} {8,S}
7    C  u0 {3,S} {9,T}
8    C  u0 {6,S}
9    C  u0 {7,T}
""",
    kinetics = None,
)

entry(
    index = 264,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {6,S} {7,[S,D,T,B]} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S}
6    C   u0 {3,S} {8,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {6,S}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 265,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,[S,D,T,B]} {8,[B,D,T]}
7    C  u0 {3,[S,D,T,B]}
8    C  u0 {6,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 266,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r1 {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {4,S}
6    C  u0 {3,[S,D,T,B]} {8,[B,D,T]}
7    C  u0 {3,[S,D,T,B]}
8    C  u0 {6,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 267,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,S} {8,[B,D,T]}
7    C  u0 {3,S}
8    C  u0 {6,[B,D,T]}
""",
    kinetics = None,
)

entry(
    index = 268,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,S} {8,D}
7    C  u0 {3,S}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 269,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,[S,D,T,B]} {6,S} {7,S}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {3,[S,D,T,B]} {4,S}
6    C  u0 {3,S} {8,D}
7    C  u0 {3,S}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 270,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {7,S}
6    C  u0 {3,S} {8,D}
7    C  u0 {3,S} {5,S}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 271,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {6,S} {7,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    C   u0 {3,S} {8,D}
7    C   u0 {3,S} {5,S}
8    C   u0 {6,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 272,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {7,D}
6    C  u0 {3,S} {8,D}
7    C  u0 {3,S} {5,D}
8    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 273,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {6,S} {7,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    C   u0 {3,S} {8,D}
7    C   u0 {3,S} {5,D}
8    C   u0 {6,D}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 274,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 {3,S} {8,T}
7    C  u0 {3,S}
8    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 275,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,[S,D,T,B]} {6,S} {7,S}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {3,[S,D,T,B]} {4,S}
6    C  u0 {3,S} {8,T}
7    C  u0 {3,S}
8    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 276,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {7,S}
6    C  u0 {3,S} {8,T}
7    C  u0 {3,S} {5,S}
8    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 277,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {6,S} {7,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    C   u0 {3,S} {8,T}
7    C   u0 {3,S} {5,S}
8    C   u0 {6,T}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 278,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S} {7,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {4,S} {7,D}
6    C  u0 {3,S} {8,T}
7    C  u0 {3,S} {5,D}
8    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 279,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {6,S} {7,S} {9,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    C   u0 {3,S} {8,T}
7    C   u0 {3,S} {5,D}
8    C   u0 {6,T}
9    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 280,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {5,[S,D,T,B]} {6,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {3,[S,D,T,B]} {4,S}
6    R!H ux {3,[S,D,T,B]}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 281,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {6,[S,D,T,B]} {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 282,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {6,[S,D,T,B]} {7,S} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,S}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {3,S} {5,S}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 283,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 {6,[S,D,T,B]} {7,S}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 284,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 C   u1 r0 {6,[S,D,T,B]} {7,S} {8,[S,D,T,B]}
4    C   u0 {2,S} {5,S}
5    C   u0 {4,S} {7,D}
6    R!H ux {3,[S,D,T,B]}
7    C   u0 r0 {3,S} {5,D}
8    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 285,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 R!H u1 {6,[S,D,T,B]}
4    C   u0 {2,S} {5,[B,S,T]}
5    C   u0 {4,[B,S,T]}
6    C   u0 r1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 286,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {4,S}
3 *1 R!H u1 {6,[S,D,T,B]}
4    C   u0 {2,S} {5,[B,S,T]}
5    C   u0 r1 {4,[B,S,T]}
6    C   u0 r1 {3,[S,D,T,B]} {7,[S,D,T,B]} {8,[S,D,T,B]}
7    R!H ux {6,[S,D,T,B]}
8    R!H ux {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 287,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r1 {6,[S,D,T,B]}
4    C  u0 {2,S} {5,[B,S,T]}
5    C  u0 r1 {4,[B,S,T]}
6    C  u0 r1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 288,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 r0 {6,[S,D,T,B]}
4    C  u0 {2,S} {5,[B,S,T]}
5    C  u0 r1 {4,[B,S,T]}
6    C  u0 r1 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 289,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3 *1 C                            u1 {6,[S,D,T,B]}
4    C                            u0 {2,S} {5,[B,S,T]}
5    C                            u0 {4,[B,S,T]}
6    C                            u0 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 290,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,[S,D,T,B]}
4    C  u0 {2,S} {5,[B,S,T]}
5    C  u0 {4,[B,S,T]}
6    C  u0 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 291,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {3,S} {4,S}
6    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 292,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {3,S} {4,S}
6    C  u0 r0 {3,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 293,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {3,S} {4,S}
6    C  u0 r0 {3,S} {7,D}
7    C  u0 r0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 294,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {5,S} {6,S}
4    C  u0 {2,S} {5,S}
5    C  u0 {3,S} {4,S}
6    C  u0 r0 {3,S} {7,[B,S,T]}
7    C  u0 r0 {6,[B,S,T]}
""",
    kinetics = None,
)

entry(
    index = 295,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,[S,D,T,B]}
4    C  u0 r1 {2,S} {5,B}
5    C  u0 {4,B}
6    C  u0 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 296,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_Sp-6R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r1 {2,S} {5,B}
5    C  u0 r1 {4,B}
6    C  u0 r0 {3,S}
""",
    kinetics = None,
)

entry(
    index = 297,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,D}
4    C  u0 r1 {2,S} {5,B}
5    C  u0 r1 {4,B}
6    C  u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 298,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,[S,D,T,B]}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 {4,S}
6    C  u0 r0 {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 299,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,[S,D,T,B]}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 {4,S} {7,[S,D,T,B]}
6    C  u0 r0 {3,[S,D,T,B]}
7    C  u0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 300,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {4,S} {7,S}
6    C  u0 r0 {3,S}
7    C  u0 r0 {5,S}
""",
    kinetics = None,
)

entry(
    index = 301,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,D}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 {4,S} {7,[S,D,T,B]}
6    C  u0 r0 {3,D}
7    C  u0 r0 {5,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 302,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D} {4,S}
3 *1 C  u1 {6,[S,D,T,B]}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 {4,S} {6,S}
6    C  u0 r0 {3,[S,D,T,B]} {5,S}
""",
    kinetics = None,
)

entry(
    index = 303,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {4,S} {6,S}
6    C  u0 r0 {3,S} {5,S}
""",
    kinetics = None,
)

entry(
    index = 304,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,D}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {4,S} {6,S}
6    C  u0 r0 {3,D} {5,S}
""",
    kinetics = None,
)

entry(
    index = 305,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {6,S}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {4,S} {6,D}
6    C  u0 r0 {3,S} {5,D}
""",
    kinetics = None,
)

entry(
    index = 306,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Ct u0 c0 {2,T}
2 *2 Ct u0 {1,T} {4,S}
3 *1 C  u1 {6,D}
4    C  u0 {2,S} {5,[B,S,T]}
5    C  u0 {4,[B,S,T]}
6    C  u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 307,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing",
    group = 
"""
1 *3 Ct u0 c0 {2,T}
2 *2 Ct u0 {1,T} {4,S}
3 *1 C  u1 {6,D}
4    C  u0 r1 {2,S} {5,[B,S,T]}
5    C  u0 {4,[B,S,T]}
6    C  u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 308,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing",
    group = 
"""
1 *3 Ct u0 c0 {2,T}
2 *2 Ct u0 {1,T} {4,S}
3 *1 C  u1 {6,D}
4    C  u0 r0 {2,S} {5,[B,S,T]}
5    C  u0 {4,[B,S,T]}
6    C  u0 r0 {3,D}
""",
    kinetics = None,
)

entry(
    index = 309,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3 *1 C                            u1
4    C                            u0 {2,S} {5,S}
5    C                            u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 310,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]} {4,S}
3 *1 C                            u1 {4,[S,D,T,B]}
4    C                            u0 {2,S} {3,[S,D,T,B]} {5,S}
5    C                            u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 311,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Cd                     u0 c0 r0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 r0 {1,[D,T,B]} {4,S}
3 *1 C                      u1 r0 {4,[S,D,T,B]}
4    C                      u0 r0 {2,S} {3,[S,D,T,B]} {5,S}
5    C                      u0 r1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 312,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Ct                     u0 c0 r0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 r0 {1,[D,T,B]} {4,S}
3 *1 C                      u1 r0 {4,[S,D,T,B]}
4    C                      u0 r0 {2,S} {3,[S,D,T,B]} {5,S}
5    C                      u0 r1 {4,S}
""",
    kinetics = None,
)

entry(
    index = 313,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,S}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {3,S} {4,S}
""",
    kinetics = None,
)

entry(
    index = 314,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D}
2 *2 Cd u0 r0 {1,D} {4,S}
3 *1 C  u1 r0 {5,D}
4    C  u0 r0 {2,S} {5,S}
5    C  u0 r0 {3,D} {4,S}
""",
    kinetics = None,
)

entry(
    index = 315,
    label = "Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 r0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 r0 {1,[D,T,B]} {4,S}
3 *1 O                            u1 r0
4    C                            u0 r0 {2,S} {5,S}
5    C                            u0 {4,S}
""",
    kinetics = None,
)

entry(
    index = 316,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]}
3 *1 C                            u1 {4,S}
4    C                            u0 {3,S} {5,[S,D,T,B]}
5    C                            u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 317,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {5,[S,D,T,B]}
5    C   u0 {4,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 318,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {8,S}
3 *1 C   u1 {4,S} {7,S}
4    C   u0 {3,S} {5,[S,D,T,B]}
5    C   u0 {4,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S}
8    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 319,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {8,S}
3 *1 C   u1 {4,S} {7,S}
4    C   u0 {3,S} {5,D}
5    C   u0 {4,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S}
8    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 320,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {8,S}
3 *1 C  u1 {4,S} {7,S}
4    C  u0 {3,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {1,S} {9,[S,D,T,B]}
7    C  u0 {3,S}
8    C  u0 {2,S}
9    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 321,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {8,S}
3 *1 C  u1 {4,S} {7,S}
4    C  u0 {3,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {1,S} {9,D}
7    C  u0 {3,S}
8    C  u0 {2,S}
9    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 322,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {8,S}
3  *1 C   u1 r0 {4,S} {7,S}
4     C   u0 {3,S} {5,D}
5     C   u0 {4,D}
6     C   u0 {1,S} {9,D}
7     C   u0 r0 {3,S}
8     C   u0 {2,S}
9     C   u0 {6,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 323,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {8,S}
3 *1 C  u1 {4,S} {7,S}
4    C  u0 {3,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {1,S} {9,T}
7    C  u0 {3,S}
8    C  u0 {2,S}
9    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 324,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {8,S}
3  *1 C   u1 r0 {4,S} {7,S}
4     C   u0 {3,S} {5,D}
5     C   u0 {4,D}
6     C   u0 {1,S} {9,T}
7     C   u0 r0 {3,S}
8     C   u0 {2,S}
9     C   u0 {6,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 325,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {8,S}
3 *1 C   u1 {4,S} {7,S}
4    C   u0 {3,S} {5,D}
5    C   u0 {4,D}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S}
8    C   u0 {2,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 326,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {8,S}
3 *1 C   u1 {4,S} {7,S}
4    C   u0 {3,S} {5,T}
5    C   u0 {4,T}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S}
8    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 327,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {8,S}
3 *1 C  u1 {4,S} {7,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
6    C  u0 {1,S} {9,[S,D,T,B]}
7    C  u0 {3,S}
8    C  u0 {2,S}
9    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 328,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {8,S}
3 *1 C  u1 {4,S} {7,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
6    C  u0 {1,S} {9,D}
7    C  u0 {3,S}
8    C  u0 {2,S}
9    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 329,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {8,S}
3  *1 C   u1 r0 {4,S} {7,S}
4     C   u0 {3,S} {5,T}
5     C   u0 {4,T}
6     C   u0 {1,S} {9,D}
7     C   u0 r0 {3,S}
8     C   u0 {2,S}
9     C   u0 {6,D}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 330,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D} {8,S}
3 *1 C  u1 {4,S} {7,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
6    C  u0 {1,S} {9,T}
7    C  u0 {3,S}
8    C  u0 {2,S}
9    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 331,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1  *3 Cd  u0 c0 r0 {2,D} {6,S} {10,[S,D,T,B]}
2  *2 Cd  u0 r0 {1,D} {8,S}
3  *1 C   u1 r0 {4,S} {7,S}
4     C   u0 {3,S} {5,T}
5     C   u0 {4,T}
6     C   u0 {1,S} {9,T}
7     C   u0 r0 {3,S}
8     C   u0 {2,S}
9     C   u0 {6,T}
10    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 332,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]} {9,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {8,S}
3 *1 C   u1 {4,S} {7,S}
4    C   u0 {3,S} {5,T}
5    C   u0 {4,T}
6    R!H ux {1,[S,D,T,B]}
7    C   u0 {3,S}
8    C   u0 {2,S}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 333,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,[S,D,T,B]}
5    C  u0 {4,[S,D,T,B]}
6    C  u0 {1,S} {7,[S,D,T,B]}
7    C  u0 {6,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 334,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,[S,D,T,B]}
5    C  u0 {4,[S,D,T,B]}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 335,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 336,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {8,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {5,D}
5    C   u0 r0 {4,D}
6    C   u0 r0 {1,S} {7,D}
7    C   u0 r0 {6,D}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 337,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
6    C  u0 {1,S} {7,D}
7    C  u0 {6,D}
""",
    kinetics = None,
)

entry(
    index = 338,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,S} {8,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {5,T}
5    C   u0 r0 {4,T}
6    C   u0 r0 {1,S} {7,D}
7    C   u0 r0 {6,D}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 339,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,[S,D,T,B]}
5    C  u0 {4,[S,D,T,B]}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 340,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S} {8,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,[S,D,T,B]}
5    C  u0 {4,[S,D,T,B]}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
8    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 341,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S} {8,S}
2 *2 Cd u0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r0 {3,S} {5,D}
5    C  u0 r0 {4,D}
6    C  u0 r0 {1,S} {7,T}
7    C  u0 r0 {6,T}
8    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 342,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 r0 {2,D} {6,S} {8,S}
2 *2 Cd u0 r0 {1,D}
3 *1 C  u1 r0 {4,S}
4    C  u0 r0 {3,S} {5,T}
5    C  u0 r0 {4,T}
6    C  u0 r0 {1,S} {7,T}
7    C  u0 r0 {6,T}
8    C  u0 r0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 343,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 344,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
6    C  u0 {1,S} {7,T}
7    C  u0 {6,T}
""",
    kinetics = None,
)

entry(
    index = 345,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {6,[S,D,T,B]} {7,[S,D,T,B]}
2 *2 Cd  u0 {1,D}
3 *1 C   u1 {4,S}
4    C   u0 {3,S} {5,[S,D,T,B]}
5    C   u0 {4,[S,D,T,B]}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 346,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {7,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {5,D}
5    C   u0 r0 {4,D}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 347,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {6,[S,D,T,B]} {7,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D}
3 *1 C   u1 r0 {4,S}
4    C   u0 r0 {3,S} {5,T}
5    C   u0 r0 {4,T}
6    R!H ux {1,[S,D,T,B]}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 348,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,D}
5    C  u0 {4,D}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 349,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {6,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
6    C  u0 {1,S}
""",
    kinetics = None,
)

entry(
    index = 350,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 {3,S} {5,T}
5    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 351,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {7,[S,D,T,B]}
3 *1 C   u1 {4,S} {6,S}
4    C   u0 {3,S} {5,T}
5    C   u0 {4,T}
6    C   u0 r0 {3,S}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 352,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]}
3 *1 C                            u1 {4,S}
4    C                            u0 {3,S} {5,[B,D]}
5    C                            u0 {4,[B,D]}
""",
    kinetics = None,
)

entry(
    index = 353,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing",
    group = 
"""
1 *3 [Cd,Ct,Cb,Cbf,O2d,S2d,Cdd,N] u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N]       u0 {1,[D,T,B]}
3 *1 C                            u1 {4,S}
4    C                            u0 r1 {3,S} {5,B}
5    C                            u0 {4,B}
""",
    kinetics = None,
)

entry(
    index = 354,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Cd                     u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 {1,[D,T,B]}
3 *1 C                      u1 {4,S}
4    C                      u0 r1 {3,S} {5,B}
5    C                      u0 r1 {4,B}
""",
    kinetics = None,
)

entry(
    index = 355,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd",
    group = 
"""
1 *3 Ct                     u0 c0 {2,[D,T,B]}
2 *2 [Cd,Ct,Cb,Cbf,CO,CS,N] u0 {1,[D,T,B]}
3 *1 C                      u1 {4,S}
4    C                      u0 r1 {3,S} {5,B}
5    C                      u0 r1 {4,B}
""",
    kinetics = None,
)

entry(
    index = 356,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing",
    group = 
"""
1 *3 Cd u0 c0 {2,D}
2 *2 Cd u0 {1,D}
3 *1 C  u1 {4,S}
4    C  u0 r0 {3,S} {5,D}
5    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 357,
    label = "Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D}
2 *2 Cd  u0 r0 {1,D} {7,[S,D,T,B]}
3 *1 C   u1 r0 {4,S} {6,S}
4    C   u0 r0 {3,S} {5,D}
5    C   u0 {4,D}
6    C   u0 r0 {3,S}
7    R!H ux {2,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 358,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,[S,D,T,B]}
2 *2 Cd  u0 {1,D}
3 *1 C   u1
4    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 359,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,[S,D,T,B]}
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 360,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 361,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {1,S} {8,[S,D,T,B]}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 362,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {1,S} {8,D}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 363,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {4,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {6,S}
3 *1 C   u1 r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {1,S} {8,D}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {4,D}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 364,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {1,S} {8,T}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 365,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D} {4,S} {9,[S,D,T,B]}
2 *2 Cd  u0 r0 {1,D} {6,S}
3 *1 C   u1 r0 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    C   u0 {1,S} {8,T}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
8    C   u0 {4,T}
9    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 366,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,[S,D,T,B]} {8,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,[S,D,T,B]} {7,[S,D,T,B]}
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {3,[S,D,T,B]}
6    C   u0 {2,S}
7    R!H ux {3,[S,D,T,B]}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 367,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {4,S}
2 *2 Cd u0 {1,D} {6,S}
3 *1 C  u1 {5,S}
4    C  u0 {1,S} {7,[S,D,T,B]}
5    C  u0 {3,S}
6    C  u0 {2,S}
7    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 368,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {4,S}
2 *2 Cd u0 {1,D} {6,S}
3 *1 C  u1 {5,S}
4    C  u0 {1,S} {7,D}
5    C  u0 {3,S}
6    C  u0 {2,S}
7    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 369,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S} {8,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,S}
4    C   u0 {1,S} {7,D}
5    C   u0 {3,S}
6    C   u0 {2,S}
7    C   u0 {4,D}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 370,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {4,S}
2 *2 Cd u0 {1,D} {6,S}
3 *1 C  u1 {5,S}
4    C  u0 {1,S} {7,T}
5    C  u0 {3,S}
6    C  u0 {2,S}
7    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 371,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S} {8,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,S}
4    C   u0 {1,S} {7,T}
5    C   u0 {3,S}
6    C   u0 {2,S}
7    C   u0 {4,T}
8    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 372,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,[S,D,T,B]} {7,[S,D,T,B]}
2 *2 Cd  u0 {1,D} {6,S}
3 *1 C   u1 {5,S}
4    R!H ux {1,[S,D,T,B]}
5    C   u0 {3,S}
6    C   u0 {2,S}
7    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 373,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {4,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1
4    C  u0 {1,S} {5,[S,D,T,B]}
5    C  u0 {4,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 374,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {4,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1
4    C  u0 {1,S} {5,D}
5    C  u0 {4,D}
""",
    kinetics = None,
)

entry(
    index = 375,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D}
3 *1 C   u1
4    C   u0 {1,S} {5,D}
5    C   u0 {4,D}
6    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 376,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H",
    group = 
"""
1 *3 Cd u0 c0 {2,D} {4,S}
2 *2 Cd u0 {1,D}
3 *1 C  u1
4    C  u0 {1,S} {5,T}
5    C  u0 {4,T}
""",
    kinetics = None,
)

entry(
    index = 377,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,S} {6,[S,D,T,B]}
2 *2 Cd  u0 {1,D}
3 *1 C   u1
4    C   u0 {1,S} {5,T}
5    C   u0 {4,T}
6    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 378,
    label = "Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D} {4,[S,D,T,B]} {5,[S,D,T,B]}
2 *2 Cd  u0 {1,D}
3 *1 C   u1
4    R!H ux {1,[S,D,T,B]}
5    R!H ux {1,[S,D,T,B]}
""",
    kinetics = None,
)

entry(
    index = 379,
    label = "Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R",
    group = 
"""
1 *3 Cd  u0 c0 {2,D}
2 *2 Cd  u0 {1,D} {5,S}
3 *1 C   u1 {4,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]}
5    C   u0 {2,S}
""",
    kinetics = None,
)

entry(
    index = 380,
    label = "Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R",
    group = 
"""
1 *3 Cd  u0 c0 r0 {2,D}
2 *2 Cd  u0 r0 {1,D} {5,S}
3 *1 C   u1 r0 {4,[S,D,T,B]} {6,[S,D,T,B]}
4    R!H ux {3,[S,D,T,B]}
5    C   u0 r0 {2,S}
6    R!H ux {3,[S,D,T,B]}
""",
    kinetics = None,
)

tree(
"""
L1: Root
    L2: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R
        L3: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Int-4R!H-3R!H
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_Ext-5R!H-R_Ext-3R!H-R
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_3R!H-inRing
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_1CbCbfCdCddCtNO2dS2d->Cd_N-3R!H-inRing
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-2COCSCbCbfCdCtN-R_N-1CbCbfCdCddCtNO2dS2d->Cd
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_1CbCbfCdCddCtNO2dS2d->Cdd
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_1Cd-inRing
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Ext-3R!H-R_N-1Cd-inRing
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_Sp-6R!H-5R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_1CbCdCt->Cd_N-Sp-6R!H-5R!H
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-5R!H=4R!H_N-1CbCbfCdCddCtNO2dS2d->Cdd_Ext-5R!H-R_N-1CbCdCt->Cd
        L3: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Ext-9R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Ext-3R!H-R_Int-8R!H-2COCSCbCbfCdCtN
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Sp-8R!H=3R!H_Int-8R!H-2COCSCbCbfCdCtN_Ext-8R!H-R_Ext-9R!H-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-3R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_Int-10R!H-4R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_1CbCbfCdCddCtNO2dS2d->Cd
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-8R!H-R_N-1CbCbfCdCddCtNO2dS2d->Cd
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-5R!H-R_Ext-4R!H-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-8R!H-R_Ext-9R!H-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_N-Sp-8R!H=3R!H_Ext-2COCSCbCbfCdCtN-R
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H
                                                        L15: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
                                                        L15: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H
                                                        L15: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H
                                                        L15: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Ext-3R!H-R_N-Sp-11R!H=10R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_Sp-7R!H=6R!H_N-Sp-11R!H=10R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-11R!H=10R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-11R!H=10R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_Sp-11R!H=10R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-10R!H-R_N-Sp-7R!H=6R!H_N-Sp-11R!H=10R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Int-9R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                                    L14: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Ext-3R!H-R_N-Sp-9R!H=8R!H_Int-10R!H-5R!H_N-Sp-10R!H-5R!H_N-Sp-7R!H=6R!H_Ext-3R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_Sp-7R!H=6R!H_N-Sp-9R!H=8R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-9R!H=8R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-9R!H=8R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_Sp-9R!H=8R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Ext-8R!H-R_N-Sp-7R!H=6R!H_N-Sp-9R!H=8R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-5R!H-3R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Ext-3R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Ext-3R!H-R_Int-8R!H-5R!H_N-Sp-8R!H-5R!H_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H
                                                L13: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-3R!H-R_N-Sp-10R!H=9R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-10R!H=9R!H
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-10R!H=9R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_Sp-10R!H=9R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-9R!H-R_N-Sp-10R!H=9R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Int-8R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_Sp-9R!H-5R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                                            L12: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-3R!H-R_N-Sp-8R!H=7R!H_Int-9R!H-5R!H_N-Sp-9R!H-5R!H_Ext-3R!H-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-8R!H=7R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-8R!H=7R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_Sp-8R!H=7R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Ext-7R!H-R_N-Sp-8R!H=7R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-5R!H-3R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-1CbCbfCdCddCtNO2dS2d-inRing_Ext-1CbCbfCdCddCtNO2dS2d-R
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_Sp-9R!H=7R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Ext-3R!H-R_N-Sp-9R!H=7R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_Sp-9R!H=7R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-7R!H-R_N-Sp-9R!H=7R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_Sp-8R!H-6R!H_Ext-3R!H-R
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_3R!H-inRing
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-5R!H-3R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-5R!H-3R!H
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
                                    L10: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
                                        L11: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Ext-6R!H-R_N-Sp-8R!H-6R!H_N-3R!H-inRing_N-Sp-8R!H=6R!H_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-5R!H-3R!H
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_Sp-7R!H-5R!H_Ext-3R!H-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_Ext-3R!H-R_Int-7R!H-5R!H_N-Sp-7R!H-5R!H_Ext-3R!H-R
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_Ext-6R!H-R_Ext-6R!H-R
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_3R!H-inRing
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_6R!H-inRing_N-3R!H-inRing
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_Sp-7R!H=6R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_Int-5R!H-3R!H_Ext-6R!H-R_N-Sp-7R!H=6R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_Sp-6R!H-3R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing_N-Sp-6R!H-3R!H
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_Sp-6R!H-3R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Ext-5R!H-R_N-Sp-6R!H-3R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_Sp-6R!H-3R!H
                                L9: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_Sp-6R!H-5R!H_N-Sp-6R!H-3R!H
                            L8: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing_Int-6R!H-5R!H_N-Sp-6R!H-5R!H
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_4R!H-inRing
                        L7: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-3R!H-R_N-6R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd_N-4R!H-inRing
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_1CbCbfCdCddCtNO2dS2d->Cd
                    L6: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-4R!H-3C_N-1CbCbfCdCddCtNO2dS2d->Cd
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_Sp-5R!H-3C
                L5: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_3R!H->C_Int-5R!H-3C_N-Sp-5R!H-3C
            L4: Root_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_N-3R!H->C
    L2: Root_Ext-3R!H-R_Ext-4R!H-R
        L3: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
                            L8: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
                            L8: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H
                            L8: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H
                            L8: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-6R!H-R_N-Sp-9R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_Sp-7R!H=6R!H_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
                        L7: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_Sp-5R!H=4R!H
                    L6: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-6R!H-R_N-Sp-7R!H=6R!H_N-Sp-5R!H=4R!H
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_Sp-5R!H=4R!H
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R_N-Sp-5R!H=4R!H
        L3: Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_Sp-5R!H#4R!H_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
        L3: Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_1CbCbfCdCddCtNO2dS2d->Cd
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_4R!H-inRing_N-1CbCbfCdCddCtNO2dS2d->Cd
            L4: Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing
                L5: Root_Ext-3R!H-R_Ext-4R!H-R_N-Sp-5R!H#4R!H_N-4R!H-inRing_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
    L2: Root_Ext-1CbCbfCdCddCtNO2dS2d-R
        L3: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
            L4: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R
                L5: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R
                    L6: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H
                        L7: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                    L6: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H
                        L7: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-4R!H-R_N-Sp-8R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                L5: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R_Ext-1CbCbfCdCddCtNO2dS2d-R
            L4: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R
                L5: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H
                    L6: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
                L5: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H
                    L6: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-4R!H-R_N-Sp-7R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
            L4: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-1CbCbfCdCddCtNO2dS2d-R
        L3: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R
            L4: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H
                L5: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
            L4: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H
                L5: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-4R!H-R_N-Sp-5R!H=4R!H_Ext-1CbCbfCdCddCtNO2dS2d-R
        L3: Root_Ext-1CbCbfCdCddCtNO2dS2d-R_Ext-1CbCbfCdCddCtNO2dS2d-R
    L2: Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R
        L3: Root_Ext-3R!H-R_Ext-2COCSCbCbfCdCtN-R_Ext-3R!H-R
"""
)

forbidden(
    label = "bond21",
    group = 
"""
1 *2 R!H u0 {2,[S,D]}
2 *1 R!H u1 {1,[S,D]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "cdd2",
    group = 
"""
1 *2 Cdd u0
""",
    shortDesc = u"""""",
    longDesc = 
u"""

""",
)

forbidden(
    label = "cyclic_1",
    group = 
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]}
3 *1 R!H u1 r1 {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Intra addition to double bond in ring should occur in Intra_R_Add_Endocyclic.
""",
)

forbidden(
    label = "cyclic_2",
    group = 
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]}
3 *4 R!H u0 r1 {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Intra addition to double bond in ring should occur in Intra_R_Add_Endocyclic.
""",
)

forbidden(
    label = "cyclic_3",
    group = 
"""
1 *2 R!H u0 r1 {2,[D,T,B]} {3,[S,D,T,B]}
2 *3 R!H u0 r1 {1,[D,T,B]}
3 *5 R!H u0 r1 {1,[S,D,T,B]}
""",
    shortDesc = u"""""",
    longDesc = 
u"""
Intra addition to double bond in ring should occur in Intra_R_Add_Endocyclic.
""",
)

