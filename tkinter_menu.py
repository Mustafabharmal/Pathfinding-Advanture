import tkinter as tk
from PIL import Image, ImageTk

class Menu:
   
  
   def create_menu(self):
      
      root = tk.Tk()
      root.attributes('-fullscreen', True)
      def play():
         root.destroy()
      # root.state("iconic")
      root.wm_title('Start Menu for Treasure Hunt')
      bg = Image.open( "graphics/background/BackgroundMenu1.png")
      resize_image = bg.resize((1920 ,1080))
      img = ImageTk.PhotoImage(resize_image)
      img_label = tk.Label(root, image = img)
      img_label.place(x = 0, y = 0,anchor='center', relx=0.5, rely=0.5)

      Play_Buttton = tk.Button(root, bg='#182f3e', fg='white',font=("Times", 40, 'bold'),command=play, default="active")
      Play_Buttton['text'] = 'Play'
      Play_Buttton.place(x=500,y=430,width=300,height=80)

      Exit_Buttton = tk.Button(root, bg='#182f3e', fg='white',font=("Times new roman", 40, 'bold'),command=exit, default="active")
      Exit_Buttton['text'] = 'Exit'
      Exit_Buttton.place(x=500,y=530,width=300,height=80)
      root.mainloop()

  

