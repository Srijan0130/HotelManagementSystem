from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        # title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black",
                          fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        # img2= Image.open("C:/Users/gurun/Desktop/.png)
        # img2= img2.resize((100,40),Image.ANTIALIAS)
        # self.photoimg2= ImageTk.PhotoImage(img2)

        # lblimg= Label(self.root,image=self.photoimg2, bd=4,relief=RIDGE)
        # lblimg.place(x=0,y=0, width=230, height=140)

        # labelFrame
        labelframeleft= LabelFrame(self.root,bd=2, relief= RIDGE, text= "Customer Details",  font=("times new roman", 18, "bold"), padx=2)
        labelframeleft.place(x=5,y=50,width=425,height= 490)

        # labels and entries
        # custRef
        lbl_cust_ref=Label(labelframeleft,text="Customer Ref", font= ("times new roman",12,"bold"),padx=2,pady=6)
        lbl_cust_ref.grid(row=0, column=0,sticky=W)
        enty_ref= ttk.Entry(labelframeleft,font= ("times new roman",13,"bold"),width=29)
        enty_ref.grid(row=0,column=1)

        # cust name
        cname= Label(labelframeleft,font=("times new roman",12,"bold"), text="Customer Name:",padx=2,pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft,font=("times new roman", 13, "bold"),width=29)
        txtcname.grid(row=1, column=1)

        # mother name
        lblmname = Label(labelframeleft, font=("times new roman", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(labelframeleft, font=("times new roman", 13, "bold"),width=29)
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, font=("times new roman", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender= ttk.Combobox(labelframeleft, font=("times new roman", 13, "bold"),width=27,state= "read only")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)

        # postcode
        lblPostCode = Label(labelframeleft, font=("times new roman", 12, "bold"), text="Post Code:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, font=("times new roman", 13, "bold"),width=29)
        txtPostCode.grid(row=4, column=1)

        # mobile number
        lblMobile = Label(labelframeleft, font=("times new roman", 12, "bold"), text="Mobile Number:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft, font=("times new roman", 13, "bold"),width=29)
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, font=("times new roman", 12, "bold"), text="E-mail:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, font=("times new roman", 13, "bold"),width=29)
        txtEmail.grid(row=6, column=1)

        # nationality
        lblNationality = Label(labelframeleft, font=("times new roman", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft, font=("times new roman", 13, "bold"), width=27, state="read only")
        combo_Nationality ["value"] = ("Nepali", "American", "African", "Australian", "British")
        combo_Nationality .current(0)
        combo_Nationality .grid(row=7, column=1)


        # idproof type combobox
        lblIdProof = Label(labelframeleft, font=("times new roman", 12, "bold"), text="ID Proof:", padx=2,
                               pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_Id= ttk.Combobox(labelframeleft, font=("times new roman", 13, "bold"), width=27,
                                         state="read only")
        combo_Id["value"] = ("Citizenship", "Passport","Driving License", )
        combo_Id.current(0)
        combo_Id.grid(row=8, column=1)

        # id number
        lblIdNumber = Label(labelframeleft, font=("times new roman", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, font=("times new roman", 13, "bold"),width=29)
        txtIdNumber.grid(row=9, column=1)

        # address
        lblAddress = Label(labelframeleft, font=("times new roman", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, font=("times new roman", 13, "bold"),width=29)
        txtAddress.grid(row=10, column=1)

        # -------------------------
        btn_frame= Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        btnAdd=Button(btn_frame,text="ADD", font=("times new roman", 12, "bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)

        btnUpdate = Button(btn_frame, text="UPDATE", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="DELETE", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="RESET", font=("times new roman", 12, "bold"), bg="black", fg="gold", width=10)
        btnReset.grid(row=0, column=3, padx=1)

        # table frame

        Table_Frame= LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System",font=("times new roman",12,"bold"),padx=2)
        Table_Frame.place(x=435,y=50,width=860,height=490)

        lblSearchBy = Label(Table_Frame, font=("times new roman", 12, "bold"), text="Search By:", bg="red",fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        combo_gender= ttk.Combobox(Table_Frame, font=("times new roman", 13, "bold"),width=24,state= "read only")
        combo_gender["value"]=("Mobile","Ref")
        combo_gender.current(0)
        combo_gender.grid(row=0,column=1)

        txtSearch = ttk.Entry(Table_Frame, font=("times new roman", 13, "bold"), width=29)
        txtSearch.grid(row=0, column=2,padx=2)

        btnSearch = Button(Table_Frame, text="Search", font=("times new roman", 11, "bold"), bg="black", fg="gold", width=10)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", font=("times new roman", 11, "bold"), bg="black", fg="gold", width=10)
        btnShowAll.grid(row=0, column=4, padx=1)

        # show data table

        details_table= Frame(Table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=860,height=350)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table= ttk. Treeview(details_table,column=("ref","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand= scroll_x.set)
        scroll_x.pack(side= BOTTOM,fill=X)
        scroll_x.pack(side=BOTTOM, fill=X)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Poof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")








if __name__ == "__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()