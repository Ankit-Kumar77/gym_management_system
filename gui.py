import customtkinter as ctk
from tkinter import messagebox
from datetime import datetime, timedelta
from database import setup_database
from models import (
    add_member, get_all_members, get_membership_by_name, get_all_membership_plans,
    add_trainer, get_all_trainers,
    mark_attendance, get_attendance_for_member,
    add_payment, get_payments_for_member,
)

# Modern GUI mode
ctk.set_appearance_mode("dark")  # Choices: "light", "dark", "system"
ctk.set_default_color_theme("dark-blue")  # Choices: "blue", "green", "dark-blue"


class GymManagementApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🏋️ Gym & Fitness Center Management System")
        self.geometry("1200x700")

        setup_database()

        # GLOBAL STYLES
        self.FONT_LARGE = ("Arial", 16, "bold")
        self.FONT_MEDIUM = ("Arial", 14)
        self.BUTTON_STYLE = {"height": 45, "corner_radius": 12, "font": self.FONT_LARGE}
        self.ENTRY_STYLE = {"height": 35, "font": self.FONT_MEDIUM}

        # HEADER SECTION
        self.title_frame = ctk.CTkFrame(self, height=70)
        self.title_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(
            self.title_frame,
            text="🏋️ GYM & FITNESS MANAGEMENT SYSTEM",
            font=("Arial", 24, "bold")
        ).pack(pady=10)

        # SIDEBAR
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=12)
        self.sidebar.pack(side="left", fill="y", padx=10, pady=10)

        ctk.CTkLabel(self.sidebar, text="📋 Menu", font=self.FONT_LARGE).pack(pady=10)

        ctk.CTkButton(self.sidebar, text="Members", command=self.open_members_tab,
                      width=180, **self.BUTTON_STYLE).pack(pady=5)
        ctk.CTkButton(self.sidebar, text="Trainers", command=self.open_trainers_tab,
                      width=180, **self.BUTTON_STYLE).pack(pady=5)
        ctk.CTkButton(self.sidebar, text="Attendance", command=self.open_attendance_tab,
                      width=180, **self.BUTTON_STYLE).pack(pady=5)
        ctk.CTkButton(self.sidebar, text="Payments", command=self.open_payments_tab,
                      width=180, **self.BUTTON_STYLE).pack(pady=5)
        ctk.CTkButton(self.sidebar, text="Exit", fg_color="red", command=self.quit,
                      width=180, **self.BUTTON_STYLE).pack(side="bottom", pady=15)

        # Main container
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        self.open_members_tab()

    def clear_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ------------------ MEMBERS TAB ------------------
    def open_members_tab(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="🧍 Member Management", font=("Arial", 22, "bold")).pack(pady=15)

        form = ctk.CTkFrame(self.main_frame)
        form.pack(pady=10, padx=10)

        self.mem_name = ctk.CTkEntry(form, placeholder_text="Full Name", **self.ENTRY_STYLE)
        self.mem_age = ctk.CTkEntry(form, placeholder_text="Age", **self.ENTRY_STYLE)
        self.mem_phone = ctk.CTkEntry(form, placeholder_text="Phone", **self.ENTRY_STYLE)
        self.mem_email = ctk.CTkEntry(form, placeholder_text="Email", **self.ENTRY_STYLE)
        self.mem_plan = ctk.CTkComboBox(form, values=[p[1] for p in get_all_membership_plans()],
                                        font=self.FONT_MEDIUM)
        self.mem_join = ctk.CTkEntry(form, **self.ENTRY_STYLE)
        self.mem_join.insert(0, datetime.now().strftime("%Y-%m-%d"))

        fields = [
            ("Name", self.mem_name),
            ("Age", self.mem_age),
            ("Phone", self.mem_phone),
            ("Email", self.mem_email),
            ("Plan", self.mem_plan),
            ("Join Date", self.mem_join),
        ]

        for i, (label, widget) in enumerate(fields):
            ctk.CTkLabel(form, text=label, font=self.FONT_MEDIUM).grid(row=i, column=0, sticky="w", padx=10, pady=8)
            widget.grid(row=i, column=1, padx=10, pady=8)

        btn_frame = ctk.CTkFrame(self.main_frame)
        btn_frame.pack(pady=10)
        ctk.CTkButton(btn_frame, text="➕ Add Member", command=self.add_member_action, **self.BUTTON_STYLE).grid(row=0, column=0, padx=10)
        ctk.CTkButton(btn_frame, text="📋 Show Members", command=self.show_members, **self.BUTTON_STYLE).grid(row=0, column=1, padx=10)

    def add_member_action(self):
        try:
            name = self.mem_name.get()
            age = int(self.mem_age.get())
            phone = self.mem_phone.get()
            email = self.mem_email.get()
            plan = self.mem_plan.get()
            join = self.mem_join.get()

            duration = get_membership_by_name(plan)[2]
            expiry_date = datetime.strptime(join, "%Y-%m-%d") + timedelta(days=30 * duration)

            add_member(name, age, "N/A", phone, email, join, plan, expiry_date.strftime("%Y-%m-%d"))
            messagebox.showinfo("Success", "Member added successfully!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_members(self):
        members = get_all_members()
        display = "\n".join([f"ID {m[0]} | {m[1]} | Plan: {m[7]}" for m in members])
        messagebox.showinfo("Members", display if display else "No members found")

    # ------------------ TRAINERS TAB ------------------
    def open_trainers_tab(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="🏋 Trainer Management", font=("Arial", 22, "bold")).pack(pady=15)

        form = ctk.CTkFrame(self.main_frame)
        form.pack(pady=10)

        self.tr_name = ctk.CTkEntry(form, placeholder_text="Trainer Name", **self.ENTRY_STYLE)
        self.tr_spec = ctk.CTkEntry(form, placeholder_text="Specialty", **self.ENTRY_STYLE)
        self.tr_phone = ctk.CTkEntry(form, placeholder_text="Phone", **self.ENTRY_STYLE)

        fields = [("Name", self.tr_name), ("Specialty", self.tr_spec), ("Phone", self.tr_phone)]
        for i, (label, widget) in enumerate(fields):
            ctk.CTkLabel(form, text=label, font=self.FONT_MEDIUM).grid(row=i, column=0, padx=10, pady=8)
            widget.grid(row=i, column=1, padx=10, pady=8)

        ctk.CTkButton(self.main_frame, text="➕ Add Trainer", command=self.add_trainer_action, **self.BUTTON_STYLE).pack(pady=15)
        ctk.CTkButton(self.main_frame, text="📋 Show Trainers", command=self.show_trainers, **self.BUTTON_STYLE).pack(pady=5)

    def add_trainer_action(self):
        add_trainer(self.tr_name.get(), self.tr_spec.get(), self.tr_phone.get())
        messagebox.showinfo("Success", "Trainer added successfully!")

    def show_trainers(self):
        trainers = get_all_trainers()
        display = "\n".join([f"ID {t[0]} | {t[1]} ({t[2]})" for t in trainers])
        messagebox.showinfo("Trainers", display if display else "No trainers found")

    # ------------------ ATTENDANCE TAB ------------------
    def open_attendance_tab(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="📆 Attendance Management", font=("Arial", 22, "bold")).pack(pady=15)

        self.att_id = ctk.CTkEntry(self.main_frame, placeholder_text="Member ID", **self.ENTRY_STYLE)
        self.att_id.pack(pady=10)

        ctk.CTkButton(self.main_frame, text="✔ Mark Now", command=self.mark_attendance_action, **self.BUTTON_STYLE).pack(pady=10)
        ctk.CTkButton(self.main_frame, text="📋 Show Records", command=self.show_attendance, **self.BUTTON_STYLE).pack(pady=5)

    def mark_attendance_action(self):
        try:
            member_id = int(self.att_id.get())
            now = datetime.now()
            mark_attendance(member_id, now.strftime("%Y-%m-%d"), now.strftime("%H:%M:%S"))
            messagebox.showinfo("Success", "Attendance recorded!")
        except:
            messagebox.showerror("Error", "Invalid Member ID")

    def show_attendance(self):
        try:
            records = get_attendance_for_member(int(self.att_id.get()))
            display = "\n".join([f"{r[0]} {r[1]}" for r in records])
            messagebox.showinfo("Attendance", display if display else "No records found")
        except:
            messagebox.showerror("Error", "Please enter a valid Member ID")

    # ------------------ PAYMENTS TAB ------------------
    def open_payments_tab(self):
        self.clear_main()
        ctk.CTkLabel(self.main_frame, text="💳 Payment Management", font=("Arial", 22, "bold")).pack(pady=15)

        self.pay_id = ctk.CTkEntry(self.main_frame, placeholder_text="Member ID", **self.ENTRY_STYLE)
        self.pay_amount = ctk.CTkEntry(self.main_frame, placeholder_text="Amount", **self.ENTRY_STYLE)
        self.pay_method = ctk.CTkComboBox(self.main_frame, values=["Cash", "Card", "UPI"], font=self.FONT_MEDIUM)

        fields = [self.pay_id, self.pay_amount, self.pay_method]
        for widget in fields:
            widget.pack(pady=8)

        ctk.CTkButton(self.main_frame, text="💰 Add Payment", command=self.add_payment_action, **self.BUTTON_STYLE).pack(pady=10)
        ctk.CTkButton(self.main_frame, text="📄 Show Payments", command=self.show_payments, **self.BUTTON_STYLE).pack(pady=5)

    def add_payment_action(self):
        add_payment(int(self.pay_id.get()), float(self.pay_amount.get()),
                    datetime.now().strftime("%Y-%m-%d"), self.pay_method.get(), "")
        messagebox.showinfo("Success", "Payment added!")

    def show_payments(self):
        records = get_payments_for_member(int(self.pay_id.get()))
        display = "\n".join([f"₹{r[1]} | {r[2]} | {r[3]}" for r in records])
        messagebox.showinfo("Payments", display if display else "No Payment Records")


if __name__ == "__main__":
    app = GymManagementApp()
    app.mainloop()
