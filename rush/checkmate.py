def checkmate(board):
    try:
        # แปลงข้อความให้อยู่ในรูปแบบตารางโดยการแบ่ง string ออกเป็นชุดๆตามการขึ้นบรรทัดใหม่ จากนั้นให้เอา string แต่ละชุดเพิ่มเป็น list
        table_board = [list(row.strip()) for row in board.strip().split("\n")]
    except:
        print("Something went wrong while trying to cast string into table")
        return 0
    p_index = set()
    b_index = set()
    r_index = set()
    q_index = set()
    k_index = set()
    occupied_index = set()
    size = len(table_board)

    # หาตำแหน่งเบี้ยต่างๆมาเก็บไว้เป็น set เพื่อใช้เป็นจุด start ของเบี้ยไว้เดินหาเส้นทางในกระดาน
    for j in range(0,len(table_board)):
        for i in range(0,len(table_board[j])):
            if table_board[j][i] == 'P':
                p_index.add((j,i))
            elif table_board[j][i] == 'B':
                b_index.add((j,i))
            elif table_board[j][i] == 'R':
                r_index.add((j,i))
            elif table_board[j][i] == 'Q':
                q_index.add((j,i))
            elif table_board[j][i] == 'K':
                k_index.add((j,i))

        # ตรวจสอบขนาดกระดานว่าเป็นสี่เหลี่ยมจริงๆและมีขนาด 2x2 หรือมากกว่านั้นเสมอ
        if size != len(table_board[j]) and size > 1:
            print(f"Board is not square")
            return 0

    # อัพเดทตำแหน่งที่มีเบี้ยวางอยู่ไว้เปรียบเทียบตอนเดินหา King ว่าเส้นทางถูกขัดขวางหรือเปล่า
    occupied_index.update(p_index, b_index, r_index, q_index)
    # ตรวจสอบตำแหน่งของเบี้ยเพื่อให้แน่ใจว่ากระดานไม่ว่างเปล่าและมี King ตามกติกา
    if not occupied_index:
        print("Board is empty")
        return 0
    if len(k_index) != 1:
        print("No King places in the board or There is more than 1 King place in the board")
        return 0
    
    # คำนวณเส้นทางสำหรับเบี้ยรูปแบบต่างๆ
    if p_index:
        for pawn in p_index:
            j = pawn[0]
            i = pawn[1]
            if (j-1) >= 0 and (i-1) >= 0:
                paths = {(j-1,i-1)}
                intersect = paths.intersection(occupied_index)
                if not intersect and k_index.issubset(paths):
                    print("Success")
                    return 0
            if (j-1) >= 0 and (i+1) <= size - 1:
                paths = {(j-1,i+1)}
                intersect = paths.intersection(occupied_index)
                if not intersect and k_index.issubset(paths):
                    print("Success")
                    return 0
    # จำนวน Bishop ต้องน้อยกว่า 2
    if len(b_index) <= 2:
        for pawn in b_index:
            # วนลูปให้ครบ 4 รอบตามจำนวนเส้นทาง
            for iterate in range(1,5):
                # กำหนดตำแหน่งเริ่มต้นของเบี้ย Bishop
                j = pawn[0]
                i = pawn[1]
                paths = set()
                if iterate == 1: # เดินเฉียงบนซ้าย
                    while (j-1) >= 0 and (i-1) >= 0:
                        # หาเส้นทางสำหรับวิธีเดินแบบที่ 1
                        paths.add((j-1,i-1))
                        j -= 1
                        i -= 1
                        # เช็คว่าเส้นทางซ้ำกับเบี้ยตัวอื่นๆไหม
                        intersect = paths.intersection(occupied_index)
                        # ถ้าเส้นทางเจอกับตำแหน่ง King ก็ให้พิมพ์ success และจบโปรแกรม
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        # ถ้าเส้นทางเจอเบี้ยตัวอื่นก่อนเจอ King ก็ให้ข้ามไปลูปต่อไปเพื่อหาเส้นทางในวิธีเดินแบบต่อไป
                        elif intersect:
                            break
                elif iterate ==2: # เดินเฉียงบนขวา
                    while (j-1) >= 0 and (i+1) <= size:
                        # หาเส้นทางสำหรับวิธีเดินแบบที่ 2
                        paths.add((j-1,i+1))
                        j -= 1
                        i += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate ==3: # เดินเฉียงลงซ้าย
                    while (j+1) <= size and (i-1) >= 0:
                        paths.add((j+1,i-1))
                        j += 1
                        i -= 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate ==4: # เดินเฉียงลงขวา
                    while (j+1) <= size and (i+1) <= size:
                        paths.add((j+1,i+1))
                        j += 1
                        i += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 5:
                    print("testing")
                
    else:
        print("Bishop on board is more than 2 pieces")
        return 0
    
    if len(r_index) <= 2:
        for pawn in r_index:
            # วนลูป 4 รอบ สำหรับ 4 ทิศทาง (ขึ้น, ลง, ซ้าย, ขวา)
            for iterate in range(1, 5):
                # รีเซ็ตตำแหน่งเริ่มต้นของตัว Rook ทุกครั้งที่เปลี่ยนทิศ
                j = pawn[0]
                i = pawn[1]
                paths = set()

                if iterate == 1: # เดินขึ้นข้างบน (ลดค่า j)
                    while (j-1) >= 0:
                        paths.add((j-1, i))
                        j -= 1
                        # ตรวจสอบการชนเหมือน Bishop
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break

                elif iterate == 2: # เดินลงข้างล่าง (เพิ่มค่า j)
                    while (j+1) < size:
                        paths.add((j+1, i))
                        j += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break

                elif iterate == 3: # เดินไปทางซ้าย (ลดค่า i)
                    while (i-1) >= 0:
                        paths.add((j, i-1))
                        i -= 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break

                elif iterate == 4: # เดินไปทางขวา (เพิ่มค่า i)
                    while (i+1) < size:
                        paths.add((j, i+1))
                        i += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break

    else:
        print("Rook on board is more than 2 pieces")
        return 0
    
    if len(q_index) == 1:
        for pawn in q_index:
            # Queen เดินได้ 8 ทิศทาง (1-4 เฉียงเหมือน Bishop, 5-8 ตรงเหมือน Rook)
            for iterate in range(1, 9):
                j = pawn[0]
                i = pawn[1]
                paths = set()

                # --- ส่วนการเดินเฉียง (เหมือน Bishop) ---
                if iterate == 1: # เฉียงบนซ้าย
                    while (j-1) >= 0 and (i-1) >= 0:
                        paths.add((j-1, i-1))
                        j -= 1
                        i -= 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 2: # เฉียงบนขวา
                    while (j-1) >= 0 and (i+1) < size:
                        paths.add((j-1, i+1))
                        j -= 1
                        i += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 3: # เฉียงล่างซ้าย
                    while (j+1) < size and (i-1) >= 0:
                        paths.add((j+1, i-1))
                        j += 1
                        i -= 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 4: # เฉียงล่างขวา
                    while (j+1) < size and (i+1) < size:
                        paths.add((j+1, i+1))
                        j += 1
                        i += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                
                # --- ส่วนการเดินแนวตรง (เหมือน Rook) ---
                elif iterate == 5: # ขึ้นบน
                    while (j-1) >= 0:
                        paths.add((j-1, i))
                        j -= 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 6: # ลงล่าง
                    while (j+1) < size:
                        paths.add((j+1, i))
                        j += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 7: # ซ้าย
                    while (i-1) >= 0:
                        paths.add((j, i-1))
                        i -= 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
                elif iterate == 8: # ขวา
                    while (i+1) < size:
                        paths.add((j, i+1))
                        i += 1
                        intersect = paths.intersection(occupied_index)
                        if k_index.issubset(paths):
                            print("Success")
                            return 0
                        elif intersect:
                            break
    else:
        print("Queen on board is more than 1 pieces")
        return 0
    
    # ถ้า King ไม่โดนเจอโดยเบี้ยตัวไหนเลยทุกเส้นทางการเดินที่เป็นไปได้โดยไม่ติดอุปสรรคจะแสดงคำว่า Fail ออกมา
    print("Fail")

