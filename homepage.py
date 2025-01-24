from textwrap import fill
import customtkinter as ctk
from sqlalchemy import column
from PIL import Image

class ShoppingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Cashier App")
        self.configure_gui()
        self.background_color = ""

    def configure_gui(self):
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.screen_width  = int(screen_width)
        self.screen_height = int(screen_height)

        # Set the window size dynamically (80% of screen size)
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.configure_top()

    def configure_top(self):
        # Main frame/Top frame
        self.main_frame = ctk.CTkFrame(
            self, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=50)
        
        self.main_frame.pack(
            fill=ctk.BOTH, 
            #expand=True,
            pady=10)

        # Top bar
        top_frame = ctk.CTkFrame(self.main_frame, height=30,corner_radius=0)
        top_frame.pack(side=ctk.TOP, fill=ctk.X, padx=20, pady=20)  # Use `pack` for top_frame itself

        # Configure columns in the grid
        top_frame.grid_columnconfigure(0, weight=3)
        top_frame.grid_columnconfigure(1, weight=0)
        top_frame.grid_columnconfigure(2, weight=0)

        # Use `grid` for arranging widgets inside `top_frame`
        group_label = ctk.CTkLabel(
            top_frame, 
            text="Group Name", 
            font=ctk.CTkFont(size=14, weight="bold"),
            fg_color="transparent")
        group_label.grid(row=0, column=0, columnspan=2, padx=30, sticky="w") 

        search_entry = ctk.CTkEntry(top_frame, width=200, placeholder_text="Search...")
        search_entry.grid(row=0, column=1, padx=5, sticky="w") 

        search_button = ctk.CTkButton(top_frame, width=40, text="Search", fg_color="red", text_color="white")
        search_button.grid(row=0, column=2,  padx=0, sticky="w") 

        account_frame = ctk.CTkFrame(top_frame, width=100, height=30, corner_radius=0)
        account_frame.grid(row=0, column=3, padx=5, sticky="w")
        cart_button = ctk.CTkButton(account_frame, text="Cart", fg_color=None, text_color="black")
        cart_button.grid(row=0, column=0, padx=5, sticky="w") 

        account_button = ctk.CTkButton(account_frame, text="Account", fg_color=None, text_color="black")
        account_button.grid(row=0, column=1, padx=5, sticky="w") 

        """
        Shows the middle part of the GUI: Navigation Buttons
        """
        # Button Frames
        self.button_frame = ctk.CTkFrame(
            self,
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=50,
            border_color="blue")
        self.button_frame.pack(fill=ctk.BOTH)

       # Navigation buttons
        nav_buttons = ["Home", "Shop", "SCAN", "Calculator", "Contact"]
        for btn in nav_buttons[::-1]:
            nav_button = ctk.CTkButton(
                self.button_frame, 
                corner_radius=0, 
                text=btn, 
                fg_color=None, 
                text_color="black",
                height=30,
                width=50,
                bg_color="transparent")
            nav_button.pack(side=ctk.RIGHT, padx=5)

        self.configure_description()

## DELETE HERE IF THERE'S A COLOR PALETTE ALREADY----------------------------------------------------------------------
    def configure_description(self):
        # Main container for left and right frames
        self.cart_frame = ctk.CTkFrame(
            self, 
            corner_radius=0, 
            width=int(self.screen_width),
            height=int(self.screen_height),
            border_color="red")
        self.cart_frame.pack(fill=ctk.BOTH, expand=True)

        # Content frame
        image_frame = ctk.CTkFrame(self.cart_frame, corner_radius=0)
        image_frame.pack(fill=ctk.BOTH, expand=True, pady=10)

        # Left side (Product List) - 70% width
        left_frame = ctk.CTkFrame(image_frame, corner_radius=0, width=int(self.screen_width * 0.6))
        left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
        """
        # Use CTkLabel for the left side placeholder
        left_scrollable_frame = ctk.CTkLabel(
            left_frame, 
            corner_radius=10, 
            fg_color="white", 
            text="IMAGE HERE",
            text_color="black")
        left_scrollable_frame.pack(fill=ctk.BOTH, expand=True)
        """
        # Load and display the image
        image_path = "images/home-page.jpg"  
        try:
            image = Image.open(image_path)
            # Resize image to fully match the welcome frame
            image = image.resize((int(self.screen_width * 0.6), self.screen_height), Image.LANCZOS)
            self.ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(int(self.screen_width * 0.45), int(self.screen_height*0.6)))
            self.image_label = ctk.CTkLabel(left_frame, image=self.ctk_image, text="")
            self.image_label.pack(fill="both", expand=True)  # Ensure the label fills the entire frame
        except Exception as e:
            self.error_label = ctk.CTkLabel(
                left_frame, text="Image not found", text_color="white", font=("Arial", 24)
            )
            self.error_label.place(relx=0.5, rely=0.5, anchor="center")
            print(f"Error loading image: {e}")

        # Right side (Shopping Cart) - 30% width
        right_frame = ctk.CTkFrame(image_frame, corner_radius=0, height=int(self.screen_width * 0.6), width=int(self.screen_width * 0.4))
        right_frame.pack(side=ctk.RIGHT, padx=10, pady=10, fill=ctk.BOTH)

        # Add title label
        cart_title_label = ctk.CTkLabel(
            right_frame, 
            text="Smart Cart", 
            font=("Arial", 20, "bold"),
            text_color="black")
        cart_title_label.grid(row=0, column=0, pady=10)

        # Add description label with wrapping
        cart_description_label = ctk.CTkLabel(
            right_frame, 
            text=(
"About Smart Shopping Assistant with barcode scanning for managing inventory. "
"Admins can add, update, or remove items and sync data with an Excel file. "
"Customers can scan products, add them to the cart, and view a summary with total cost. "
"Uses Python, SQLite, OpenCV, and pyzbar."
            ),
            font=("Arial", 15),
            text_color="black",
            wraplength=int(self.screen_width * 0.20))  # Wrap text to fit within 28% of screen width
        cart_description_label.grid(row=1, column=0, sticky="w",pady=10, padx=10)

        # Add "Start Shopping" Button
        start_shopping_button = ctk.CTkButton(
            right_frame, 
            text="Start Shopping", 
            font=("Arial", 15),
            text_color="black")
        start_shopping_button.grid(row=2, column=0, pady=10)

    
if __name__ == "__main__":
    #root = ctk.CTk()
    app = ShoppingApp()
    app.mainloop()