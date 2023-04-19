girl_name= ('Samantha','Jada','Jade','Çlaire','Elizabeth','Mary','Susan','Waje','Taibat','Lilian')
girl_age = (17,16,17,18,16,18,17,20,19,17)
girl_height = (5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5)
girl_scores =(80,85,70,60,76,66,87,95,50,49)

boy_name = ('Charles','Jude','James','Kelvin','Biodun','Wale','Kunle','Matthew','Tom','Kayode')
boy_age = (19,16,18,17,20,19,16,18,17,19)
boy_height = (5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7)
boy_scores =(74,87,75,68,66,78,87,98,54,60)

print("Girls_name | Girls_age | Girls_height | Girls_score ")

for i in range(len(girl_name)):
    print (girl_name[i],"|",girl_age[i],"|",girl_height[i],"|",girl_scores[i])
print("\n")

print("Boys_name | Boys_age | Boys_height | Boys_score ")

for i in range(len(boy_name)):
    print (boy_name[i],"|",boy_age[i],"|",boy_height[i],"|",boy_scores[i])