import flet as ft;
import array as arr;
BG = '#00D632'
WHITE = '#FFFFFF'

class Navigation(ft.UserControl):
     def change(self,e):
        self.changeFunc(e)
        return
     def __init__(self,func):
        super().__init__()
        self.changeFunc = func
   #   text = "a"
     def build(self):
        return ft.Container(
           padding= ft.padding.only(100,100,0,0) ,
           content =ft.NavigationBar(
          
        on_change= self.change,
        
        destinations=[
            ft.NavigationDestination(icon=ft.icons.PEOPLE, label="Friends"),
            ft.NavigationDestination(icon=ft.icons.CARD_GIFTCARD, label="Bill"),
            ft.NavigationDestination(
                icon=ft.icons.BOOKMARK_BORDER,
                selected_icon=ft.icons.BOOKMARK,
                label="Explore",
            ),
        ]
      ))

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
class SecondPage(ft.UserControl):

   def build(self):

      return ft.Container(
        content=ft.Column(
            controls=[
                ft.Container(
                    content=ft.Text('Add Bill', size=20, weight=ft.FontWeight.BOLD),
                    bgcolor='green',
                    padding=ft.padding.all(10),
                ),

                ft.Container(
                    content=ft.TextField(
                        label="Add Title for Bill",
                        hint_text="Add Title here",
                        width=380,
                        border_color="green",
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.TextField(
                        label="Amount",
                        hint_text="Add Amount here",
                        width=380,
                        border_color="green",
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.Dropdown(
                        label="Bill or Expense",
                        hint_text="click for options",
                        width=380,
                        border_color="green",
                        options=[
                            ft.dropdown.Option("Bill"),
                            ft.dropdown.Option("Expense"),
                        ],
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.Dropdown(
                        label="Select Group",
                        hint_text="click for options",
                        width=380,
                        border_color="green",
                        options=[
                            ft.dropdown.Option("Group 1"),
                            ft.dropdown.Option("Group 2"),
                            ft.dropdown.Option("Group 3"),
                        ],
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.Dropdown(
                        label="Split Actions",
                        hint_text="click for options",
                        width=380,
                        border_color="green",
                        options=[
                            ft.dropdown.Option("Split equally"),
                            ft.dropdown.Option("Custom"),
                            ft.dropdown.Option("According to item"),
                        ],
                    ),
                    margin=ft.margin.only(top=10),
                ),

                ft.Container(
                    content=ft.ElevatedButton(
                        text='Save',
                       # on_click=open_dlg_modal_bill,
                        bgcolor='green',
                        width=100
                    ),

                    margin=ft.margin.only(top=20),
                ),

                ft.Text(),
            ]
        )
    )
   
class ThirdPage(ft.UserControl):
  def  __init__(self,page):
   super().__init__()
   self.page = page
   self.textfield_dialog = ft.AlertDialog(
        modal=True,
        title=ft.Text("Enter Payment tag"),
        actions=[
            ft.TextField(label="click here", width=200),
            ft.TextButton("Submit", on_click=self.close_textfield),
            ft.ElevatedButton("CANCEL", bgcolor="red", on_click=self.close_textfield),
        ],
        on_dismiss=lambda e: print("Modal dismissed"),
  ) 
   self.dlg_modal_settings = ft.AlertDialog(
        modal=True,
        title=ft.Text("              Choose payment method"),
        actions=[
            ft.ElevatedButton("Cashapp", bgcolor = BG, color=WHITE, icon_color = WHITE, icon="attach_money", on_click=self.open_textfield),
            ft.ElevatedButton("PayPal", bgcolor = '#00457C', color=WHITE, icon_color = WHITE, icon="paypal", on_click=self.open_textfield),
            ft.ElevatedButton("Venmo", bgcolor = '#008CFF', color=WHITE, icon_color = WHITE, icon="v", on_click=self.open_textfield),
            ft.ElevatedButton("CANCEL", bgcolor="red", color=WHITE, icon_color = WHITE, on_click=self.close_dlg_settings),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),
    )
   self.dlg_modal_profile = ft.AlertDialog (
        modal = True,
        title = ft.Text("Edit Profile"),
        actions = [
            ft.ElevatedButton("Edit Name", bgcolor = WHITE, color=BG, icon_color =BG, icon="drive_file_rename_outlined", on_click=self.open_textfield),
            ft.ElevatedButton("Edit Picture", bgcolor = WHITE, color=BG, icon_color=BG, icon="picture_as_pdf_outlined", on_click= self.open_textfield),
            ft.ElevatedButton("CANCEL", bgcolor="red", color=WHITE, icon_color = WHITE, on_click=self.close_dlg_settings),

        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: print("Modal dismissed"),

    )
   

  def close_textfield(self,e):

        self.textfield_dialog.open = False
        self.dlg_modal_settings.open = False
        self.page.update()

  def open_textfield(self,e):
        self.page.dialog = self.textfield_dialog
        self.page.dialog.open = True
        self.page.update()

  def open_dlg_modal_settings(self,e):
        self.page.dialog = self.dlg_modal_settings
        self.dlg_modal_settings.open = True
        self.page.update()      
  def close_dlg_settings(self):
        self.page.dialog.open = False
        self.page.update()
 

  

  


  def build(self):
    
      return ft.Container(
        width = 400, 
        height = 850,
        bgcolor= BG, 
        border_radius = 20,
        padding = ft.padding.only(left = 10, top = 60, right = 200),
        margin = ft.margin.only(left = -40), 
        content = ft.Column(
            controls = [
                ft.Container(height =20), 
                ft.Row(
                    controls = [
                        ft.Container(padding=ft.padding.all(5),
                          bgcolor=WHITE,
                          width=90,height=90,
                          border_radius=50,
                          content=ft.Container(bgcolor=WHITE,
                            height=70,width=70,
                            border_radius=40,
                            content=ft.CircleAvatar(opacity=0.9,
                            foreground_image_url="https://bloximages.newyork1.vip.townnews.com/nola.com/content/tncms/assets/v3/editorial/4/69/469f1c32-6f4b-5c5d-b24f-f567206d6a2d/60c3ec1d12eeb.image.jpg?resize=362%2C500"
                            )
                          )
                        )
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.PERSON, color = WHITE), 
                        ft.Text('Dos Acker',size=30,weight='bold', color = WHITE), 


                    ]
                ),
                ft.Row( alignment= 'right', 
                    controls = [
                        ft.Text('______________________________________________________________', color = WHITE)
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.ATTACH_MONEY, color = WHITE),
                        ft.Container(
                            content=ft.ElevatedButton(
                                text='Add new Payment',
                                color = BG,
                                on_click = self.open_dlg_modal_settings,
                                bgcolor=WHITE,
                                width=200
                            ),

                    ),
                    ]
                ),
                ft.Row(
                    controls = [
                        ft.Icon(ft.icons.EDIT_OUTLINED, color =WHITE),
                        ft.Container(
                            content=ft.ElevatedButton(
                                text='Edit profile',
                                color = BG,
                                on_click=self.open_dlg_modal_settings,
                                bgcolor=WHITE,
                                width=200
                            ),

                    ),
                
                    ]
                )
                

            ]
        )
        

    )
    
    


 
def main(page: ft.Page):
      
     firstPage = FirstPage(page)
     secondPage = SecondPage()
     thirdPage = ThirdPage(page)
     
     secondPage.visible = False
     thirdPage.visible = False

     def changetab(e):
        my_index = e.control.selected_index
        firstPage.visible = True if my_index == 0 else False
        secondPage.visible = True if my_index == 1 else False
        thirdPage.visible = True if my_index == 2 else False
        page.update()
        
      
     n = Navigation(changetab)  
     c = ft.Container(content=ft.Column(controls = [firstPage,secondPage,thirdPage]))
     page.add(n)
     page.add(c)
      
     page.update()
      
     
ft.app(target=main)

