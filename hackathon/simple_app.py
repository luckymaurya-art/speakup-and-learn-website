#!/usr/bin/env python3
"""
SpeakUp and Learn App - Enhanced Version
A beautiful and secure Tkinter application for building speaking confidence
"""

import tkinter as tk
from tkinter import messagebox, ttk
import hashlib
import json
import os
import re
from datetime import datetime

class SimpleSpeakUpApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SpeakUp and Learn - Enhanced Version")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f2f5")
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
        
        # Enhanced user database with hashed passwords
        self.users = self.load_users()
        self.current_user = None
        
        # Enhanced styling
        self.setup_styles()
        self.create_login_screen()
    
    def setup_styles(self):
        """Setup enhanced styling and colors"""
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
    
    def hash_password(self, password):
        """Hash password using SHA-256"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def validate_username(self, username):
        """Validate username format"""
        if len(username) < 3:
            messagebox.showerror("Error", "Username must be at least 3 characters long.")
            return False
        if not re.match(r'^[a-zA-Z0-9_]+$', username):
            messagebox.showerror("Error", "Username can only contain letters, numbers, and underscores.")
            return False
        return True
    
    def validate_password(self, password):
        """Validate password strength"""
        if len(password) < 6:
            messagebox.showerror("Error", "Password must be at least 6 characters long.")
            return False
        if not re.search(r'[A-Za-z]', password):
            messagebox.showerror("Error", "Password must contain at least one letter.")
            return False
        if not re.search(r'\d', password):
            messagebox.showerror("Error", "Password must contain at least one number.")
            return False
        return True
    
    def load_users(self):
        """Load users from file with fallback to default"""
        default_users = {"Ex": "1234", "admin": "password"}
        
        if os.path.exists('users.json'):
            try:
                with open('users.json', 'r') as f:
                    file_users = json.load(f)
                    # If file has hashed passwords, use them; otherwise hash the plain text
                    for user, pwd in file_users.items():
                        if len(pwd) == 64:  # SHA-256 hash length
                            default_users[user] = pwd
                        else:
                            default_users[user] = self.hash_password(pwd)
            except Exception as e:
                print(f"Error loading users: {e}")
        
        return default_users
    
    def save_users(self):
        """Save users to file"""
        try:
            with open('users.json', 'w') as f:
                json.dump(self.users, f, indent=2)
        except Exception as e:
            print(f"Error saving users: {e}")
    
    def create_gradient_background(self, canvas, width, height):
        """Create a beautiful gradient background"""
        for i in range(height):
            ratio = i / height
            r = int(99 + (139 - 99) * ratio)  # Purple to blue
            g = int(102 + (69 - 102) * ratio)
            b = int(241 + (19 - 241) * ratio)
            color = f"#{r:02x}{g:02x}{b:02x}"
            canvas.create_line(0, i, width, i, fill=color, width=1)
    
    def add_hover_effect(self, button, normal_color, hover_color):
        """Add hover effect to buttons"""
        def on_enter(e):
            button.config(bg=hover_color)
        def on_leave(e):
            button.config(bg=normal_color)
        
        button.bind("<Enter>", on_enter)
        button.bind("<Leave>", on_leave)
        
    def create_login_screen(self):
        """Create enhanced login screen with gradient background"""
        # Clear existing widgets
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Create gradient background
        self.bg_canvas = tk.Canvas(self.root, width=600, height=500, highlightthickness=0)
        self.bg_canvas.pack(fill="both", expand=True)
        self.create_gradient_background(self.bg_canvas, 600, 500)
        
        # Main container with shadow effect
        main_frame = tk.Frame(self.bg_canvas, bg=self.colors['white'], 
                            relief="flat", bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=450, height=400)
        
        # Add subtle shadow
        shadow_frame = tk.Frame(self.bg_canvas, bg="#e5e7eb", width=452, height=402)
        shadow_frame.place(relx=0.5, rely=0.5, anchor="center", x=2, y=2)
        main_frame.lift()
        
        # Logo and title
        logo_frame = tk.Frame(main_frame, bg=self.colors['white'])
        logo_frame.pack(pady=30)
        
        # Microphone icon
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
        
        # Remember me checkbox
        self.remember_var = tk.BooleanVar()
        remember_check = tk.Checkbutton(form_frame, text="Remember me", 
                                      variable=self.remember_var,
                                      font=self.fonts['small'],
                                      bg=self.colors['white'])
        remember_check.pack(pady=5)
        
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
        
        # Instructions
        instructions = tk.Label(main_frame, 
                               text="Try: Username='Ex', Password='1234'", 
                               font=self.fonts['small'], 
                               bg=self.colors['white'], fg=self.colors['gray'])
        instructions.pack(pady=10)
        
        # Bind Enter key
        self.root.bind('<Return>', lambda e: self.handle_login())
        
        # Focus on username entry
        self.username_entry.focus()
        
    def handle_login(self):
        """Handle enhanced login with security"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showwarning("Missing Information", 
                                 "Please enter both username and password.")
            return
        
        # Check if user exists and password matches (handles both hashed and plain text)
        if username in self.users:
            stored_password = self.users[username]
            
            # If stored password is hashed (64 chars), compare hashes
            if len(stored_password) == 64:
                if stored_password == self.hash_password(password):
                    self.current_user = username
                    messagebox.showinfo("Welcome!", f"Welcome back, {username}!")
                    self.create_dashboard()
                    return
            # If stored password is plain text, compare directly
            elif stored_password == password:
                # Upgrade to hashed password
                self.users[username] = self.hash_password(password)
                self.save_users()
                self.current_user = username
                messagebox.showinfo("Welcome!", f"Welcome back, {username}!")
                self.create_dashboard()
                return
        
        # Login failed
        messagebox.showerror("Login Failed", 
                           "Invalid username or password.\n\nTry:\nUsername: Ex\nPassword: 1234")
        self.password_entry.delete(0, tk.END)
            
    def show_signup(self):
        """Show enhanced signup window"""
        signup_window = tk.Toplevel(self.root)
        signup_window.title("Create Account - SpeakUp & Learn")
        signup_window.geometry("450x500")
        signup_window.resizable(False, False)
        signup_window.configure(bg=self.colors['light'])
        
        # Center the signup window
        signup_window.transient(self.root)
        signup_window.grab_set()
        
        # Create gradient background
        bg_canvas = tk.Canvas(signup_window, width=450, height=500, highlightthickness=0)
        bg_canvas.pack(fill="both", expand=True)
        self.create_gradient_background(bg_canvas, 450, 500)
        
        # Main frame
        main_frame = tk.Frame(bg_canvas, bg=self.colors['white'], 
                             relief="flat", bd=0)
        main_frame.place(relx=0.5, rely=0.5, anchor="center", width=380, height=450)
        
        # Add shadow
        shadow_frame = tk.Frame(bg_canvas, bg="#e5e7eb", width=382, height=452)
        shadow_frame.place(relx=0.5, rely=0.5, anchor="center", x=2, y=2)
        main_frame.lift()
        
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
        new_password.pack(fill="x", pady=(0, 10), ipady=8)
        
        # Password strength indicator
        strength_label = tk.Label(form_frame, text="", 
                                font=self.fonts['small'],
                                bg=self.colors['white'])
        strength_label.pack(pady=5)
        
        def check_password_strength():
            password = new_password.get()
            if len(password) < 6:
                strength_label.config(text="Password too short", fg="red")
            elif len(password) < 8:
                strength_label.config(text="Password strength: Weak", fg="orange")
            elif len(password) < 12:
                strength_label.config(text="Password strength: Medium", fg="blue")
            else:
                strength_label.config(text="Password strength: Strong", fg="green")
        
        new_password.bind('<KeyRelease>', lambda e: check_password_strength())
        
        # Create account function
        def create_account():
            username = new_username.get().strip()
            password = new_password.get()
            
            if not username or not password:
                messagebox.showwarning("Missing Information", 
                                     "Please enter both username and password.")
                return
            
            if not self.validate_username(username):
                return
                
            if not self.validate_password(password):
                return
                
            if username in self.users:
                messagebox.showerror("Username Exists", 
                                   "This username is already taken.")
                return
                
            # Hash the password before storing
            self.users[username] = self.hash_password(password)
            self.save_users()
            messagebox.showinfo("Success!", "Account created successfully!")
            signup_window.destroy()
            
        # Create account button
        create_btn = tk.Button(form_frame, text="Create Account", 
                             font=self.fonts['subheading'], 
                             bg=self.colors['success'], fg=self.colors['white'],
                             relief="flat", bd=0, cursor="hand2",
                             command=create_account)
        create_btn.pack(fill="x", pady=(20, 0), ipady=10)
        self.add_hover_effect(create_btn, self.colors['success'], '#059669')
        
        # Focus on username entry
        new_username.focus()
        
    def create_dashboard(self):
        """Create enhanced dashboard"""
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
                                width=20, height=2, command=self.practice_speaking)
        practice_btn.pack(pady=10)
        self.add_hover_effect(practice_btn, self.colors['primary'], '#4f46e5')
        
        # Upload button
        upload_btn = tk.Button(buttons_frame, text="📁 Upload Audio", 
                              font=self.fonts['subheading'], 
                              bg=self.colors['info'], fg=self.colors['white'],
                              relief="flat", bd=0, cursor="hand2",
                              width=20, height=2, command=self.upload_audio)
        upload_btn.pack(pady=10)
        self.add_hover_effect(upload_btn, self.colors['info'], '#2563eb')
        
        # Progress button
        progress_btn = tk.Button(buttons_frame, text="📊 View Progress", 
                                font=self.fonts['subheading'], 
                                bg=self.colors['secondary'], fg=self.colors['white'],
                                relief="flat", bd=0, cursor="hand2",
                                width=20, height=2, command=self.view_progress)
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
    
    def practice_speaking(self):
        """Handle practice speaking functionality"""
        messagebox.showinfo("Practice Speaking", 
                          "🎤 Practice speaking functionality would be implemented here.\n\n"
                          "This could include:\n"
                          "• Voice recording\n"
                          "• Speech analysis\n"
                          "• Confidence building exercises")
    
    def upload_audio(self):
        """Handle upload audio functionality"""
        messagebox.showinfo("Upload Audio", 
                          "📁 Audio upload functionality would be implemented here.\n\n"
                          "This could include:\n"
                          "• File selection dialog\n"
                          "• Audio format validation\n"
                          "• Processing and analysis")
    
    def view_progress(self):
        """Handle view progress functionality"""
        messagebox.showinfo("View Progress", 
                          "📊 Progress tracking functionality would be implemented here.\n\n"
                          "This could include:\n"
                          "• Speaking confidence metrics\n"
                          "• Practice session history\n"
                          "• Improvement over time")
        
    def logout(self):
        """Handle logout"""
        self.current_user = None
        # Reset window size and title
        self.root.title("SpeakUp and Learn - Enhanced Version")
        self.root.geometry("600x500")
        self.create_login_screen()
        
    def run(self):
        """Start the enhanced app"""
        self.root.mainloop()

if __name__ == "__main__":
    print("Starting Enhanced SpeakUp and Learn App...")
    app = SimpleSpeakUpApp()
    app.run()
