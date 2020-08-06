# 파일 오픈 & 닫기
score_file = open('score.txt','w',encoding='utf8')
print('수학:0',file=score_file)
print('영어:19',file=score_file)
score_file.close()

# w는 쓰기 용도, a는 그 파일에 이어서 쓰는 것
score_file = open('score.txt','a',encoding='utf8')
score_file.write('과학:100')
score_file.write('\n코딩:100')
score_file.close()

#파일 읽어오기 r
score_file = open('score.txt','r',encoding='utf8')
print(score_file.read())

#한 줄씩 불러오기
score_file = open('score.txt','r',encoding='utf8')
print(score_file.readline())

# 몇 줄인지 모를 때 반복문 통해서 파일 불러오기
score_file = open('score.txt','r',encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()

#pickle 파일 형태로 저장하는 것 => 피클은 항상 바이너리 타입으로 정의, 인코딩은 할 필요 없음
import pickle
profile_file = open('profil.pickle','wb')
profile = {'이름':'이수현','나이':27,'취미':'코딩'}
print(profile)
pickle.dump(profile,profile_file) # profile에 있는 정보를 file에 저장
profile_file.close()

# 만든 파일 가져오기
profile_file = open('profil.pickle','rb')
profile = pickle.load(profile_file)
print(profile)
profile_file.close()

#with 쓰면 파일 열고 닫기 좀 더 편함
with open('study.txt','w', encoding='uft8') as study_file:
    study_file.write('파이썬을 공부하고 있어요')
