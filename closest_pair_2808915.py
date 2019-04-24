import sys
import math


def Closest_Pair(P):
    Px = sorted(P, key=lambda x: x[0])
    Py = sorted(P, key=lambda x: x[1])
    return Closest_Pair_Rec(Px, Py)


def Closest_Pair_Rec(Px, Py):
    if len(Px) <= 3:
        p1, p2 = None, None
        Max = 0xffff
        for i in range(len(Px)):
            for j in range(i + 1, len(Px)):
                if dis(Px[i], Px[j]) < Max:
                    Max = dis(Px[i], Px[j])
                    p1, p2 = Px[i], Px[j]
        return p1, p2
    mid = math.ceil(len(Px) / 2)
    Qx = sorted(Px[:mid], key=lambda x: x[0])
    Qy = sorted(Px[:mid], key=lambda x: x[1])
    Rx = sorted(Px[mid:], key=lambda x: x[0])
    Ry = sorted(Px[mid:], key=lambda x: x[1])
    q0, q1 = Closest_Pair_Rec(Qx, Qy)
    r0, r1 = Closest_Pair_Rec(Rx, Ry)
    flag = min(dis(q0, q1), dis(r0, r1))
    x_max = Qx[len(Qx) - 1][0]

    Sy = sorted([_ for _ in Px if abs(_[0] - x_max) < flag],
                key=lambda x: x[1])
    s1, s2 = None, None
    Max = 0xffff
    for i in range(len(Sy)):
        for j in range(i+1, len(Sy)):
            if dis(Sy[i], Sy[j]) < Max:
                Max = dis(Sy[i], Sy[j])
                s1, s2 = Sy[i], Sy[j]

    if dis(s1, s2) < flag:
        return sorted([s1, s2],key=lambda x:x[0])
    elif dis(q0, q1) < dis(r0, r1):
        return sorted([q0, q1],key=lambda x:x[0])
    else:
        return sorted([r0, r1],key=lambda x:x[0])


def dis(p1, p2):
    if p1 is None or p2 is None:
        return 0xffff
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def read_file(path):
    ret = []
    with open(path, "r") as f:
        for line in f.readlines():
            ret.append([float(_) for _ in line.split()])
    return ret

if __name__ == '__main__':
    if(len(sys.argv) < 2):
        sys.exit()
    ans = Closest_Pair(read_file(sys.argv[1]))
    for point in ans:
        print(point[0],point[1])
