import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
import json
import os
from typing import Dict, Optional
import math


class SpeakUpApp:
    """Enhanced Speak Up and Learn application with improved structure and features."""
    
    def __init__(self):
        self.root = tk.Tk()
        self.users_file = "users.json"
        self.users = self.load_users()
        self.setup_window()
        self.setup_styles()
        self.create_login_interface()
        
    def setup_window(self):
        """Configure the main window."""
        self.root.title("Speak Up and Learn - Enhanced Login")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f8ff")
        
        # Center the window on screen
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
        
    def setup_styles(self):
        """Define application styles and colors."""
        self.colors = {
            'primary': '#2E86AB',
            'secondary': '#A23B72',
            'success': '#4CAF50',
            'warning': '#FF9800',
            'danger': '#F44336',
            'info': '#2196F3',
            'light': '#F8F9FA',
            'dark': '#343A40',
            'white': '#FFFFFF'
        }
        
        self.fonts = {
            'title': ('Segoe UI', 24, 'bold'),
            'heading': ('Segoe UI', 18, 'bold'),
            'subheading': ('Segoe UI', 14, 'bold'),
            'body': ('Segoe UI', 12),
            'small': ('Segoe UI', 10)
        }
        
        # Logo colors matching your brand
        self.logo_colors = {
            'speech_bubble': '#2E86AB',  # Dark teal
            'microphone': '#FFFFFF',     # White
            'plant_stem': '#FF6B35',    # Orange
            'plant_leaf': '#4ECDC4',    # Light teal
            'plant_leaf2': '#FF6B35'    # Orange
        }
        
    def load_users(self) -> Dict[str, str]:
        """Load users from JSON file or create default."""
        if os.path.exists(self.users_file):
            try:
                with open(self.users_file, 'r') as f:
                return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return {"admin": self.hash_password("admin123")}
        return {"admin": self.hash_password("admin123")}
        
    def save_users(self):
        """Save users to JSON file."""
        try:
            with open(self.users_file, 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save users: {str(e)}")
            
    def hash_password(self, password: str) -> str:
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()
        
    def validate_username(self, username: str) -> bool:
        """Validate username format."""
        if len(username) < 3:
            return False
        if not username.isalnum():
            return False
        return True
        
    def validate_password(self, password: str) -> bool:
        """Validate password strength."""
        if len(password) < 6:
            return False
        return True
        
    def create_gradient_background(self, canvas, width, height, color1, color2):
        """Create a gradient background."""
        r1, g1, b1 = color1
        r2, g2, b2 = color2
        
        for i in range(height):
            r = int(r1 + (r2 - r1) * i / height)
            g = int(g1 + (g2 - g1) * i / height)
            b = int(b1 + (b2 - b1) * i / height)
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(0, i, width, i, fill=color, width=1)
            
    def create_login_interface(self):
        """Create the main login interface."""
        # Create canvas for gradient background
        canvas = tk.Canvas(self.root, width=600, height=500, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        # Create gradient background
        self.create_gradient_background(canvas, 600, 500, (46, 134, 171), (248, 249, 250))
        
        # Main frame
        main_frame = tk.Frame(self.root, bg=self.colors['white'], relief='flat', bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=400, height=450)
        
        # Add subtle shadow effect
        shadow_frame = tk.Frame(self.root, bg='#000000', height=452, width=402)
        shadow_frame.place(relx=0.5, rely=0.5, anchor='center', x=2, y=2)
        shadow_frame.lower(main_frame)
        
        # Title
        title_label = tk.Label(main_frame, text="Speak Up and Learn", 
                              font=self.fonts['title'], 
                              bg=self.colors['white'], 
                              fg=self.colors['primary'])
        title_label.pack(pady=(30, 10))
        
        # Subtitle
        subtitle_label = tk.Label(main_frame, text="Enhanced Learning Platform", 
                                 font=self.fonts['body'], 
                                 bg=self.colors['white'], 
                                 fg=self.colors['dark'])
        subtitle_label.pack(pady=(0, 30))
        
        # Username field
        username_frame = tk.Frame(main_frame, bg=self.colors['white'])
        username_frame.pack(fill='x', padx=40, pady=(0, 15))
        
        username_label = tk.Label(username_frame, text="Username", 
                                 font=self.fonts['body'], 
                                 bg=self.colors['white'], 
                                 fg=self.colors['dark'])
        username_label.pack(anchor='w')
        
        self.username_entry = tk.Entry(username_frame, font=self.fonts['body'], 
                                      relief='flat', bd=1, highlightthickness=2,
                                      highlightcolor=self.colors['primary'],
                                      highlightbackground='#E0E0E0')
        self.username_entry.pack(fill='x', pady=(5, 0), ipady=8)
        
        # Password field
        password_frame = tk.Frame(main_frame, bg=self.colors['white'])
        password_frame.pack(fill='x', padx=40, pady=(0, 20))
        
        password_label = tk.Label(password_frame, text="Password", 
                                 font=self.fonts['body'], 
                                 bg=self.colors['white'], 
                                 fg=self.colors['dark'])
        password_label.pack(anchor='w')
        
        self.password_entry = tk.Entry(password_frame, font=self.fonts['body'], 
                                      show="*", relief='flat', bd=1, highlightthickness=2,
                                      highlightcolor=self.colors['primary'],
                                      highlightbackground='#E0E0E0')
        self.password_entry.pack(fill='x', pady=(5, 0), ipady=8)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.colors['white'])
        buttons_frame.pack(fill='x', padx=40, pady=(0, 30))
        
        # Login button
        self.login_btn = tk.Button(buttons_frame, text="Login", 
                                  font=self.fonts['subheading'], 
                                  bg=self.colors['success'], 
                                  fg=self.colors['white'],
                                  relief='flat', bd=0, cursor='hand2',
                                  command=self.login)
        self.login_btn.pack(fill='x', pady=(0, 10), ipady=10)
        
        # Sign up button
        self.signup_btn = tk.Button(buttons_frame, text="Create Account", 
                                   font=self.fonts['subheading'], 
                                   bg=self.colors['info'], 
                                   fg=self.colors['white'],
                                   relief='flat', bd=0, cursor='hand2',
                                   command=self.show_signup)
        self.signup_btn.pack(fill='x', ipady=10)
        
        # Add hover effects
        self.add_hover_effects()
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.login())
        
    def add_hover_effects(self):
        """Add hover effects to buttons."""
        def on_enter_login(e):
            self.login_btn.config(bg='#45a049')
            
        def on_leave_login(e):
            self.login_btn.config(bg=self.colors['success'])
            
        def on_enter_signup(e):
            self.signup_btn.config(bg='#1976D2')
            
        def on_leave_signup(e):
            self.signup_btn.config(bg=self.colors['info'])
            
        self.login_btn.bind("<Enter>", on_enter_login)
        self.login_btn.bind("<Leave>", on_leave_login)
        self.signup_btn.bind("<Enter>", on_enter_signup)
        self.signup_btn.bind("<Leave>", on_leave_signup)
        
    def login(self):
        """Handle login process."""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Input Required", "Please enter both username and password.")
            return
            
        if not self.validate_username(username):
            messagebox.showerror("Invalid Username", "Username must be at least 3 characters and contain only letters and numbers.")
            return
            
        hashed_password = self.hash_password(password)
        
        if username in self.users and self.users[username] == hashed_password:
            messagebox.showinfo("Login Successful", f"Welcome back, {username}!")
            self.root.withdraw()
            self.open_dashboard(username)
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
            self.password_entry.delete(0, tk.END)
            
    def show_signup(self):
        """Show signup window."""
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Create Account")
        signup_window.geometry("450x550")
        signup_window.resizable(False, False)
        signup_window.configure(bg=self.colors['light'])
        
        # Center the signup window
        signup_window.update_idletasks()
        x = (signup_window.winfo_screenwidth() // 2) - (450 // 2)
        y = (signup_window.winfo_screenheight() // 2) - (550 // 2)
        signup_window.geometry(f"450x550+{x}+{y}")
        
        # Make signup window modal
        signup_window.transient(self.root)
        signup_window.grab_set()
        
        # Main frame
        main_frame = tk.Frame(signup_window, bg=self.colors['white'], relief='flat', bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=380, height=500)
        
        # Title
        title_label = tk.Label(main_frame, text="Create Account", 
                              font=self.fonts['heading'], 
                              bg=self.colors['white'], 
                              fg=self.colors['primary'])
        title_label.pack(pady=(30, 20))
        
        # Username field
        username_frame = tk.Frame(main_frame, bg=self.colors['white'])
        username_frame.pack(fill='x', padx=30, pady=(0, 15))
        
        username_label = tk.Label(username_frame, text="Username", 
                                 font=self.fonts['body'], 
                                 bg=self.colors['white'], 
                                 fg=self.colors['dark'])
        username_label.pack(anchor='w')
        
        new_username_entry = tk.Entry(username_frame, font=self.fonts['body'], 
                                     relief='flat', bd=1, highlightthickness=2,
                                     highlightcolor=self.colors['primary'],
                                     highlightbackground='#E0E0E0')
        new_username_entry.pack(fill='x', pady=(5, 0), ipady=8)
        
        # Password field
        password_frame = tk.Frame(main_frame, bg=self.colors['white'])
        password_frame.pack(fill='x', padx=30, pady=(0, 15))
        
        password_label = tk.Label(password_frame, text="Password", 
                                 font=self.fonts['body'], 
                                 bg=self.colors['white'], 
                                 fg=self.colors['dark'])
        password_label.pack(anchor='w')
        
        new_password_entry = tk.Entry(password_frame, font=self.fonts['body'], 
                                     show="*", relief='flat', bd=1, highlightthickness=2,
                                     highlightcolor=self.colors['primary'],
                                     highlightbackground='#E0E0E0')
        new_password_entry.pack(fill='x', pady=(5, 0), ipady=8)
        
        # Confirm password field
        confirm_frame = tk.Frame(main_frame, bg=self.colors['white'])
        confirm_frame.pack(fill='x', padx=30, pady=(0, 20))
        
        confirm_label = tk.Label(confirm_frame, text="Confirm Password", 
                                font=self.fonts['body'], 
                                bg=self.colors['white'], 
                                fg=self.colors['dark'])
        confirm_label.pack(anchor='w')
        
        confirm_password_entry = tk.Entry(confirm_frame, font=self.fonts['body'], 
                                         show="*", relief='flat', bd=1, highlightthickness=2,
                                         highlightcolor=self.colors['primary'],
                                         highlightbackground='#E0E0E0')
        confirm_password_entry.pack(fill='x', pady=(5, 0), ipady=8)
        
        # Buttons frame
        buttons_frame = tk.Frame(main_frame, bg=self.colors['white'])
        buttons_frame.pack(fill='x', padx=30, pady=(0, 30))
        
        def create_account():
            username = new_username_entry.get().strip()
            password = new_password_entry.get()
            confirm_password = confirm_password_entry.get()
            
            if not username or not password or not confirm_password:
                messagebox.showwarning("Input Required", "Please fill in all fields.")
                return
                
            if not self.validate_username(username):
                messagebox.showerror("Invalid Username", "Username must be at least 3 characters and contain only letters and numbers.")
                return
                
            if not self.validate_password(password):
                messagebox.showerror("Weak Password", "Password must be at least 6 characters long.")
                return
                
            if password != confirm_password:
                messagebox.showerror("Password Mismatch", "Passwords do not match.")
                return
                
            if username in self.users:
                messagebox.showerror("Username Exists", "Username already exists. Please choose a different one.")
                return
                
            # Create account
            self.users[username] = self.hash_password(password)
            self.save_users()
            messagebox.showinfo("Account Created", "Account created successfully! You can now login.")
            signup_window.destroy()
            
        # Create account button
        create_btn = tk.Button(buttons_frame, text="Create Account", 
                              font=self.fonts['subheading'], 
                              bg=self.colors['success'], 
                              fg=self.colors['white'],
                              relief='flat', bd=0, cursor='hand2',
                              command=create_account)
        create_btn.pack(fill='x', pady=(0, 10), ipady=10)
        
        # Cancel button
        cancel_btn = tk.Button(buttons_frame, text="Cancel", 
                              font=self.fonts['subheading'], 
                              bg=self.colors['danger'], 
                              fg=self.colors['white'],
                              relief='flat', bd=0, cursor='hand2',
                              command=signup_window.destroy)
        cancel_btn.pack(fill='x', ipady=10)
        
        # Add hover effects
        def on_enter_create(e):
            create_btn.config(bg='#45a049')
        def on_leave_create(e):
            create_btn.config(bg=self.colors['success'])
        def on_enter_cancel(e):
            cancel_btn.config(bg='#d32f2f')
        def on_leave_cancel(e):
            cancel_btn.config(bg=self.colors['danger'])
            
        create_btn.bind("<Enter>", on_enter_create)
        create_btn.bind("<Leave>", on_leave_create)
        cancel_btn.bind("<Enter>", on_enter_cancel)
        cancel_btn.bind("<Leave>", on_leave_cancel)
        
    def open_dashboard(self, username):
        """Open the main dashboard."""
        dashboard = tk.Toplevel(self.root)
        dashboard.title(f"Dashboard - Welcome {username}")
        dashboard.geometry("700x600")
        dashboard.resizable(False, False)
        dashboard.configure(bg=self.colors['light'])
        
        # Center the dashboard
        dashboard.update_idletasks()
        x = (dashboard.winfo_screenwidth() // 2) - (700 // 2)
        y = (dashboard.winfo_screenheight() // 2) - (600 // 2)
        dashboard.geometry(f"700x600+{x}+{y}")
        
        # Create canvas for gradient background
        canvas = tk.Canvas(dashboard, width=700, height=600, highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        self.create_gradient_background(canvas, 700, 600, (46, 134, 171), (248, 249, 250))
        
        # Main content frame
        main_frame = tk.Frame(dashboard, bg=self.colors['white'], relief='flat', bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor='center', width=600, height=500)
        
        # Welcome message
        welcome_label = tk.Label(main_frame, text=f"Welcome, {username}!", 
                                font=self.fonts['title'], 
                                bg=self.colors['white'], 
                                fg=self.colors['primary'])
        welcome_label.pack(pady=(30, 20))
        
        # Features frame
        features_frame = tk.Frame(main_frame, bg=self.colors['white'])
        features_frame.pack(fill='both', expand=True, padx=40, pady=(0, 30))
        
        # Feature buttons
        features = [
            ("Record Speech", "🎤", self.colors['info'], self.record_speech),
            ("Upload Audio", "📂", self.colors['warning'], self.upload_audio),
            ("View Progress", "📊", self.colors['secondary'], self.view_progress),
            ("Settings", "⚙️", self.colors['dark'], self.open_settings)
        ]
        
        for i, (text, icon, color, command) in enumerate(features):
            btn = tk.Button(features_frame, text=f"{icon} {text}", 
                          font=self.fonts['subheading'], 
                          bg=color, 
                          fg=self.colors['white'],
                          relief='flat', bd=0, cursor='hand2',
                          command=command)
            btn.pack(fill='x', pady=10, ipady=15)
            
            # Add hover effects
            def make_hover_effect(button, original_color):
                def on_enter(e):
                    button.config(bg=self.darken_color(original_color))
                def on_leave(e):
                    button.config(bg=original_color)
                return on_enter, on_leave
            
            on_enter, on_leave = make_hover_effect(btn, color)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            
        # Logout button
        logout_btn = tk.Button(main_frame, text="Logout", 
                              font=self.fonts['body'], 
                              bg=self.colors['danger'], 
                              fg=self.colors['white'],
                              relief='flat', bd=0, cursor='hand2',
                              command=lambda: self.logout(dashboard))
        logout_btn.pack(pady=(0, 20), ipady=8, padx=40, fill='x')
        
    def darken_color(self, color):
        """Darken a hex color for hover effects."""
        if color.startswith('#'):
            color = color[1:]
        r, g, b = int(color[0:2], 16), int(color[2:4], 16), int(color[4:6], 16)
        r, g, b = max(0, r-30), max(0, g-30), max(0, b-30)
        return f"#{r:02x}{g:02x}{b:02x}"
        
    def record_speech(self):
        """Handle record speech functionality."""
        messagebox.showinfo("Record Speech", "Speech recording feature will be implemented here.")
        
    def upload_audio(self):
        """Handle upload audio functionality."""
        messagebox.showinfo("Upload Audio", "Audio upload feature will be implemented here.")
        
    def view_progress(self):
        """Handle view progress functionality."""
        messagebox.showinfo("View Progress", "Progress tracking feature will be implemented here.")
        
    def open_settings(self):
        """Handle settings functionality."""
        messagebox.showinfo("Settings", "Settings panel will be implemented here.")
        
    def logout(self, dashboard):
        """Handle logout."""
        dashboard.destroy()
        self.root.deiconify()
        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        
    def run(self):
        """Start the application."""
        self.root.mainloop()


if __name__ == "__main__":
    app = SpeakUpApp()
    app.run()
