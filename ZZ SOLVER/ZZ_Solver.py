import random

def cycle4(k, a,b,c,d):
    k[a], k[b], k[c], k[d] = k[b], k[c], k[d], k[a]
    return k
def swap_pairs(k, a,b,c,d):
    k[a], k[b], = k[b], k[a]
    k[c], k[d] = k[d], k[c]
    return k
def Y_t(k):
    k = cycle4(k, 1,2,3,4)
    return k
def Yi_t(k):
    k = cycle4(k, 1,4,3,2)
    return k
def Y2_t(k):
    k = swap_pairs(k, 1,3,2,4)
    return k
def Zi_t(k):
    k = cycle4(k, 0,3,5,1)
    return k
def Z2_t(k):
    k = swap_pairs(k, 0,5,1,3)
    return k

def translate_moves(moves):
    rbot = ['Y','Yi','Y2','Zi','Z2']
    notations = ['U','L','F','R','B','D']
    forditott = []
    orientation = ['U','L','F','R','B','D']
    turn = ""
    for move in moves:
        ind = orientation.index(move[0])
        if len(move) == 1:
            turn = "D"
        elif move[1] == "i":
            turn = "Di"
        else:
            turn = "D2"
        if ind == 0:
            forditott.extend(['Z2',turn])
            orientation = Z2_t(orientation)
        elif ind == 1:
            forditott.extend(['Zi',turn])
            orientation = Zi_t(orientation)
        elif ind == 2:
           forditott.extend(['Y','Zi',turn])
           orientation = Y_t(orientation)
           orientation = Zi_t(orientation)
        elif ind == 3:
            forditott.extend(['Y2','Zi',turn])
            orientation = Y2_t(orientation)
            orientation = Zi_t(orientation)
        elif ind == 4:
            forditott.extend(['Yi','Zi',turn])
            orientation = Yi_t(orientation)
            orientation = Zi_t(orientation)
        elif ind == 5:
            forditott.extend([turn])
    return forditott

def swap_center_one(orientation, a, b, c, d):
    orientation[a], orientation[b], orientation[c], orientation[d] = orientation[b], orientation[c], orientation[d], \
    orientation[a]
    return orientation

def swap_center_two(orientation, a, b, c, d):
    orientation[a], orientation[b], orientation[c], orientation[d] = orientation[b], orientation[a], orientation[d], \
    orientation[c]
    return orientation

def center_y(orientation):
    orientation = swap_center_one(orientation, 1, 2, 3, 4)
    return orientation

def center_yi(orientation):
    orientation = swap_center_one(orientation, 1, 4, 3, 2)
    return orientation

def center_y2(orientation):
    orientation = swap_center_two(orientation, 1, 3, 2, 4)
    return orientation

def center_x(orientation):
    orientation = swap_center_one(orientation, 0, 2, 5, 4)
    return orientation

def center_xi(orientation):
    orientation = swap_center_one(orientation, 0, 4, 5, 2)
    return orientation

def center_x2(orientation):
    orientation = swap_center_two(orientation, 0, 5, 4, 2)
    return orientation

def center_zi(orientation):
    orientation = swap_center_one(orientation, 0, 3, 5, 1)
    return orientation

def center_z(orientation):
    orientation = swap_center_one(orientation, 0, 1, 5, 3)
    return orientation

def first_translate(something):
    notations = {'U': ['U', 'Ui', 'U2'],
                     'L': ['L', 'Li', 'L2'],
                     'F': ['F', 'Fi', 'F2'],
                     'R': ['R', 'Ri', 'R2'],
                     'B': ['B', 'Bi', 'B2'],
                     'D': ['D', 'Di', 'D2']}
    standard = ['U', 'L', 'F', 'R', 'B', 'D']
    orientation = ['U', 'L', 'F', 'R', 'B', 'D']
    rotations = ["X", "Xi", "X2", "Y", "Yi", "Y2", "Z", "Zi"]
    neg_rotations = ["Xi", "X", "X2", "Yi", "Y", "Y2", "Zi", "Z"]
    functions = [center_x, center_xi, center_x2, center_y, center_yi, center_y2,
                     center_z, center_zi]
    translated = []
    elso = something[0]
    masodik = something[1]
    if masodik in neg_rotations:
        orientation = functions[neg_rotations.index(masodik)](orientation)
        something.pop(1)
    if elso in neg_rotations:
        orientation = functions[neg_rotations.index(elso)](orientation)
        something.pop(0)
    for move in something:
        first_letter = move[0]
        oIndex = orientation.index(first_letter)
        item = standard[oIndex]
        if len(move) == 1:
            translated.append(notations.get(item)[0])
        elif move[1] == "i":
            translated.append(notations.get(item)[1])
        else:
            translated.append(notations.get(item)[2])
    return translated



def gen_scramble():
    moves = ["U", "D", "F", "B", "R", "L"]
    dir = ["", "i", "2"]
    slen = random.randint(17,21)
    s = valid([[random.choice(moves), random.choice(dir)] for x in range(slen)])

    shuff = []
    shuff.extend(list(str(s[x][0]) + str(s[x][1]) + "" for x in range(len(s))))

    return shuff

def valid(ar):
    moves = ["U", "D", "F", "B", "R", "L"]
    for x in range(1, len(ar)):
        while ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    for x in range(2, len(ar)):
        while ar[x][0] == ar[x-2][0] or ar[x][0] == ar[x-1][0]:
            ar[x][0] = random.choice(moves)
    return ar

def replace(moves):
    vect = 0
    for i in moves:
        if len(i) == 1:
            vect += 1
        else:
            if i[1] == 'i':
                vect -= 1
            elif i[1] == '2':
                vect += 2
    char = moves[0][0]
    while vect > 4:
        vect -= 4
    while vect < -4:
        vect += 4
    if vect == 0:
        return -1
    if vect == 4 or vect == -4:
        return -1
    elif vect == 2 or vect == -2:
        char += '2'
    elif vect == 1 or vect == -3:
        pass
    elif vect == 3 or vect == -1:
        char += 'i'
    return char

