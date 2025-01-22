import customtkinter as ctk
from PIL import Image


class DynamicGUIApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Dynamic GUI with Image")
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        # Get screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # Set the window size dynamically (80% of screen size)
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)
        x_position = int((screen_width - window_width) / 2)
        y_position = int((screen_height - window_height) / 2)

        self.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Store dimensions for dynamic resizing
        self.window_width = window_width
        self.window_height = window_height

    def create_widgets(self):
        # Main frame
        self.main_frame = ctk.CTkFrame(self, fg_color="gray")
        self.main_frame.pack(fill="both", expand=True)

        # Welcome section with an image
        self.create_welcome_section()

        # Panel section
        self.panel_frame = ctk.CTkFrame(self.main_frame, width=int(self.window_width * 0.4), fg_color="white")
        self.panel_frame.pack(side="right", fill="both")

        # Buttons for Log In and Sign Up
        self.login_button = ctk.CTkButton(self.panel_frame, text="Log In", command=self.show_login)
        self.login_button.place(relx=0.5, rely=0.3, anchor="center")

        self.signup_button = ctk.CTkButton(self.panel_frame, text="Sign Up", command=self.show_signup)
        self.signup_button.place(relx=0.5, rely=0.5, anchor="center")

    def create_welcome_section(self):
        # Frame for the welcome section
        self.welcome_frame = ctk.CTkFrame(self.main_frame, width=int(self.window_width * 0.6), fg_color="black")
        self.welcome_frame.pack(side="left", fill="both", expand=True)

        # Load and display the image
        image_path = "images/welcome-page.jpg"  # Replace with your image path
        try:
            image = Image.open(image_path)
            # Resize image to fully match the welcome frame
            image = image.resize((int(self.window_width * 0.6), self.window_height), Image.LANCZOS)
            self.ctk_image = ctk.CTkImage(light_image=image, dark_image=image, size=(int(self.window_width * 0.6), self.window_height))
            self.image_label = ctk.CTkLabel(self.welcome_frame, image=self.ctk_image, text="")
            self.image_label.pack(fill="both", expand=True)  # Ensure the label fills the entire frame
        except Exception as e:
            self.error_label = ctk.CTkLabel(
                self.welcome_frame, text="Image not found", text_color="white", font=("Arial", 24)
            )
            self.error_label.place(relx=0.5, rely=0.5, anchor="center")
            print(f"Error loading image: {e}")

    def show_login(self):
        self.clear_panel()
        login_label = ctk.CTkLabel(self.panel_frame, text="LOG IN", font=("Arial", 18), text_color="black")
        login_label.grid(row=0, column=0, columnspan=2, pady=10)

        email_label = ctk.CTkLabel(self.panel_frame, text="Email:", font=("Arial", 12))
        email_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        email_entry = ctk.CTkEntry(self.panel_frame, width=200)
        email_entry.grid(row=1, column=1, padx=10, pady=5)

        password_label = ctk.CTkLabel(self.panel_frame, text="Password:", font=("Arial", 12))
        password_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        password_entry = ctk.CTkEntry(self.panel_frame, width=200, show="*")
        password_entry.grid(row=2, column=1, padx=10, pady=5)

    def show_signup(self):
        self.clear_panel()
        signup_label = ctk.CTkLabel(self.panel_frame, text="Sign up", font=("Arial", 18), text_color="black")
        signup_label.grid(row=0, column=0, columnspan=2, pady=10)

        name_label = ctk.CTkLabel(self.panel_frame, text="Name:", font=("Arial", 12))
        name_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        name_entry = ctk.CTkEntry(self.panel_frame, width=200)
        name_entry.grid(row=1, column=1, padx=10, pady=5)

        email_label = ctk.CTkLabel(self.panel_frame, text="Email:", font=("Arial", 12))
        email_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        email_entry = ctk.CTkEntry(self.panel_frame, width=200)
        email_entry.grid(row=2, column=1, padx=10, pady=5)

        contact_label = ctk.CTkLabel(self.panel_frame, text="Contact Number:", font=("Arial", 12))
        contact_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        contact_entry = ctk.CTkEntry(self.panel_frame, width=200)
        contact_entry.grid(row=3, column=1, padx=10, pady=5)

        password_label = ctk.CTkLabel(self.panel_frame, text="Password:", font=("Arial", 12))
        password_label.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        password_entry = ctk.CTkEntry(self.panel_frame, width=200, show="*")
        password_entry.grid(row=4, column=1, padx=10, pady=5)

    def clear_panel(self):
        for widget in self.panel_frame.winfo_children():
            widget.destroy()


# Run the app
if __name__ == "__main__":
    app = DynamicGUIApp()
    app.mainloop()
