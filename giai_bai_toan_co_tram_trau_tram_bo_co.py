"""
Trăm trâu, trăm cỏ
Trâu đứng ăn năm
Trâu nằm ăn ba
Lụ khụ trâu già
Ba con một bó
Hỏi có bao nhiêu con trâu đứng, trâu nằm, trâu già
"""
for trau_dung in range(0, 21,1):
    for trau_nam in range(0,34,1):
        for trau_gia in range(0,101,1):
            if (trau_dung + trau_nam + trau_gia == 100) and (5*trau_dung + 3*trau_nam + trau_gia//3 == 100):
                print(f"Có {trau_dung} con trâu đứng, {trau_nam} con trâu nằm, {trau_gia} con trâu già")