def remrep(moves):
    stack = []

    for m in moves:
        face = m[0]
        if len(m) == 1:
            cnt = 1
        elif m[1] == '2':
            cnt = 2
        else:
            cnt = 3

        if not stack or stack[-1][0] != face:
            stack.append((face, cnt))
        else:
            prev_face, prev_cnt = stack.pop()
            new_cnt = (prev_cnt + cnt) % 4
            if new_cnt:
                stack.append((face, new_cnt))

    result = []
    for face, cnt in stack:
        c = cnt % 4
        if c == 1:
            result.append(face)
        elif c == 2:
            result.append(face + '2')
        elif c == 3:
            result.append(face + 'i')

    return result

wFace = [1,1,1,1,1,1,1,1,1]
oFace = [2,2,2,2,2,2,2,2,2]
gFace = [3,3,3,3,3,3,3,3,3]
rFace = [4,4,4,4,4,4,4,4,4]
bFace = [5,5,5,5,5,5,5,5,5]
yFace = [6,6,6,6,6,6,6,6,6]


lil_cube = wFace + oFace + gFace + rFace + bFace + yFace


class Cube:
    def __init__(self, cube):
        self.cube = cube.copy()
        self.scrambl = None
        self.scrambledCube = cube.copy()
        self.boolPrint = False
    def nothing(self):
        return []

    def corrigation(self):
        self.Y()
        self.Zi()
        self.Zi()
        self.scrambledCube = self.cube.copy()
        return
    def rose(self, name, idk):
        alma = 9
        ctr = 0
        print(name)
        for i in idk:
            print(i,"",end="")
            ctr += 1
            if ctr == alma:
                ctr = 0
                print()
        print()

    def edge_finder_edges(self, edge, edges):
        edges_pos = [[1,37],[3,28],[5,19],[7,10],[25,12],[21,34],[43,30],[39,16],[46,23],[48,32],[50,41],[52,14]]
        edge1 = [edge[1],edge[0]]
        for position, item in enumerate(edges):
            if edge == item:
                return edges_pos[position]
            elif edge1 == item:
                return [edges_pos[position][1],edges_pos[position][0]]

    def corner_finder_corners(self, corner, corners):
        corners_pos = [[0, 9, 38],[2, 36, 29],[4, 27, 20],[6, 18, 11],[45, 13, 24],[47, 22, 33],[49, 31, 42],[51, 40, 15]]
        corner1 = [corner[2],corner[0],corner[1]]
        corner2 = [corner[1],corner[2],corner[0]]
        for position, item in enumerate(corners):
            if corner == item:
                return corners_pos[position]
            elif corner1 == item:
                return [corners_pos[position][1],corners_pos[position][2],corners_pos[position][0]]
            elif corner2 == item:
                return [corners_pos[position][2],corners_pos[position][0],corners_pos[position][1]]
    def decoy(self, patternCube):
        scrambledEdges = self.get_edges()
        scrambledCorners = self.get_corners()
        self.set_cube(patternCube)
        patternEdges = self.get_edges()
        patternCorners = self.get_corners()
        self.set_cube([1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3,3,4,4,4,4,4,4,4,4,4,5,5,5,5,5,5,5,5,5,6,6,6,6,6,6,6,6,6])
        solvedEdges = self.get_edges()
        solvedCorners = self.get_corners()
        decoyed = self.scrambledCube.copy()
        for idx, patternEdge in enumerate(patternEdges):
            pos = self.edge_finder_edges(patternEdge, scrambledEdges)
            decoyed[pos[0]] = solvedEdges[idx][0]
            decoyed[pos[1]] = solvedEdges[idx][1]
        for idx, patternCorner in enumerate(patternCorners):
            pos = self.corner_finder_corners(patternCorner, scrambledCorners)
            decoyed[pos[0]] = solvedCorners[idx][0]
            decoyed[pos[1]] = solvedCorners[idx][1]
            decoyed[pos[2]] = solvedCorners[idx][2]
        return decoyed.copy()


    def solve_pattern_with_ZZ_fmc(self):
        patternCube = []
        txtcases = [r'PATTERN\case1.txt',r'PATTERN\case2.txt',r'PATTERN\case3.txt']
        choice = random.choice(txtcases)
        print(choice)
        with open(choice, "r") as pt:
            for line in pt:
                line = line.strip()
                for i in line:
                    patternCube.append(int(i))
        self.scrambledCube = self.decoy(patternCube)
        self.set_cube(self.scrambledCube.copy())
        fewestMove = [x for x in range(60)]
        moves = []
        orientations = [self.nothing,self.X,self.Xi,self.Z,self.Zi,self.X2]
        edgeorieantation = [self.nothing,self.Y,self.Y2,self.Yi]
        firstblock = [self.solve_fblock_fl,self.solve_fblock_bl,self.solve_fblock_fr,self.solve_fblock_br]
        finishfb = [self.solve_advf2l_fl,self.solve_advf2l_bl,self.solve_advf2l_fr,self.solve_advf2l_br]
        secondblock = [self.solve_sblock_fl,self.solve_sblock_bl,self.solve_sblock_fr,self.solve_sblock_br]
        finishsb = [self.solve_basf2l_fl,self.solve_basf2l_bl,self.solve_basf2l_fr,self.solve_basf2l_br]
        with open(r'SOT\case.txt', "r") as fl:
            for line in fl:
                seq = line.strip().split(" ")
                seq = [int(x) - 1  for x in seq]
                moves.extend(orientations[seq[0]]())
                moves.extend(edgeorieantation[seq[1]]())
                moves.extend(self.edge_orientation())
                moves.extend(self.solve_line())
                moves.extend(firstblock[seq[2]]())
                moves.extend(finishfb[seq[3]]())
                moves.extend(secondblock[seq[4]]())
                moves.extend(finishsb[seq[5]]())
                moves.extend(self.solve_zbll())
                moves.extend(self.solve_auf())
                moves = first_translate(moves.copy())
                moves = remrep(moves)
                moves = remrep(moves)
                moves = remrep(moves)
                if len(moves) <= len(fewestMove):
                    fewestMove = moves.copy()
                moves.clear()
                self.set_cube(self.scrambledCube.copy())
        self.scramble(fewestMove)
        if self.is_solved():
            print("Succes!")
        else:
            print("Fail!")
        print("Solution lenght:",len(fewestMove))
        print("<------------->")
        return fewestMove



    def solve_with_ZZ_fmc(self):
        fewestMove = [x for x in range(60)]
        moves = []
        orientations = [self.nothing,self.X,self.Xi,self.Z,self.Zi,self.X2]
        edgeorieantation = [self.nothing,self.Y,self.Y2,self.Yi]
        firstblock = [self.solve_fblock_fl,self.solve_fblock_bl,self.solve_fblock_fr,self.solve_fblock_br]
        finishfb = [self.solve_advf2l_fl,self.solve_advf2l_bl,self.solve_advf2l_fr,self.solve_advf2l_br]
        secondblock = [self.solve_sblock_fl,self.solve_sblock_bl,self.solve_sblock_fr,self.solve_sblock_br]
        finishsb = [self.solve_basf2l_fl,self.solve_basf2l_bl,self.solve_basf2l_fr,self.solve_basf2l_br]
        with open(r'SOT\case.txt', "r") as fl:
            for line in fl:
                seq = line.strip().split(" ")
                seq = [int(x) - 1  for x in seq]
                moves.extend(orientations[seq[0]]())
                moves.extend(edgeorieantation[seq[1]]())
                moves.extend(self.edge_orientation())
                moves.extend(self.solve_line())
                moves.extend(firstblock[seq[2]]())
                moves.extend(finishfb[seq[3]]())
                moves.extend(secondblock[seq[4]]())
                moves.extend(finishsb[seq[5]]())
                moves.extend(self.solve_zbll())
                moves.extend(self.solve_auf())
                moves = first_translate(moves.copy())
                moves = remrep(moves)
                if len(moves) <= len(fewestMove):
                    fewestMove = moves.copy()
                moves.clear()
                self.set_cube(self.scrambledCube.copy())
        print("Scramble:", self.scrambl)
        print("Solution:",fewestMove)
        self.scramble(fewestMove)
        if self.is_solved():
            print("Succes!")
        else:
            print("Fail!")
        print("Solution lenght:",len(fewestMove))
        print("<------------->")
        return fewestMove

    def solve_once_with_ZZ(self):
        everyMove = []
        edgeOrientationMoves = self.edge_orientation()
        everyMove.extend(edgeOrientationMoves)
        lineMoves = self.solve_line()
        everyMove.extend(lineMoves)
        firstBlockMoves = self.solve_fblock_bl()
        everyMove.extend(firstBlockMoves)
        advF2lMoves = self.solve_advf2l_fl()
        everyMove.extend(advF2lMoves)
        secondBlockMoves = self.solve_sblock_br()
        everyMove.extend(secondBlockMoves)
        basF2lMoves = self.solve_basf2l_fr()
        everyMove.extend(basF2lMoves)
        zbllMoves = self.solve_zbll()
        everyMove.extend(zbllMoves)
        aufMoves = self.solve_auf()
        everyMove.extend(aufMoves)
        everyMove = remrep(everyMove)
        everyMove = remrep(everyMove)
        everyMove = translate_moves(everyMove)
        return everyMove

    def solve_auf(self):
        result = []
        if not (self.is_solved()):
            self.U()
            result = ['U']
            if not (self.is_solved()):
                self.U()
                result = ['U2']
                if not (self.is_solved()):
                    self.U()
                    result = ['Ui']
        return result

    def get_ll(self):
        return [self.cube[0],self.cube[9],self.cube[38],self.cube[2],self.cube[36],self.cube[29],self.cube[4],self.cube[27],self.cube[20],self.cube[37],self.cube[28],self.cube[19]]
    
    def is_solved(self):
        cubecpy = self.get_cube()
        a = cubecpy[0:9]
        b = cubecpy[9:18]
        c = cubecpy[18:27]
        d = cubecpy[27:36]
        e = cubecpy[36:45]
        f = cubecpy[45:54]
        result = a.count(a[0]) == len(a)
        if (result):
            result = b.count(b[0]) == len(b)
            if (result):
                result = c.count(c[0]) == len(c)
                if (result):
                    result = d.count(d[0]) == len(d)
                    if (result):
                        result = e.count(e[0]) == len(e)
                        if (result):
                            result = f.count(f[0]) == len(f)
                            if (result):
                                return True
        return False
    def is_ll_solved(self):
        cubecpy = self.cube.copy()
        top = cubecpy[0:9]
        left = cubecpy[9:12]
        front = cubecpy[18:21]
        right = cubecpy[27:30]
        back = cubecpy[36:39]
        result = top.count(top[0]) == len(top)
        if (result):
            result = left.count(left[0]) == len(left)
            if (result):
                result = front.count(front[0]) == len(front)
                if (result):
                    result = right.count(right[0]) == len(right)
                    if (result):
                        result = back.count(back[0]) == len(back)
                        if (result):
                            return True
        return False
    def solve_zbll(self):
        if self.is_ll_solved():
            return []
        keyStickerUp = self.get_cube()[8]
        pathCase, pathMove = None, None
        notsolved = self.get_cube()
        while pathCase == None:
            c = self.get_cube()
            AS  = [c[0],c[36],c[27],c[18]]
            H   = [c[9],c[11],c[27],c[29]]
            L   = [c[2],c[6],c[27],c[38]]
            Pi  = [c[9],c[11],c[20],c[36]]
            S   = [c[6],c[20],c[29],c[38]]
            T   = [c[9],c[29],c[6],c[4]]
            U   = [c[36],c[38],c[6],c[4]]
            PLL = [c[0],c[2],c[4],c[6]]
            zbll1 = AS.count(AS[0]) == len(AS)
            zbll2 = H.count(H[0]) == len(H)
            zbll3 = L.count(L[0]) == len(L)
            zbll4 = Pi.count(Pi[0]) == len(Pi)
            zbll5 = S.count(S[0]) == len(S)
            zbll6 = T.count(T[0]) == len(T)
            zbll7 = U.count(U[0]) == len(U)
            zbll8 = PLL.count(PLL[0]) == len(PLL)
            if (zbll1):
                pathCase, pathMove = r'ZBLL\AS\case.txt', r'ZBLL\AS\move.txt'
            elif (zbll2):
                pathCase, pathMove = r'ZBLL\H\case.txt', r'ZBLL\H\move.txt'
            elif (zbll3):
                pathCase, pathMove = r'ZBLL\L\case.txt', r'ZBLL\L\move.txt'
            elif (zbll4):
                pathCase, pathMove = r'ZBLL\Pi\case.txt', r'ZBLL\Pi\move.txt'
            elif (zbll5):
                pathCase, pathMove = r'ZBLL\S\case.txt', r'ZBLL\S\move.txt'
            elif (zbll6):
                pathCase, pathMove = r'ZBLL\T\case.txt', r'ZBLL\T\move.txt'
            elif (zbll7):
                pathCase, pathMove = r'ZBLL\U\case.txt', r'ZBLL\U\move.txt'
            elif (zbll8):

                pathCase, pathMove = r'ZBLL\PLL\case.txt', r'ZBLL\PLL\move.txt'
            self.U()
        while self.get_cube() != notsolved:
            self.U()
        lastLayer = self.get_ll()
        target = lastLayer.pop(9)
        opp = [[1,6],[2,4],[3,5]]
        ll = []
        for i in lastLayer:
            if target == i:
                ll.append(3)
            elif i == self.cube[8]:
                ll.append(4)
            elif target in opp[0] and i in opp[0] or target in opp[1] and i in opp[1] or target in opp[2] and i in opp[2]:
                ll.append(2)
            else:
                ll.append(1)
        
        ll = [str(x) for x in ll]
        ll = ' '.join(ll)
        result = self.get_solution(pathCase, pathMove, ll)
        return result

    def solve_sblock_fl(self):
        edgeDL, edgeFL, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerDown:
                    edgeDL = idx
                elif i[0] == keyStickerFront:
                    edgeFL = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDL, edgeFL]
        if case == [45,11,4]:
            return []
        pathCase, pathMove = r'F2L\SBBFL\case.txt', r'F2L\SBBFL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_sblock_fr(self):
        edgeFR, edgeDR, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edgeDR, edgeFR, corner = None, None, None
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerDown:
                    edgeDR = idx
                elif i[0] == keyStickerFront:
                    edgeFR = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDR, edgeFR]
        if case == [47,9,5]:
            return []
        pathCase, pathMove = r'F2L\SBBFR\case.txt', r'F2L\SBBFR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_sblock_bl(self):
        edgeDL, edgeBL, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerDown:
                    edgeDL = idx
                elif i[0] == keyStickerBack:
                    edgeBL = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDL, edgeBL]
        if case == [51,11,7]:
            return []
        pathCase, pathMove = r'F2L\SBBBL\case.txt', r'F2L\SBBBL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_sblock_br(self):
        edgeDR, edgeBR, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerDown:
                    edgeDR = idx
                elif i[0] == keyStickerBack:
                    edgeBR = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDR, edgeBR]
        if case == [49,9,6]:
            return []
        pathCase, pathMove = r'F2L\SBBBR\case.txt', r'F2L\SBBBR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_advf2l_fl(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerFront:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [45, 4]:
            return []
        pathCase, pathMove = r'F2L\ADVFL\case.txt', r'F2L\ADVFL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_advf2l_fr(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerFront:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [47, 5]:
            return []
        pathCase, pathMove = r'F2L\ADVFR\case.txt', r'F2L\ADVFR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_advf2l_br(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerBack:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [49, 6]:
            return []
        pathCase, pathMove = r'F2L\ADVBR\case.txt', r'F2L\ADVBR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_advf2l_bl(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerBack:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [51, 7]:
            return []
        pathCase, pathMove = r'F2L\ADVBL\case.txt', r'F2L\ADVBL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_basf2l_fl(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerFront:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [45, 4]:
            return []
        pathCase, pathMove = r'F2L\F2LFL\case.txt', r'F2L\F2LFL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_basf2l_fr(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerFront:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [47, 5]:
            return []
        pathCase, pathMove = r'F2L\F2LFR\case.txt', r'F2L\F2LFR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_basf2l_br(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerBack:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [49, 6]:
            return []
        pathCase, pathMove = r'F2L\F2LBR\case.txt', r'F2L\F2LBR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_basf2l_bl(self):
        edge, corner = None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerBack:
                    edge = idx
        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]
        case = [corner, edge]
        if case == [51, 7]:
            return []
        pathCase, pathMove = r'F2L\F2LBL\case.txt', r'F2L\F2LBL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_fblock_fl(self):
        edgeDL, edgeFL, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edgeDL, edgeFL, corner = None, None, None
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerDown:
                    edgeDL = idx
                elif i[0] == keyStickerFront:
                    edgeFL = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDL, edgeFL]
        if case == [45,11,4]:
            return []
        pathCase, pathMove = r'F2L\BBFL\case.txt', r'F2L\BBFL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_fblock_fr(self):
        edgeDR, edgeFR, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerDown:
                    edgeDR = idx
                elif i[0] == keyStickerFront:
                    edgeFR = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerFront or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerFront or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerFront or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDR, edgeFR]
        if case == [47,9,5]:
            return []
        pathCase, pathMove = r'F2L\BBFR\case.txt', r'F2L\BBFR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_fblock_bl(self):
        edgeDL, edgeBL, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerLeft:
                if i[0] == keyStickerDown:
                    edgeDL = idx
                elif i[0] == keyStickerBack:
                    edgeBL = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerLeft or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerLeft or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerLeft or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDL, edgeBL]
        if case == [51,11,7]:
            return []
        pathCase, pathMove = r'F2L\BBBL\case.txt', r'F2L\BBBL\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def solve_fblock_br(self):
        edgeDR, edgeBR, corner = None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[1] == keyStickerRight:
                if i[0] == keyStickerDown:
                    edgeDR = idx
                elif i[0] == keyStickerBack:
                    edgeBR = idx

        cubecorner = [[0,9,38],[2,36,29],[4,27,20],[6,18,11],[45,13,24],[47,22,33],[49,31,42],[51,40,15]]
        corners = self.get_corners()
        for idx, i in enumerate(corners):
            if i[0] == keyStickerRight or i[0] == keyStickerBack or i[0] == keyStickerDown:
                if i[1] == keyStickerRight or i[1] == keyStickerBack or i[1] == keyStickerDown:
                    if i[2] == keyStickerRight or i[2] == keyStickerBack or i[2] == keyStickerDown:
                        if i[0] == keyStickerDown:
                            corner = cubecorner[idx][0]
                        elif i[1] == keyStickerDown:
                            corner = cubecorner[idx][1]
                        else:
                            corner = cubecorner[idx][2]

        case = [corner, edgeDR, edgeBR]
        if case == [49,9,6]:
            return []
        pathCase, pathMove = r'F2L\BBBR\case.txt', r'F2L\BBBR\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def get_solution(self, pathCase, pathMove, case):
        caseLnCtr, moveLnCtr = 1, 1
        moves = []
        with open(pathCase, "r") as fl:
            for line in fl:
                if case == line.rstrip('\n'):
                    break
                caseLnCtr += 1
        with open(pathMove, "r") as fl:
            for line in fl:
                if moveLnCtr == caseLnCtr:
                    solution = line.strip().split(" ")
                    notations = ["U","Ui","U2","L","Li","L2","F","Fi","F2","R","Ri","R2","B","Bi","B2","D","Di","D2"]
                    functions = [self.U,self.Ui,self.U2,self.L,self.Li,self.L2,self.F,self.Fi,self.F2,self.R,self.Ri,self.R2,self.B,self.Bi,self.B2,self.D,self.Di,self.D2]
                    for i in solution:
                        functions[notations.index(i)]()
                    moves.extend(solution)
                    break
                moveLnCtr += 1
        self.counter = caseLnCtr
        return moves

    def solve_line(self):
        pathCase, pathMove = None, None
        edgeFD, edgeBD = None, None
        moves = []
        caseLnCtr, moveLnCtr = 1, 1
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[0] == keyStickerDown:
                if i[1] == keyStickerFront:
                    edgeFD = idx
                elif i[1] == keyStickerBack:
                    edgeBD = idx
        case = [edgeFD, edgeBD]
        if case == [8,10]:
            return []
        pathCase, pathMove = r'LINE\case.txt', r'LINE\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        with open(pathCase, "r") as fl:
            for line in fl:
                if case == line.rstrip('\n'):
                    break
                caseLnCtr += 1
        with open(pathMove, "r") as fl:
            for line in fl:
                if moveLnCtr == caseLnCtr:
                    solution = line.strip().split(" ")
                    notations = ["U","Ui","U2","L","Li","L2","F2","R","Ri","R2","B2","D","Di","D2"]
                    functions = [self.U,self.Ui,self.U2,self.L,self.Li,self.L2,self.F2,self.R,self.Ri,self.R2,self.B2,self.D,self.Di,self.D2]
                    for i in solution:
                        functions[notations.index(i)]()
                    moves.extend(solution)
                    break
                moveLnCtr += 1
        return moves

    def solve_cross(self):
        edgeFD, edgeRD, edgeBD, edgeLD = None, None, None, None
        keyStickerDown = self.get_cube()[53]
        keyStickerFront = self.get_cube()[26]
        keyStickerBack = self.get_cube()[44]
        keyStickerLeft = self.get_cube()[17]
        keyStickerRight = self.get_cube()[35]
        edges = self.get_edges()
        for idx, i in enumerate(edges):
            if i[0] == keyStickerDown:
                if i[1] == keyStickerFront:
                    edgeFD = idx
                elif i[1] == keyStickerRight:
                    edgeRD = idx
                elif i[1] == keyStickerBack:
                    edgeBD = idx
                elif i[1] == keyStickerLeft:
                    edgeLD = idx
        case = [edgeFD, edgeRD, edgeBD, edgeLD]
        if case == [8,9,10,11]:
            return []
        if case[0] == 0:
            pathCase, pathMove = r'CROSS\0\case.txt', r'CROSS\0\move.txt'
        elif case[0] == 1:
            pathCase, pathMove = r'CROSS\1\case.txt', r'CROSS\1\move.txt'
        elif case[0] == 2:
            pathCase, pathMove = r'CROSS\2\case.txt', r'CROSS\2\move.txt'
        elif case[0] == 3:
            pathCase, pathMove = r'CROSS\3\case.txt', r'CROSS\3\move.txt'
        elif case[0] == 4:
            pathCase, pathMove = r'CROSS\4\case.txt', r'CROSS\4\move.txt'
        elif case[0] == 5:
            pathCase, pathMove = r'CROSS\5\case.txt', r'CROSS\5\move.txt'
        elif case[0] == 6:
            pathCase, pathMove = r'CROSS\6\case.txt', r'CROSS\6\move.txt'
        elif case[0] == 7:
            pathCase, pathMove = r'CROSS\7\case.txt', r'CROSS\7\move.txt'
        elif case[0] == 8:
            pathCase, pathMove = r'CROSS\8\case.txt', r'CROSS\8\move.txt'
        elif case[0] == 9:
            pathCase, pathMove = r'CROSS\9\case.txt', r'CROSS\9\move.txt'
        elif case[0] == 10:
            pathCase, pathMove = r'CROSS\10\case.txt', r'CROSS\10\move.txt'
        else:
            pathCase, pathMove = r'CROSS\11\case.txt', r'CROSS\11\move.txt'
        case = [str(x) for x in case]
        case = ' '.join(case)
        result = self.get_solution(pathCase, pathMove, case)
        return result

    def edge_orientation(self):
        pathCase, pathMove = None, None
        moves = []
        caseLnCtr, moveLnCtr = 1, 1
        bdeCtr = self.count_bad_edges()
        bdeIndexes = self.get_bad_edges()
        if bdeCtr == 0:
            return moves
        elif bdeCtr == 2:
            pathCase, pathMove = r'EO\2\case.txt', r'EO\2\move.txt'
        elif bdeCtr == 4:
            pathCase, pathMove = r'EO\4\case.txt', r'EO\4\move.txt'
        elif bdeCtr == 6:
            pathCase, pathMove = r'EO\6\case.txt', r'EO\6\move.txt'
        elif bdeCtr == 8:
            pathCase, pathMove = r'EO\8\case.txt', r'EO\8\move.txt'
        elif bdeCtr == 10:
            pathCase, pathMove = r'EO\10\case.txt', r'EO\10\move.txt'
        else:
            pathCase, pathMove = r'EO\12\case.txt', r'EO\12\move.txt'
        bdeIndexes = [str(x) for x in bdeIndexes]
        bdeIndexes = ' '.join(bdeIndexes)
        result = self.get_solution(pathCase, pathMove, bdeIndexes)
        return result

    def set_cube(self, cube):
        self.cube = cube.copy()
    def get_cube(self):
        return self.cube.copy()

    def get_edges(self):
        edges = [[self.cube[1], self.cube[37]],
                 [self.cube[3], self.cube[28]],
                 [self.cube[5], self.cube[19]],
                 [self.cube[7], self.cube[10]],
                 [self.cube[25], self.cube[12]],
                 [self.cube[21], self.cube[34]],
                 [self.cube[43], self.cube[30]],
                 [self.cube[39], self.cube[16]],
                 [self.cube[46], self.cube[23]],
                 [self.cube[48], self.cube[32]],
                 [self.cube[50], self.cube[41]],
                 [self.cube[52], self.cube[14]]]
        return edges
    def count_bad_edges(self):
        keyStickerUp = self.cube[8]
        keyStickerDown = self.cube[53]
        keyStickerFront = self.cube[26]
        keyStickerBack = self.cube[44]
        keyStickerLeft = self.cube[17]
        keyStickerRight = self.cube[35]
        edgesToCheck = self.get_edges()
        badEdgeCounter = 0
        for i in edgesToCheck:
            if i[0] == keyStickerLeft or i[0] == keyStickerRight:
                badEdgeCounter += 1
            elif i[1] == keyStickerUp or i[1] == keyStickerDown:
                badEdgeCounter += 1
        return badEdgeCounter
    def get_bad_edges(self):
        keyStickerUp = self.cube[8]
        keyStickerDown = self.cube[53]
        keyStickerFront = self.cube[26]
        keyStickerBack = self.cube[44]
        keyStickerLeft = self.cube[17]
        keyStickerRight = self.cube[35]
        edgesToCheck = self.get_edges()
        badEdgeIndexes = []
        for i in edgesToCheck:
            if i[0] == keyStickerLeft or i[0] == keyStickerRight:
                badEdgeIndexes.append(edgesToCheck.index(i))
            elif i[1] == keyStickerUp or i[1] == keyStickerDown:
                badEdgeIndexes.append(edgesToCheck.index(i))
        badEdgeIndexes.sort()
        return badEdgeIndexes

    def is_solvable(self):
        self.edge_orientation()
        self.solve_line()
        self.solve_fblock_bl()
        self.solve_advf2l_fl()
        self.solve_sblock_br()
        self.solve_basf2l_fr()
        self.solve_zbll()
        self.solve_auf()
        if not (self.is_solved()):
            self.set_cube(self.scrambledCube) 
            return False
        self.set_cube(self.scrambledCube) 
        return True

    def scramble(self, s):
        self.scrambl = s
        notations = ["U","Ui","U2","L","Li","L2","F","Fi","F2","R","Ri","R2","B","Bi","B2","D","Di","D2"]
        functions = [self.U,self.Ui,self.U2,self.L,self.Li,self.L2,self.F,self.Fi,self.F2,self.R,self.Ri,self.R2,self.B,self.Bi,self.B2,self.D,self.Di,self.D2]            
        for i in s:
            functions[notations.index(i)]()
        self.scrambledCube = self.cube.copy()
        return

    def corner_twist(self, corner):
        corner[0], corner[1], corner[2] = corner[2], corner[0], corner[1]
        return corner
    def get_corners(self):
        corners = [[self.cube[0], self.cube[9], self.cube[38]],
                   [self.cube[2], self.cube[36], self.cube[29]],
                   [self.cube[4], self.cube[27], self.cube[20]],
                   [self.cube[6], self.cube[18], self.cube[11]],
                   [self.cube[45], self.cube[13], self.cube[24]],
                   [self.cube[47], self.cube[22], self.cube[33]],
                   [self.cube[49], self.cube[31], self.cube[42]],
                   [self.cube[51], self.cube[40], self.cube[15]]]
        return corners
    def count_corner_twists(self):
        keyStickerUp = self.cube[8]
        keyStickerDown = self.cube[53]
        corners = self.get_corners()
        cornerTwistCounter = 0
        for corner in corners:
            while corner[0] != keyStickerUp or corner[0] != keyStickerDown:
                if corner[0] == keyStickerUp or corner[0] == keyStickerDown:
                    break
                self.corner_twist(corner)
                cornerTwistCounter += 1
        return cornerTwistCounter

    def print(self):
        c = ''
        for i in self.cube:
            c += str(i)
        print("    " + c[0:3] + "\n" + "    " + c[7:9] + c[3] + "\n" + "    " + c[6] + c[5] + c[4])
        print(c[9:12] + " " + c[18:21] + " " + c[27:30] + " " + c[36:39])
        print(c[16:18] + c[12] + " " + c[25:27] + c[21] + " " + c[34:36] + c[30] + " " + c[43:45] + c[39])
        print(
            c[15] + c[14] + c[13] + " " + c[24] + c[23] + c[22] + " " + c[33] + c[32] + c[31] + " " + c[42] + c[41] + c[
                40])
        print("    " + c[45:48] + "\n" + "    " + c[52:54] + c[48] + "\n" + "    " + c[51] + c[50] + c[49])

    def swap_one(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.cube[a], self.cube[b], self.cube[c], self.cube[d] = self.cube[b], self.cube[c], self.cube[d], self.cube[a]
        self.cube[e], self.cube[f], self.cube[g], self.cube[h] = self.cube[f], self.cube[g], self.cube[h], self.cube[e]
        self.cube[i], self.cube[j], self.cube[k], self.cube[l] = self.cube[j], self.cube[k], self.cube[l], self.cube[i]
        self.cube[m], self.cube[n], self.cube[o], self.cube[p] = self.cube[n], self.cube[o], self.cube[p], self.cube[m]
        self.cube[q], self.cube[r], self.cube[s], self.cube[t] = self.cube[r], self.cube[s], self.cube[t], self.cube[q]
        return self.cube
    def swap_two(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t):
        self.cube[a], self.cube[b], self.cube[c], self.cube[d] = self.cube[b], self.cube[a], self.cube[d], self.cube[c]
        self.cube[e], self.cube[f], self.cube[g], self.cube[h] = self.cube[f], self.cube[e], self.cube[h], self.cube[g]
        self.cube[i], self.cube[j], self.cube[k], self.cube[l] = self.cube[j], self.cube[i], self.cube[l], self.cube[k]
        self.cube[m], self.cube[n], self.cube[o], self.cube[p] = self.cube[n], self.cube[m], self.cube[p], self.cube[o]
        self.cube[q], self.cube[r], self.cube[s], self.cube[t] = self.cube[r], self.cube[q], self.cube[t], self.cube[s]
        return self.cube
    def swap_face_one(self, a, b, c, d, e, f, g, h):
        self.cube[a], self.cube[b], self.cube[c], self.cube[d] = self.cube[b], self.cube[c], self.cube[d], self.cube[a]
        self.cube[e], self.cube[f], self.cube[g], self.cube[h] = self.cube[f], self.cube[g], self.cube[h], self.cube[e]
        return self.cube
    def swap_face_two(self, a, b, c, d, e, f, g, h):
        self.cube[a], self.cube[b], self.cube[c], self.cube[d] = self.cube[b], self.cube[a], self.cube[d], self.cube[c]
        self.cube[e], self.cube[f], self.cube[g], self.cube[h] = self.cube[f], self.cube[e], self.cube[h], self.cube[g]
        return self.cube


    def second_translate(self, moves):
        pass

    def U(self):
        self.cube = self.swap_one(0, 6, 4, 2, 1, 7, 5, 3, 18, 27, 36, 9, 19, 28, 37, 10, 20, 29, 38, 11)
        return self.cube
    def Ui(self):
        self.cube = self.swap_one(0, 2, 4, 6, 1, 3, 5, 7, 18, 9, 36, 27, 19, 10, 37, 28, 20, 11, 38, 29)
        return self.cube
    def U2(self):
        self.cube = self.swap_two(0, 4, 2, 6, 1, 5, 3, 7, 18, 36, 19, 37, 20, 38, 9, 27, 10, 28, 11, 29)
        return self.cube
    def L(self):
        self.cube = self.swap_one(9, 15, 13, 11, 10, 16, 14, 12, 0, 40, 45, 18, 7, 39, 52, 25, 6, 38, 51, 24)
        return self.cube
    def Li(self):
        self.cube = self.swap_one(9, 11, 13, 15, 10, 12, 14, 16, 0, 18, 45, 40, 7, 25, 52, 39, 6, 24, 51, 38)
        return self.cube
    def L2(self):
        self.cube = self.swap_two(9, 13, 11, 15, 10, 14, 12, 16, 0, 45, 7, 52, 6, 51, 18, 40, 25, 39, 24, 38)
        return self.cube
    def F(self):
        self.cube = self.swap_one(18, 24, 22, 20, 19, 25, 23, 21, 6, 13, 47, 27, 5, 12, 46, 34, 4, 11, 45, 33)
        return self.cube
    def Fi(self):
        self.cube = self.swap_one(18, 20, 22, 24, 19, 21, 23, 25, 6, 27, 47, 13, 5, 34, 46, 12, 4, 33, 45, 11)
        return self.cube
    def F2(self):
        self.cube = self.swap_two(18, 22, 20, 24, 19, 23, 21, 25, 6, 47, 27, 13, 5, 46, 34, 12, 4, 45, 33, 11)
        return self.cube
    def R(self):
        self.cube = self.swap_one(20, 47, 42, 2, 21, 48, 43, 3, 22, 49, 36, 4, 27, 33, 31, 29, 34, 32, 30, 28)
        return self.cube
    def Ri(self):
        self.cube = self.swap_one(20, 2, 42, 47, 21, 3, 43, 48, 22, 4, 36, 49, 27, 29, 31, 33, 34, 28, 30, 32)
        return self.cube
    def R2(self):
        self.cube = self.swap_two(20, 42, 2, 47, 21, 43, 3, 48, 22, 36, 4, 49, 27, 31, 29, 33, 34, 30, 28, 32)
        return self.cube
    def B(self):
        self.cube = self.swap_one(36, 42, 40, 38, 37, 43, 41, 39, 0, 29, 49, 15, 1, 30, 50, 16, 2, 31, 51, 9)
        return self.cube
    def Bi(self):
        self.cube = self.swap_one(36, 38, 40, 42, 37, 39, 41, 43, 0, 15, 49, 29, 1, 16, 50, 30, 2, 9, 51, 31)
        return self.cube
    def B2(self):
        self.cube = self.swap_two(36, 40, 38, 42, 37, 41, 39, 43, 0, 49, 15, 29, 1, 50, 16, 30, 2, 51, 9, 31)
        return self.cube
    def D(self):
        self.cube = self.swap_one(24, 15, 42, 33, 23, 14, 41, 32, 22, 13, 40, 31, 45, 51, 49, 47, 46, 52, 50, 48)
        return self.cube
    def Di(self):
        self.cube = self.swap_one(24, 33, 42, 15, 23, 32, 41, 14, 22, 31, 40, 13, 45, 47, 49, 51, 46, 48, 50, 52)
        return self.cube
    def D2(self):
        self.cube = self.swap_two(24, 42, 33, 15, 23, 41, 32, 14, 22, 40, 31, 13, 45, 49, 47, 51, 46, 50, 48, 52)
        return self.cube

    def get_u_face(self):
        return self.cube[0:9]
    def get_l_face(self):
        return self.cube[9:18]
    def get_f_face(self):
        return self.cube[18:27]
    def get_r_face(self):
        return self.cube[27:36]
    def get_b_face(self):
        return self.cube[36:45]
    def get_d_face(self):
        return self.cube[45:54]

    def X(self):
        up = self.get_f_face()
        front = self.get_d_face()
        down = self.get_b_face()
        back = self.get_u_face()
        self.cube = up + self.get_l_face() + front + self.get_r_face() + back + down
        self.cube = self.swap_face_one(9, 11, 13, 15, 10, 12, 14, 16)  # Li turn only
        self.cube = self.swap_face_one(27, 33, 31, 29, 34, 32, 30, 28)  # R turn only
        self.cube = self.swap_face_two(36, 40, 38, 42, 37, 41, 39, 43)  # B2 turn only
        self.cube = self.swap_face_two(45, 49, 47, 51, 46, 50, 48, 52)  # D2 turn only
        return ['X']
    def Xi(self):
        up = self.get_b_face()
        front = self.get_u_face()
        down = self.get_f_face()
        back = self.get_d_face()
        self.cube = up + self.get_l_face() + front + self.get_r_face() + back + down
        self.cube = self.swap_face_one(9, 15, 13, 11, 10, 16, 14, 12)  # L turn only
        self.cube = self.swap_face_one(27, 29, 31, 33, 34, 28, 30, 32)  # Ri turn only
        self.cube = self.swap_face_two(0, 4, 2, 6, 1, 5, 3, 7)  # U2 turn only
        self.cube = self.swap_face_two(36, 40, 38, 42, 37, 41, 39, 43)  # B2 turn only
        return ['Xi']
    def X2(self):
        up = self.get_d_face()
        front = self.get_b_face()
        down = self.get_u_face()
        back = self.get_f_face()
        self.cube = up + self.get_l_face() + front + self.get_r_face() + back + down
        self.cube = self.swap_face_two(36, 40, 38, 42, 37, 41, 39, 43)  # B2 turn only
        self.cube = self.swap_face_two(27, 31, 29, 33, 34, 30, 28, 32)  # R2 turn only
        self.cube = self.swap_face_two(18, 22, 20, 24, 19, 23, 21, 25)  # F2 turn only
        self.cube = self.swap_face_two(9, 13, 11, 15, 10, 14, 12, 16)  # L2 turn only
        return ['X2']
    def Y(self):
        left = self.get_f_face()
        front = self.get_r_face()
        right = self.get_b_face()
        back = self.get_l_face()
        self.cube = self.get_u_face() + left + front + right + back + self.get_d_face()
        self.cube = self.swap_face_one(0, 6, 4, 2, 1, 7, 5, 3)  # U turn only
        self.cube = self.swap_face_one(45, 47, 49, 51, 46, 48, 50, 52)  # Di turn only
        return ['Y']
    def Yi(self):
        left = self.get_b_face()
        front = self.get_l_face()
        right = self.get_f_face()
        back = self.get_r_face()
        self.cube = self.get_u_face() + left + front + right + back + self.get_d_face()
        self.cube = self.swap_face_one(0, 2, 4, 6, 1, 3, 5, 7)  # Ui turn only
        self.cube = self.swap_face_one(45, 51, 49, 47, 46, 52, 50, 48)  # D turn only
        return ['Yi']
    def Y2(self):
        left = self.get_r_face()
        front = self.get_b_face()
        right = self.get_l_face()
        back = self.get_f_face()
        self.cube = self.get_u_face() + left + front + right + back + self.get_d_face()
        self.cube = self.swap_face_two(0, 4, 2, 6, 1, 5, 3, 7)  # U2 turn only
        self.cube = self.swap_face_two(45, 49, 47, 51, 46, 50, 48, 52)  # D2 turn only
        return ['Y2']

    def Zi(self):
        up = self.get_r_face()
        left = self.get_u_face()
        right = self.get_d_face()
        down = self.get_l_face()
        self.cube = up + left + self.get_f_face() + right + self.get_b_face() + down
        self.cube = self.swap_face_one(18, 20, 22, 24, 19, 21, 23, 25)  # Fi turn only
        self.cube = self.swap_face_one(36, 42, 40, 38, 37, 43, 41, 39)  # B turn only
        self.cube = self.swap_face_one(45, 47, 49, 51, 46, 48, 50, 52)  # Di turn only
        self.cube = self.swap_face_one(9, 11, 13, 15, 10, 12, 14, 16)  # Li turn only
        self.cube = self.swap_face_one(27, 29, 31, 33, 34, 28, 30, 32)  # Ri turn only
        self.cube = self.swap_face_one(0, 2, 4, 6, 1, 3, 5, 7)  # Ui turn only
        return ['Zi']

    def Z(self):
        up = self.get_l_face()
        left = self.get_d_face()
        right = self.get_u_face()
        down = self.get_r_face()
        self.cube = up + left + self.get_f_face() + right + self.get_b_face() + down
        self.cube = self.swap_face_one(18, 24, 22, 20, 19, 25, 23, 21)  # F turn only
        self.cube = self.swap_face_one(36, 38, 40, 42, 37, 39, 41, 43)  # Bi turn only
        self.cube = self.swap_face_one(45, 51, 49, 47, 46, 52, 50, 48)  # D turn only
        self.cube = self.swap_face_one(9, 15, 13, 11, 10, 16, 14, 12)  # L turn only
        self.cube = self.swap_face_one(27, 33, 31, 29, 34, 32, 30, 28)  # R turn only
        self.cube = self.swap_face_one(0, 6, 4, 2, 1, 7, 5, 3)  # U turn only
        return ['Z']


import time
start = time.time()
myCube = Cube(lil_cube)
for i in range(1):
    scramble = gen_scramble()
    myCube.scramble(scramble)
    result = myCube.solve_with_ZZ_fmc()
    print(result)
end = time.time()
print(end - start)





