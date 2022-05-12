#6-a
nested_lst=[[1,2,3], [4,5,6], [7,8,9]]
ans_1= nested_lst[1] [1]
print(ans_1)

#6-b
nested_lst1 = [["Hat", "Glove", "Goggle"], ["Button", "Zipper", "Hook"]]
ans_2=nested_lst1 [1] [1] [0]
print(ans_2)

#6-c
nested_lst2= [{"orange": "orange"}, {"rose": "red"}, {"violet": "blue"}]
ans_3=nested_lst2 [2] ["violet"]
print(ans_3)

#6-d
nested_dict={"Dakar":{"weather":"sunny","roads": "dry"}}
ans_4=nested_dict["Dakar"] ["roads"]
print(ans_4)

#6-e
nested_dict1= {"Tokyo": {"weather":["sunny", "cloudy"], "roads":"dry"}, "Dakar": {"weather":["foggy","windy"], "roads": "sandy"}}
ans_5=nested_dict1["Tokyo"] ["weather"] [0]
print(ans_5)