import customtkinter as ctk

class SmartCashierApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Smart Cashier App")
        self.configure(bg="gray")

        self.configure_gui()

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

        # Create the layout
        self.create_calculator()
        self.create_item_list()

    def create_calculator(self):
        # Main container for left and right frames
        self.left_frame = ctk.CTkFrame(self, corner_radius=0)
        self.left_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        self.right_frame = ctk.CTkFrame(self, corner_radius=0)
        self.right_frame.pack(side=ctk.RIGHT, fill=ctk.BOTH, expand=True, padx=10, pady=10)
        
        # Back button
        back_button = ctk.CTkButton(
            self.left_frame, 
            text="Back", 
            width=100, 
            height=50, 
            corner_radius=10,
            fg_color="gray20",
            hover_color="gray30",
        )
        back_button.pack(side=ctk.TOP, anchor=ctk.NW, pady=10, padx=10)

        # Calculator Frame
        calculator_frame = ctk.CTkFrame(self.left_frame, width=300, height=400, corner_radius=10, fg_color="gray20")
        calculator_frame.pack(padx=10, pady=30)

        # Calculator display
        display = ctk.CTkLabel(
            calculator_frame, 
            text="", 
            height=50, 
            width=250, 
            fg_color="lightgreen", 
            corner_radius=10,
            text_color="black",
            anchor="e")
        display.pack(pady=10, padx=10)

        # Calculator buttons
        button_texts = [
            ["7", "8", "9", "÷"],
            ["4", "5", "6", "×"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
        ]
        for row in button_texts:
            button_row = ctk.CTkFrame(calculator_frame, fg_color="transparent")
            button_row.pack(pady=5)
            for text in row:
                button = ctk.CTkButton(
                    button_row, 
                    text=text, 
                    width=50, 
                    height=50, 
                    corner_radius=10,
                    fg_color="gray30",
                    text_color="white")
                button.pack(side=ctk.LEFT, padx=5)
 
    def create_item_list(self):
         # Left side (Product List)
        right_frame = ctk.CTkFrame(self.right_frame, corner_radius=0)
        right_frame.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=True, padx=10, pady=10)

        # Use CTkScrollableFrame instead of Canvas
        right_scrollable_frame = ctk.CTkScrollableFrame(right_frame, width=320, corner_radius=10)
        right_scrollable_frame.pack(fill=ctk.BOTH, expand=True)

        columns = 2  # Number of products per row

        # Add product widgets to the scrollable frame
        for i in range(20):  # Example product list
            product_frame = ctk.CTkFrame(
                right_scrollable_frame, 
                width=90,
                height=150,
                corner_radius=10, 
                fg_color="white")
            product_frame.grid(row=i // columns, column=i % columns, padx=10, pady=10, sticky="nsew")


            product_image = ctk.CTkLabel(
                product_frame, 
                width=180, 
                height=180, 
                text=f"Product {i+1}", 
                font=("Arial", 14),
                fg_color="gray",
                corner_radius=10)
            
            product_image.pack(anchor="center", padx=10, pady=10)

            product_label = ctk.CTkLabel(product_frame, text=f"Product {i+1}", font=("Arial", 18))
            product_label.pack(anchor="w", padx=5, pady=2)

            stock_label = ctk.CTkLabel(product_frame, text=f"Stock: {10 + i}")
            stock_label.pack(anchor="w", padx=5)

            category_label = ctk.CTkLabel(product_frame, text=f"price: Price {i%5}")
            category_label.pack(anchor="w", padx=5)


if __name__ == "__main__":
    app = SmartCashierApp()
    app.mainloop()
