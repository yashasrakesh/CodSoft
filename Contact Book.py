import tkinter as tk
from tkinter import messagebox


class ContactBook:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("400x300")

        self.contacts = {}

        self.create_gui()

    def create_gui(self):
        self.label_name = tk.Label(self.root,font=("Arial",10,"bold"),bg="cyan", text="Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack(pady=10)

        self.label_phone = tk.Label(self.root,font=("Arial",10,"bold"),bg="cyan", text="Phone:")
        self.label_phone.pack(pady=10)
        self.entry_phone = tk.Entry(self.root)
        self.entry_phone.pack(pady=10)

        self.btn_add = tk.Button(self.root, text="Add Contact", command=self.add_contact,font=("Arial",10,"bold"), bg="green", fg="white")
        self.btn_add.pack(pady=10)

        self.btn_view = tk.Button(self.root, text="View Contacts", command=self.view_contacts,font=("Arial",10,"bold"), bg="blue", fg="white")
        self.btn_view.pack(pady=10)

        self.label_search = tk.Label(self.root,font=("Arial",10,"bold"),bg="cyan", text="Search:")
        self.label_search.pack(pady=10)
        self.entry_search = tk.Entry(self.root)
        self.entry_search.pack(pady=10)

        self.btn_search = tk.Button(self.root, text="Search Contact",font=("Arial",10,"bold"), command=self.search_contact, bg="orange",
                                    fg="white")
        self.btn_search.pack(pady=10)

        self.btn_update = tk.Button(self.root, text="Update Contact",font=("Arial",10,"bold"), command=self.update_contact, bg="purple",
                                    fg="white")
        self.btn_update.pack(pady=10)

        self.btn_delete = tk.Button(self.root, text="Delete Contact", font=("Arial",10,"bold"),command=self.delete_contact, bg="red", fg="white")
        self.btn_delete.pack(pady=10)

    def add_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if name and phone:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Please enter both name and phone.")

    def view_contacts(self):
        if self.contacts:
            contacts_str = "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])
            messagebox.showinfo("Contacts", contacts_str)
        else:
            messagebox.showinfo("Contacts", "No contacts to display.")

    def search_contact(self):
        search_name = self.entry_search.get()
        if search_name in self.contacts:
            phone = self.contacts[search_name]
            messagebox.showinfo("Contact Info", f"{search_name}: {phone}")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def update_contact(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if name in self.contacts:
            self.contacts[name] = phone
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")

    def delete_contact(self):
        name = self.entry_name.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showerror("Error", "Contact not found.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBook(root)
    root.mainloop()
