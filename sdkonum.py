korean_numbers = {'영': '0', '공': '0', '빵': '0', '일': '1', '하나': '1', '이': '2', '둘': '2', '삼': '3', '셋' : '3', '사': '4', '넷': '4', '오': '5', '육': '6', '칠': '7', '팔': '8', '구': '9', '에': '-'}

def to_num(text):
    text += ' '
    temp_num_idx = []
    num_count = 0
    num_space = 0
    dasi_flag = False
    ten_flag = False
    
    for idx, char in enumerate(text):
        # print(f'idx : {idx}, char : {char}, num_count : {num_count}')
        if char == ' ' or dasi_flag:
            if num_count:
                num_space += 1
            dasi_flag = False
            continue
        
        if ten_flag:
            ten_flag = False
            continue

        if char == '십':
            ten_flag = True
            num_count = 0
            continue

        if char in korean_numbers:
            num_count += 1
        else:
            if char == '다' and text[idx+1]== '시':
                num_count += 1
                dasi_flag = True
                if num_count == 4:
                    num_start_idx = idx - (3 + num_space)
                continue
            
            if char == '하' and text[idx+1]=='나':
                num_count += 1
                dasi_flag = True
                if num_count == 4:
                    num_start_idx = idx - (3 + num_space)
                continue

            if num_count >= 4:
                num_end_idx = idx
                temp_num_idx.append((num_start_idx, num_end_idx))
            num_count = 0
            num_space = 0
        
        if num_count == 4:
            num_start_idx = idx - (3 + num_space)
            
    if num_count >=4:
        num_end_idx = idx
        temp_num_idx.append((num_start_idx, num_end_idx))

    if temp_num_idx:

        temp_text_start_idx = 0
        temp_text = ''
        for i in temp_num_idx:
            temp_text += text[temp_text_start_idx:i[0]]
            temp_text_start_idx = i[1]
            for j in text[i[0]:i[1]]:
                if j == ' ' or j == '다' or j == '하':
                    continue
                if j == '시':
                    temp_text += '-'
                    continue
                if j == '나':
                    temp_text += '1'
                    continue
                temp_text += korean_numbers[j]
                    
        temp_text += text[temp_text_start_idx:]
        text = temp_text

    return text

if __name__ == "__main__":
    text = '전화번호는 공 일 공에 하나둘셋넷 다시 영공빵오다 주소는 서울시 이 팔 팔 다시 육삼오입니다'
    result = to_num(text)
    print(result)
