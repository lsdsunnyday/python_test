class Dog():
	"""一次模拟小狗的简单测试"""

	def __init__(self,name,age):    #原来这个方法的两侧各有两条下划线
		"""初始化属性name和age"""
		self.name=name
		self.age=age

	def sit(self):
	   """模拟小狗被命令时蹲下"""
	   print(self.name.title()+" is now sitting.")

	 def roll_over(self):
	   """模拟小狗被命令时打滚"""
	   print(self.name.title()+" rolled over!")

my_dog = Dog("lele",7)
print("My dog's name is "+my_dog.name.title()+".")
print("My dog is "+str(my_dog.age)+" years old.")
my_dog.name
my_dog.sit()
my_dog.roll_over()



class Restaurant():
    """一次模拟餐馆的简单测试"""

    def __init__(self,restaurant_name,cuisine_type):    #原来这个方法的两侧各有两条下划线
        """初始化属性name和type"""
        self.name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print("The name of the restaurant is "+self.name.title()+".")
        print("The cuisine type of the restaurant is "+self.cuisine_type()+".")
    def open_restaurant(self):
        print(self.name.title()+" is open!")