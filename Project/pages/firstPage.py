import flet as ft;
import array as arr;
class FriendCard(ft.UserControl):
   
   name = "noName"
   BG = '#041955'
   FWG = '#97b4ff'
   FG = '#3450a1'
   PINK = '#eb06ff'
   WHITE = '#FFFFFF'
   friendlist = []
   def __init__(self, n,d,friendlist):
        super().__init__()
        self.friendlist = friendlist
        self.name = n
        self.deleteFriend = d
   def deleteClicked(self,e):
        self.deleteFriend(self)
        self.update()
   def build(self):
      
      return  ft.Container(
                
            border_radius=20,
            bgcolor=self.FWG,
            width=150,
            height=110,
            padding=15,
            content=ft.Column(
                controls=[
                    ft.ElevatedButton("Pay",
                        on_click=self.deleteClicked, bgcolor="green"
                    ),
                    ft.Row(alignment='center', controls=[ft.Text(self.name) ]),
                    ft.Row(alignment='center',
                           controls=[
                               ft.Container(
                                   border_radius=20,
                                   bgcolor=self.FWG,
                                   width=85,
                                   height=45,
                                   padding=15,
                                   content=ft.Container(

                                   )
                               )
                           ]
                           )
                ]
            )
        )
class Friend():
   name = ""
   username = ""
  
  
class Friends():
   
   friends = [arr]

   def __init__(self,friends:arr):
    self.friends = friends
    
   def getFriends(self):
    return self.friends
   
   def addFriend(self,name):
      f = Friend()
      f.name = name
      self.friends.append(f)
      return
      
class Group():
   owner = ""
   name = ""
   members = []

   def addMember(self,friend:Friend):
     self.members.append(friend)

   def removeMember(self,friend:Friend):
     self.members.remove(friend)  

class Groups():
  groups = []

  def addGroup(self,group:Group):
     self.groups.append(group)

  def removeGroup(self,group:Group):
     self.groups.remove(group)


class Bill():
   group = 0
   total = 0
   splitby =1
   def __init__(self,group:Group):
    self.group = group
   
   def getGroup(self):
      return self.group
class FriendsList(ft.UserControl):
    listOfFriends = ft.Row()
    
    friends = []
    def renderFriends():
       return
    def build(self):
      return  self.listOfFriends
    
    def deleteFriend(self, friend:FriendCard):
        self.listOfFriends.controls.remove(friend)
        self.update()
        return
    def addFriend(self,name):
        self.listOfFriends.controls.append(FriendCard(name,self.deleteFriend,0))
        
        self.update()
        return

   
class Users():

    users = ["avery","tommy","ethan","derek","todd","justin","michael"]

    def findUsers(self,str):
     matches = []
     for i in range(len(self.users)):
        if(str in self.users[i] ):
           print(self.users[i])
           matches.append(self.users[i])

        print(matches)
     return matches
    


class SearchBar(ft.UserControl):
   changeText = 0
   
   page = 0
   def onChangeText(self,e):
      self.changeText(e.control.value)


   def __init__(self,onChangeText):
      super().__init__()
      self.changeText = onChangeText
      
   
   #Ui for searchbar 
   def build(self):
      return ft.TextField(
            label="avery",
            icon=ft.icons.FORMAT_SIZE,
            hint_text="type a username",
            helper_text="",
            counter_text="0 symbols typed",
            prefix_icon=ft.icons.SEARCH,
            suffix_text="",
            on_change =  self.onChangeText
     )
   
class userCard(ft.UserControl):
   addFriend = 0
   def __init__(self,name,addFriend):
      super().__init__()
      self.addFriend = addFriend
      self.name = name
   
   def build(self):
      return ft.Container(content = ft.Column(controls=[
                   ft.IconButton(
                    icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.GREEN,
                    tooltip="Update To-Do",
                    #on_click=self.addFriend,
                    data=(self.name),  ## <-------------------- store the reference to the button in a tuple. You could store it in a dictionary or whatever else you want
                   on_click=lambda e: self.addFriend(e.control.data)
                ),ft.Text(self.name)]))  

   
class SearchResults(ft.UserControl):
     lv = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
     def build(self):
       
       return self.lv
     
     def render(self,itemsToRender):
        self.lv.controls.clear()
        
        for i in range(len(itemsToRender)):
         self.lv.controls.append(itemsToRender[i])   
        
         
         self.update()

class FirstPage(ft.UserControl):  
   
   
   def __init__(self,page):
      super().__init__()
      self.users = Users()
      self.friends = FriendsList()
      self.searchResults = SearchResults()
      self.page = page
   
   def addFriend(self,name):
        self.friends.addFriend(name)
        #friends.append(name)
        self.page.update()
        return
     
   def createSearchResults(self,items):
        results = []
        print(items)
        for i in range(len(items)):
         results.append(userCard(items[i],self.addFriend))
         
        self.searchResults.render(results)
        self.page.update()
   
   def updateText(self,e):
       self.createSearchResults(self.users.findUsers(e))
       return
   
   def build(self):
    searchBar = SearchBar(self.updateText)
    return ft.Container(content = ft.Column(controls =[
       searchBar,
       self.searchResults,
       self.friends
    ]))


   