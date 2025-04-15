# del keyword >
# used to delete object properties or object itself. 
# del s1.name
# del s1

# example
# class Student:
#     def __init__(self, name):
#         self.name = name

# s1 = Student("sachin")
# print(s1.name)
# del s1.name
# print(s1.name)



# private (like) attributes & methods
# conceptual implementations in python
# private attributes & methods are meant to be used only within the clas and are not accessible from outside the class.
# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person!")

#     def welcome(self):
#         self.__hello()

# p1 = person()
# print(p1.welcome())



# inheritance
# when one class(child/drived) derives the properties & methods of another class(parent/base).
# class car:
#     color = "black"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped...")

# class toyotaCar(car):
#     def __init__(self,name):
#         self.name = name

# car1 = toyotaCar("fortuner")
# car2 = toyotaCar("xyz")
# print(car1.color)








# inheritance types> 
# single->in this we can accesss only the single class.

# class parent:
#     def show_parent(self):
#         print("this is the parent class")

# class child(parent):
#     def show_child(self):
#         print("this is the child class")

# c = child()
# c.show_parent()
# c.show_child()




#hierarchical-> it works as a single parent as two childs and every child having the parent DNA 
# class parent:
#     def show_parent(self): 
#         print("this is the parent class")

# class child1(parent):
#     def show_child1(self):
#         print("this is the first child")
# class child2(parent):
#     def show_child2(self):
#         print("this is the second child")

# c = child1()
# d = child2()
# c.show_parent()
# c.show_child1()
# d.show_parent()
# d.show_child2()

# hybrid *********************************************  
 
 
# multi-level-> in this cse we can create the multiple level classes to acces with the child class.
# class grandparent:
#     def show_grand(self):
#         print("this is the grand parent class")
# class parent(grandparent):
#     def show_parent(self):
#         print("this is the parent class ")
# class child(parent):
#     def show_child(self):
#         print("this is the child class")


# child1 = child()
# child1.show_grand()
# child1.show_parent()
# child1.show_child()






#mltiple inheritance-> in this case we can access the multiple parent classes
# class mother:
#     def show_mother(self):
#         print("this is the mother class")
# class father:
#     def show_father(self):
#         print("this is the father class")

# class child(father,mother):
#     def show_child(self):
#         print("this is the child class")

# c = child()
# c.show_mother()
# c.show_father()
# c.show_child()



#*********** polimorphism>*******************
# class Bird:
#     def fly(self):
#         print("bird is flying")

# class airplane:
#     def fly(self):
#         print("the airplane is flying")

# bird = Bird()
# air = airplane()

# bird.fly()
# air.fly()   



# run time polymorphism(Dynamic polymorphism)-> method overriding-> ye type ka polymorphism runtime per resolve hota hai. python me yeh method overriding ke through achieve hota hai.
# class animal:
#     def animal_sound(self):
#         print("animal makes sounds diffrently...")

# class dog(animal):
#     def dog_sound(self):
#         print("dogs barks at strangers")
# class cat(animal):
#     def cat_sound(self):
#         print("cat meows at night")

# # object
# pets = animal()
# pet1 = dog()
# pet2 = cat()

# # function call
# pets.animal_sound()
# pet1.dog_sound()
# pet2.cat_sound()


# compile time polimorphism ->method/function overloding,oprator overloading->yeh type ka polymorphis compile time per resolve hota hai. python me yeh method overloding aur oprator overloadingke through achive hota hai(although python me direct method overriding support
# nahi hai, lekin hum default arguments ya variable-length arguments ka use kar sakte hain)
# class calculator:
#     def cal(self, a, b, c=0):
#         print(a+b+c)
# cal1 = calculator()
# cal1.cal(2,4)
# cal1.cal(2,4,8)







# polymorphism in real wolrd scenario
# imagine kariye ek software application jo diffrent types of media 
# files ko play karta hai jaise audio or video files,
# hum ek mediaplayer class create kar sakte hain jo play method ko define
# karega, aur phir audioplayer aur videoplayer classes inherit karegi mediaplayer
# class ko aur play ethod ko override karengi apne specific behavior ke liye.

# class media_player:
#     def play(self):
#         print("playing media")

# class audio_player(media_player):
#     def audio(self):
#         print("playing audio file...")

# class video_player(media_player):
#     def video(self):
#         print("playing the video file...")


# m = media_player()
# a = audio_player()
# v = video_player()

# m.play()
# a.audio()
# v.video()

