"""
SpeakUp and Learn - Public Speaking Confidence App
A beautiful Tkinter application for building speaking confidence
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime


class SpeakUpApp:
    def __init__(self):
        self.root = tk.Tk()
        self.users = self.load_users()
        self.current_user = None
        self.setup_window()
        self.setup_styles()
        self.create_login_screen()
        
    def setup_window(self):
        """Configure the main window"""
        self.root.title("SpeakUp and Learn - Build Your Speaking Confidence")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f2f5")
        
        # Center the window on screen
        self.root.eval('tk::PlaceWindow . center')
        
    def setup_styles(self):
        """Define application styles and colors"""
        self.colors = {
            'primary': '#6366f1',
            'secondary': '#8b5cf6', 
            'success': '#10b981',
            'warning': '#f59e0b',
            'danger': '#ef4444',
            'info': '#3b82f6',
            'light': '#f8fafc',
            'dark': '#1f2937',
            'white': '#ffffff',
            'gray': '#6b7280'
        }
        
        self.fonts = {
            'title': ('Inter', 24, 'bold'),
            'heading': ('Inter', 18, 'bold'),
            'subheading': ('Inter', 14, 'bold'),
            'body': ('Inter', 12),
            'small': ('Inter', 10)
        }
        
    def create_gradient_background(self, canvas, width, height):
        """Create a beautiful gradient background"""
        # Create gradient from purple to blue
        for i in range(height):
            ratio = i / height
            r = int(99 + (139 - 99) * ratio)  # Purple to blue
            g = int(102 + (69 - 102) * ratio)
            b = int(241 + (19 - 241) * ratio)
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(0, i, width, i, fill=color, width=1)
    
    def create_login_screen(self):
        """Create the main login screen"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Create gradient background
        self.bg_canvas = tk.Canvas(self.root, width=600, height=500, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.create_gradient_background(self.bg_canvas, 600, 500)
        
        # Main container
        main_frame = tk.Frame(self.bg_canvas, bg=self.colors['white'], 
                            relief="flat", bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)
        
        # Add subtle shadow effect
        shadow_frame = tk.Frame(self.bg_canvas, bg="#e5e7eb", width=452, height=402)
        shadow_frame.place(relx=0.5, rely=0.5, anchor="center", x=2, y=2)
        main_frame.lift()
        
        # App logo and title
        logo_frame = tk.Frame(main_frame, bg=self.colors['white'])
        logo_frame.pack(pady=30)
        
        # Microphone icon (using text as icon)
        logo_label = tk.Label(logo_frame, text="🎤", font=('Arial', 48), 
                            bg=self.colors['white'], fg=self.colors['primary'])
        logo_label.pack()
        
        title_label = tk.Label(logo_frame, text="SpeakUp & Learn", 
                              font=self.fonts['title'], 
                              bg=self.colors['white'], fg=self.colors['dark'])
        title_label.pack(pady=(10, 5))
        
        subtitle_label = tk.Label(logo_frame, text="Build Your Speaking Confidence", 
                                font=self.fonts['body'], 
                                bg=self.colors['white'], fg=self.colors['gray'])
        subtitle_label.pack()
        
        # Login form
        form_frame = tk.Frame(main_frame, bg=self.colors['white'])
        form_frame.pack(pady=20, padx=40, fill="x")
        
        # Username field
        username_frame = tk.Frame(form_frame, bg=self.colors['white'])
        username_frame.pack(fill="x", pady=(0, 15))
        
        username_label = tk.Label(username_frame, text="Username", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['white'], fg=self.colors['dark'],
                                anchor="w")
        username_label.pack(fill="x")
        
        self.username_entry = tk.Entry(username_frame, font=self.fonts['body'], 
                                      relief="flat", bd=1, highlightthickness=2,
                                      highlightcolor=self.colors['primary'],
                                      highlightbackground="#e5e7eb")
        self.username_entry.pack(fill="x", pady=(5, 0), ipady=8)
        
        # Password field
        password_frame = tk.Frame(form_frame, bg=self.colors['white'])
        password_frame.pack(fill="x", pady=(0, 20))
        
        password_label = tk.Label(password_frame, text="Password", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['white'], fg=self.colors['dark'],
                                anchor="w")
        password_label.pack(fill="x")
        
        self.password_entry = tk.Entry(password_frame, font=self.fonts['body'], 
                                      show="*", relief="flat", bd=1, highlightthickness=2,
                                      highlightcolor=self.colors['primary'],
                                      highlightbackground="#e5e7eb")
        self.password_entry.pack(fill="x", pady=(5, 0), ipady=8)
        
        # Buttons frame
        buttons_frame = tk.Frame(form_frame, bg=self.colors['white'])
        buttons_frame.pack(fill="x", pady=(10, 0))
        
        # Login button
        self.login_btn = tk.Button(buttons_frame, text="Login", 
                                  font=self.fonts['subheading'], 
                                  bg=self.colors['primary'], fg=self.colors['white'],
                                  relief="flat", bd=0, cursor="hand2",
                                  command=self.handle_login)
        self.login_btn.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.add_hover_effect(self.login_btn, self.colors['primary'], '#4f46e5')
        
        # Sign up button
        self.signup_btn = tk.Button(buttons_frame, text="Sign Up", 
                                   font=self.fonts['subheading'], 
                                   bg=self.colors['white'], fg=self.colors['primary'],
                                   relief="flat", bd=1, cursor="hand2",
                                   command=self.show_signup)
        self.signup_btn.pack(side="left", fill="x", expand=True, padx=(10, 0))
        self.add_hover_effect(self.signup_btn, self.colors['white'], '#f3f4f6')
        
        # Bind Enter key to login
        self.root.bind('<Return>', lambda e: self.handle_login())
        
    def add_hover_effect(self, button, normal_color, hover_color):
        """Add hover effect to buttons"""
        def on_enter(e):
            button.config(bg=hover_color)
        def on_leave(e):
            button.config(bg=normal_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
    def handle_login(self):
        """Handle login logic"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Missing Information", 
                                 "Please enter both username and password.")
            return
        
        # Debug: Show what users are available (remove this in production)
        print(f"Available users: {list(self.users.keys())}")
        print(f"Trying to login: {username}")
        
        if username in self.users and self.users[username] == password:
            self.current_user = username
            messagebox.showinfo("Welcome!", f"Welcome back, {username}!")
            self.create_dashboard()
        else:
            messagebox.showerror("Login Failed", 
                               "Invalid username or password.\n\nTry:\nUsername: Ex\nPassword: 1234")
            
    def show_signup(self):
        """Show signup window"""
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Create Account - SpeakUp & Learn")
        signup_window.geometry("400x450")
        signup_window.resizable(False, False)
        signup_window.configure(bg=self.colors['light'])
        
        # Center the signup window
        signup_window.transient(self.root)
        signup_window.grab_set()
        
        # Main frame
        main_frame = tk.Frame(signup_window, bg=self.colors['white'], 
                             relief="flat", bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=350, height=400)
        
        # Title
        title_label = tk.Label(main_frame, text="Create Your Account", 
                             font=self.fonts['heading'], 
                             bg=self.colors['white'], fg=self.colors['dark'])
        title_label.pack(pady=30)
        
        # Form fields
        form_frame = tk.Frame(main_frame, bg=self.colors['white'])
        form_frame.pack(pady=20, padx=30, fill="x")
        
        # Username
        username_label = tk.Label(form_frame, text="Username", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['white'], fg=self.colors['dark'],
                                anchor="w")
        username_label.pack(fill="x", pady=(0, 5))
        
        new_username = tk.Entry(form_frame, font=self.fonts['body'], 
                               relief="flat", bd=1, highlightthickness=2,
                               highlightcolor=self.colors['primary'])
        new_username.pack(fill="x", pady=(0, 15), ipady=8)
        
        # Password
        password_label = tk.Label(form_frame, text="Password", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['white'], fg=self.colors['dark'],
                                anchor="w")
        password_label.pack(fill="x", pady=(0, 5))
        
        new_password = tk.Entry(form_frame, font=self.fonts['body'], 
                               show="*", relief="flat", bd=1, highlightthickness=2,
                               highlightcolor=self.colors['primary'])
        new_password.pack(fill="x", pady=(0, 20), ipady=8)
        
        # Create account button
        def create_account():
            username = new_username.get().strip()
            password = new_password.get()
            
            if not username or not password:
                messagebox.showwarning("Missing Information", 
                                     "Please enter both username and password.")
                return
                
            if len(password) < 4:
                messagebox.showwarning("Weak Password", 
                                     "Password must be at least 4 characters long.")
                return
                
            if username in self.users:
                messagebox.showerror("Username Exists", 
                                   "This username is already taken.")
                return
                
            self.users[username] = password
            self.save_users()
            messagebox.showinfo("Success!", "Account created successfully!")
            signup_window.destroy()
            
        create_btn = tk.Button(form_frame, text="Create Account", 
                             font=self.fonts['subheading'], 
                             bg=self.colors['success'], fg=self.colors['white'],
                             relief="flat", bd=0, cursor="hand2",
                             command=create_account)
        create_btn.pack(fill="x", pady=(10, 0), ipady=10)
        self.add_hover_effect(create_btn, self.colors['success'], '#059669')
        
    def create_dashboard(self):
        """Create the main dashboard"""
        # Clear login screen
        for widget in self.root.winfo_children():
            widget.destroy()
            
        # Configure window for dashboard
        self.root.title(f"Dashboard - Welcome, {self.current_user}!")
        self.root.geometry("800x600")
        
        # Create gradient background
        self.bg_canvas = tk.Canvas(self.root, width=800, height=600, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.create_gradient_background(self.bg_canvas, 800, 600)
        
        # Header
        header_frame = tk.Frame(self.bg_canvas, bg=self.colors['white'], 
                              relief="flat", bd=0)
        header_frame.place(relx=0.5, rely=0.1, anchor="center", width=700, height=80)
        
        welcome_label = tk.Label(header_frame, text=f"Welcome back, {self.current_user}! 🎉", 
                               font=self.fonts['heading'], 
                               bg=self.colors['white'], fg=self.colors['dark'])
        welcome_label.pack(pady=20)
        
        # Main content area
        content_frame = tk.Frame(self.bg_canvas, bg=self.colors['white'], 
                               relief="flat", bd=0)
        content_frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=400)
        
        # Dashboard title
        dashboard_title = tk.Label(content_frame, text="Your Speaking Journey", 
                                  font=self.fonts['title'], 
                                  bg=self.colors['white'], fg=self.colors['dark'])
        dashboard_title.pack(pady=20)
        
        # Action buttons
        buttons_frame = tk.Frame(content_frame, bg=self.colors['white'])
        buttons_frame.pack(pady=30)
        
        # Practice button
        practice_btn = tk.Button(buttons_frame, text="🎤 Practice Speaking", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['primary'], fg=self.colors['white'],
                                relief="flat", bd=0, cursor="hand2",
                                width=20, height=2)
        practice_btn.pack(pady=10)
        self.add_hover_effect(practice_btn, self.colors['primary'], '#4f46e5')
        
        # Upload button
        upload_btn = tk.Button(buttons_frame, text="📁 Upload Audio", 
                              font=self.fonts['subheading'], 
                              bg=self.colors['info'], fg=self.colors['white'],
                              relief="flat", bd=0, cursor="hand2",
                              width=20, height=2)
        upload_btn.pack(pady=10)
        self.add_hover_effect(upload_btn, self.colors['info'], '#2563eb')
        
        # Progress button
        progress_btn = tk.Button(buttons_frame, text="📊 View Progress", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['secondary'], fg=self.colors['white'],
                                relief="flat", bd=0, cursor="hand2",
                                width=20, height=2)
        progress_btn.pack(pady=10)
        self.add_hover_effect(progress_btn, self.colors['secondary'], '#7c3aed')
        
        # Logout button
        logout_btn = tk.Button(content_frame, text="Logout", 
                             font=self.fonts['body'], 
                             bg=self.colors['gray'], fg=self.colors['white'],
                             relief="flat", bd=0, cursor="hand2",
                             command=self.logout)
        logout_btn.pack(pady=20)
        self.add_hover_effect(logout_btn, self.colors['gray'], '#4b5563')
        
    def logout(self):
        """Handle logout"""
        self.current_user = None
        self.create_login_screen()
        
    def load_users(self):
        """Load users from file"""
        # Always start with default users
        users = {"Ex": "1234"}
        
        try:
            if os.path.exists('users.json'):
                with open('users.json', 'r') as f:
                    file_users = json.load(f)
                    # Merge file users with default users
                    users.update(file_users)
                    print(f"Loaded users from file: {file_users}")
        except Exception as e:
            print(f"Error loading users.json: {e}")
            pass
        
        print(f"Final users dictionary: {users}")
        return users
        
    def save_users(self):
        """Save users to file"""
        try:
            with open('users.json', 'w') as f:
                json.dump(self.users, f)
        except:
            pass
            
    def run(self):
        """Start the application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = SpeakUpApp()
    app.run()
