import customtkinter as ctk
from sqlalchemy import column

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

        # Set window size to 80% of screen size
        self.screen_width  = int(screen_width)
        self.screen_height = int(screen_height)
        # Set the window size dynamically (80% of screen size)
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        self.configure_frames()

    def configure_frames(self):
        # Main frame/Top frame
        self.main_frame = ctk.CTkFrame(
            self, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=int(self.screen_height * 0.1))
        
        self.main_frame.pack(
            fill=ctk.BOTH, 
            expand=True,
            pady=10)

        # Top bar
        top_frame = ctk.CTkFrame(self.main_frame, corner_radius=0)
        top_frame.pack(side=ctk.TOP, fill=ctk.X)  # Use `pack` for top_frame itself

        # Use `grid` for arranging widgets inside `top_frame`
        group_label = ctk.CTkLabel(top_frame, text="Group Name", font=ctk.CTkFont(size=16, weight="bold"))
        group_label.grid(row=0, column=0, padx=10, sticky="w") 

        search_entry = ctk.CTkEntry(top_frame, placeholder_text="Search...")
        search_entry.grid(row=0, column=1, padx=5, sticky="w") 

        search_button = ctk.CTkButton(top_frame, text="Search", fg_color="transparent", text_color="white")
        search_button.grid(row=0, column=2, padx=5, sticky="w") 

        cart_button = ctk.CTkButton(top_frame, text="Cart", fg_color=None, text_color="black")
        cart_button.grid(row=0, column=3, padx=5, sticky="e") 

        account_button = ctk.CTkButton(top_frame, text="Account", fg_color=None, text_color="black")
        account_button.grid(row=0, column=4, padx=5, sticky="e") 

        # Button Frames
        self.button_frame = ctk.CTkFrame(
            self, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=int(self.screen_height * 0.1),
            border_color="blue")
        self.button_frame.pack(fill=ctk.BOTH, expand=True)

        # Cart Frames
        self.cart_frame = ctk.CTkFrame(
            self, 
            corner_radius=0, 
            width=int(self.screen_width * 0.7),
            height=int(self.screen_height * 0.8),
            border_color="red")
        self.cart_frame.pack(fill=ctk.BOTH, expand=True)


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

        

        # Content frame
        content_frame = ctk.CTkFrame(self.cart_frame, corner_radius=0)
        content_frame.pack(fill=ctk.BOTH, expand=True)

        # Left side (Product List)
        left_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Use CTkScrollableFrame instead of Canvas
        left_scrollable_frame = ctk.CTkScrollableFrame(left_frame, width=720, corner_radius=10)
        left_scrollable_frame.pack(fill=ctk.BOTH, expand=True)

        columns = 3  # Number of products per row

        # Add product widgets to the scrollable frame
        for i in range(20):  # Example product list
            product_frame = ctk.CTkFrame(
                left_scrollable_frame, 
                width=90,
                height=150,
                corner_radius=10, 
                fg_color="white")
            product_frame.grid(row=i // columns, column=i % columns, padx=10, pady=10, sticky="nsew")


            product_image = ctk.CTkLabel(
                product_frame, 
                width=200, 
                height=200, 
                text=f"Product {i+1}", 
                font=("Arial", 14),
                fg_color="gray",
                corner_radius=10)
            
            product_image.pack(anchor="center", padx=10, pady=10)

            product_label = ctk.CTkLabel(product_frame, text=f"Product {i+1}", font=("Arial", 14))
            product_label.pack(anchor="w", padx=5, pady=2)

            barcode_label = ctk.CTkLabel(product_frame, text=f"Barcode: {100000 + i}")
            barcode_label.pack(anchor="w", padx=5)

            stock_label = ctk.CTkLabel(product_frame, text=f"Stock: {10 + i}")
            stock_label.pack(anchor="w", padx=5)

            category_label = ctk.CTkLabel(product_frame, text=f"Category: Category {i%5}")
            category_label.pack(anchor="w", padx=5)

            add_to_cart_button = ctk.CTkButton(product_frame, text="Add to Cart", fg_color="red", text_color="white")
            add_to_cart_button.pack(anchor="e", padx=5, pady=5)

        # Right side (Shopping Cart)
        right_frame = ctk.CTkFrame(content_frame, corner_radius=0)
        right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Use CTkScrollableFrame for the shopping cart
        right_scrollable_frame = ctk.CTkScrollableFrame(right_frame, width=300, corner_radius=10)
        right_scrollable_frame.pack(fill=ctk.BOTH, expand=True)

        cart_label = ctk.CTkLabel(right_scrollable_frame, text="Shopping Cart", font=("Arial", 16))
        cart_label.pack(pady=10)

        # Example cart items
        for i in range(5):
            cart_item_label = ctk.CTkLabel(right_scrollable_frame, text=f"Cart Item {i+1}")
            cart_item_label.pack(anchor="w", padx=10, pady=5)

if __name__ == "__main__":
    #root = ctk.CTk()
    app = ShoppingApp()
    app.mainloop()