# ตัวอย่างตารางเทียบกับตำแหน่ง K = [1,0], R = [2,0], P = [3,1]
# . . . .           [0,0] [0,1] [0,2] [0,3]
# . . . K    ->     [1,0] [1,1] [1,2] [1,3]
# R . . .           [2,0] [2,1] [2,2] [2,3]
# . B . .           [3,0] [3,1] [3,2] [3,3]
# ถ้า B จะเดินก็ต้องเดินเป็นตัว X ตำแหน่งที่ไปได้ก็คือ [2,0] กับ [[2,2], [1,3]]
# กำหนดให้ตำแหน่งด้านหน้าคือ j ด้านหลังคือ i ดังนั้นจากตัวอย่างของ Bishop
#       จะต้องทดลองเดิน 4 ทิศเพื่อเดินหา King จนกว่าจะสุดขอบกระดาน หรือ เจอเบี้ยตัวอื่นทำให้เดินต่อไม่ได้
#       ซึ่งจะขยับด้านหนึ่งตำแหน่ง j กับ i จะต้องเปลี่ยนที่ละ 1 ช่อง เช่น B ไปหา R ต้องเฉียงขึ้นซ้าย j - 1 กับ i - 1
#       จาก [3,1] -> [2,0]
#       ถ้าเจออุปสรรคแล้วก็หยุดเดินแล้วให้เปลี่ยนไปลองเดินทิศใหม่อย่างทางเฉียงขึ้นขวาวนไปเรื่อยๆจนกว่าจะครบ 4 ทิศ
#       ถ้าเจอ King แล้วก็จะพิมพ์ success และจบการทำงานด้วยการ return 0

# ดังนั้น ถ้า j - 1 = ขึ้นบน
#         j + 1 = ลงล่าง
#         i - 1 = ไปซ้าย
#         i + 1 = ไปขวา