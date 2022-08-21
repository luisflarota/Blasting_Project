#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import math
import tkinter
from tkinter import ttk

import numpy as np
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

import backend

# Instantiate the tkinker gui
app = tkinter.Tk()
app.wm_title("Blasting Software")
app.geometry('1200x600')
database = backend.Dabase("blasting_db.db")
#These ones are inputs for the explosive
app_parent = ttk.Notebook(app)
app_1 = ttk.Frame(master = app_parent)
app_2 = ttk.Frame(master = app_parent)
app_3 = ttk.Frame(master = app_parent)
app_parent.add(app_1, text = "Estimation")
app_parent.add(app_2, text = "Databases")
app_parent.add(app_3, text = "Rock Factor Parameters")

#APP1_BEGINNING
explosive_label = tkinter.Label(app_1, text = "Explosive ", font='Helvetica 14 bold')
explosive_label.grid(row = 0, column = 0)

label_explosive_bottom = tkinter.Label(app_1, text = "Explosive on the Bottom", font = "Helvetica 9 bold")
label_explosive_bottom.grid(row = 1, column = 0)

def insert_density_we(event = None):
    if event:
        density_explosive_bottom.delete(0, tkinter.END)
        density_explosive_bottom.insert(tkinter.END, database.show_density(cbtext.get()))
        ws_explosive_bottom.delete(0, tkinter.END)
        ws_explosive_bottom.insert(tkinter.END, database.show_we(cbtext.get()))

cbtext = tkinter.StringVar()
cbox_explosive_bottom = ttk.Combobox(app_1, value = database.names_columns(), width = 18, textvariable = cbtext)
cbox_explosive_bottom.bind('<<ComboboxSelected>>', insert_density_we)
cbox_explosive_bottom.grid(row= 1, column = 1)


label_dens_explosive_bottom = tkinter.Label(app_1, text = "Density - Explos. Bottom")
label_dens_explosive_bottom.grid(row = 2, column = 0)

text_dens = tkinter.DoubleVar()
density_explosive_bottom = tkinter.Entry(app_1, width = 21, textvariable = text_dens)
density_explosive_bottom.grid(row = 2, column = 1)

label_ws_explosive_bottom = tkinter.Label(app_1, text = "Weight S.- Explos. Bottom")
label_ws_explosive_bottom.grid(row = 3, column = 0)
textweb = tkinter.DoubleVar()
ws_explosive_bottom = tkinter.Entry(app_1, textvariable = textweb, width = 21)
ws_explosive_bottom.grid(row = 3, column = 1)

label_hf_explosive_bottom = tkinter.Label(app_1, text = "Height explosive bottom", bg = 'yellow')
label_hf_explosive_bottom.grid(row = 4, column = 0)
texthf = tkinter.DoubleVar()
hf_explosive_bottom = tkinter.Entry(app_1, textvariable = texthf, width = 21)
hf_explosive_bottom.grid(row = 4, column = 1)

label_explosive_column = tkinter.Label(app_1, text = "Explosive on the Column", font = "Helvetica 9 bold")
label_explosive_column.grid(row = 5, column = 0)


def insert_density_we_(event = None):
    if event:
        density_explosive_column.delete(0, tkinter.END)
        density_explosive_column.insert(tkinter.END, database.show_density(cbtext_.get()))
        ws_explosive_column.delete(0, tkinter.END)
        ws_explosive_column.insert(tkinter.END, database.show_we(cbtext_.get()))


cbtext_ = tkinter.StringVar()
cbox_explosive_column = ttk.Combobox(app_1, width = 18, value = database.names_columns(), textvariable = cbtext_)
cbox_explosive_column.bind('<<ComboboxSelected>>', insert_density_we_)
cbox_explosive_column.grid(row= 5, column = 1)
label_dens_explosive_column = tkinter.Label(app_1, text = "Density - Explos. Column")
label_dens_explosive_column.grid(row = 6, column = 0)

textdec = tkinter.DoubleVar()
density_explosive_column = tkinter.Entry(app_1, textvariable = textdec, width = 21)
density_explosive_column.grid(row = 6, column = 1)

label_ws_explosive_column = tkinter.Label(app_1, text = "Weight S.- Explos. Column")
label_ws_explosive_column.grid(row = 7, column = 0)
textwec = tkinter.DoubleVar()
ws_explosive_column = tkinter.Entry(app_1, textvariable = textwec, width = 21)
ws_explosive_column.grid(row = 7, column = 1)

#Design Inputs
design_label = tkinter.Label(app_1, text = "Design", font='Helvetica 14 bold')
design_label.grid(row = 8, column = 0)
hole_diameter = tkinter.Label(app_1, text = "Hole Diameter (in.)")
hole_diameter.grid(row = 9, column = 0)

hole_diameter_text = tkinter.DoubleVar()
cbox_hole_diameter = ttk.Combobox(app_1, width = 18, values = [10, 11, 12, 13, 14], textvariable = hole_diameter_text)
cbox_hole_diameter.grid(row= 9, column = 1)

bench_label = tkinter.Label(app_1, text = "Bench height (m.)")
bench_label.grid(row = 10, column = 0)
textbh = tkinter.DoubleVar()
bench_height_input = tkinter.Entry(app_1, textvariable = textbh, width = 21)
bench_height_input.grid(row = 10, column = 1)

burden = tkinter.Label(app_1, text = "Burden (m.)")
burden.grid(row = 11, column = 0)
textbi = tkinter.DoubleVar()
burden_input = tkinter.Entry(app_1, textvariable = textbi, width = 21)
burden_input.grid(row = 11, column = 1)

spacing = tkinter.Label(app_1, text = "Spacing (m.)")
spacing.grid(row = 12, column = 0)
textsi = tkinter.DoubleVar()
spacing_input = tkinter.Entry(app_1, textvariable = textsi, width = 21)
spacing_input.grid(row = 12, column = 1)

subdrill = tkinter.Label(app_1, text = "Sub-drilling (m.)")
subdrill.grid(row = 13, column = 0)
textsd = tkinter.DoubleVar()
subdrill_input = tkinter.Entry(app_1, textvariable = textsd, width = 21)
subdrill_input.grid(row = 13, column = 1)

stemm = tkinter.Label(app_1, text = "Stemming (m.)")
stemm.grid(row = 14, column = 0)
textstem = tkinter.DoubleVar()
stemming_input = tkinter.Entry(app_1, textvariable = textstem, width = 21)
stemming_input.grid(row = 14, column = 1)

drill_des = tkinter.Label(app_1, text = "Drilling desviation (m.)")
drill_des.grid(row = 15, column = 0)
textdd = tkinter.DoubleVar()
drill_des_input = tkinter.Entry(app_1, textvariable = textdd, width = 21)
drill_des_input.grid(row = 15, column = 1)

pattern = tkinter.Label(app_1, text = "Pattern")
pattern.grid(row = 16, column = 0)
pattern_text = tkinter.StringVar()
cbox_pattern = ttk.Combobox(app_1, width = 18, values = ['Staggered', 'Squared'], textvariable = pattern_text)
cbox_pattern.grid(row= 16, column = 1)

#Rock properties
rock_label = tkinter.Label(app_1, text = "Rock Properties", font='Helvetica 14 bold')
rock_label.grid(row = 17, column = 0)


#function to make parameters window for rock factor

    #switch frames???
def change_to_3():
    app_parent.select(app_3)

rock_factor = tkinter.Label(app_1, text = "Rock Factor")
rock_factor.grid(row = 18, column = 0)
textrf = tkinter.DoubleVar()
rock_factor_input = tkinter.Entry(app_1, textvariable = textrf, width = 21)
rock_factor_input.grid(row = 18, column = 1)
rock_factor_button = tkinter.Button(app_1, text = 'Parameters?', command = change_to_3)
rock_factor_button.grid(row = 18, column = 3)

rock_density = tkinter.Label(app_1, text = "Rock Density (kg/m3)")
rock_density.grid(row = 19, column = 0)
textrd = tkinter.DoubleVar()
rock_density_input = tkinter.Entry(app_1, textvariable = textrd, width = 21)
rock_density_input.grid(row = 19, column = 1)


#Setting more variables for KR
#Explosive column height


#Solving the problem
def solve_kuz_ram():
    h_column = float(textbh.get()) - float(textstem.get()) + float(textsd.get())
    # Tons/hole
    ton_hole = float(textbi.get()) * float(textsi.get()) * float(textbh.get()) * float(textrd.get())
    # Height of explosive that is in the column (this is different dfor the bottom)
    h_explosiv_column = h_column - float(texthf.get())
    # Q for bottom as well for column
    # Texthf is height of explosive at the bottom
    bottom_charge = 0.5067 * float(
        text_dens.get()
        ) * (float(hole_diameter_text.get()) **2) * float(texthf.get())
    column_charge = 0.5067 * float(
        textdec.get()
        ) * (float(hole_diameter_text.get()) **2) * h_explosiv_column
    subdrilling_charge = 0.5067 * text_dens.get() * (
        float(hole_diameter_text.get()) **2
        ) * float(textsd.get())
    # total Q, stemming is included
    total_charge = bottom_charge + column_charge
    # total Q, stemming is not included
    total_charge_nostem = total_charge - subdrilling_charge
    # WS of the whole hole
    total_weight_strenght = 100*(
        float(textweb.get()) * (bottom_charge - subdrilling_charge) + float(textwec.get()) * column_charge
        )/(bottom_charge + column_charge - subdrilling_charge)
    # Power factor, which is in gr/ton
    power_factor = total_charge * 1000 / ton_hole
    # 50 prob which is in mm
    # textrf is rockfactor
    # textrd is rockdensity
    d_50 = float(textrf.get()) * 10 * (
        (ton_hole /(float(textrd.get()) * total_charge)
        )**0.8
        ) * (total_charge **(1/6)) * ((115/total_weight_strenght) ** 0.633)
    # Uniformity index
    if pattern_text.get() == "Staggered":
        pattern_value = 1.1
    else:
        pattern_value = 1
    uniform_index = pattern_value * (
        (
            h_column - float(textsd.get())
        )/float(textbh.get()) * (
            2.2 - 14 * float(textbi.get())/(float(hole_diameter_text.get()) * 25.4)
            ) *(
                (1 + float(textsi.get())/float(textbi.get()))/2
                ) ** 0.5 * (1 - (float(textdd.get())/float(textbi.get()))) * (
                    abs(bottom_charge - column_charge) / (bottom_charge+column_charge) + 0.1
                    ) ** 0.1
                    )
    uniform_index = round(uniform_index, 2)
    #Particular size
    particular_size = d_50 / (0.693 ** (1/uniform_index))
    particular_size = round(particular_size, 0)
    data = pd.DataFrame(columns = ['Size_Particle'])
    for i in range(10, 101, 10):
        if i == 100:
            i = 99.5
        #PLEASE LOOK AT THESE VALUES.... THEY ARE ABOVE 10m.!!!!!!!!
        data.loc[i] = math.exp((np.log(np.log(1/ (1- i/100))) + uniform_index * np.log(particular_size/10)) / uniform_index)
        
    fig = Figure(figsize = (7,5))
    ax = fig.add_subplot(111)
    ax.plot(data['Size_Particle'], data.index)
    ax.annotate("P80 is: {} cm".format(round(data.loc[80]['Size_Particle'],2)), xy = (data.loc[80],80), arrowprops = dict(facecolor = 'black'))
    ax.annotate("Q. total: {} kg".format(round(total_charge,2)), xy = (1,60))
    ax.annotate("Q. bottom: {} kg".format(round(bottom_charge,2)), xy = (1,55))
    ax.annotate("Q. column: {} kg".format(round(column_charge,2)), xy = (1,50))
    ax.annotate("PF: {} gr/ton".format(round(power_factor,2)), xy = (1,30))
    ax.set_title("Fragmentation Curve")
    ax.set_xlabel("Size (cm)")
    ax.set_ylabel("Passing Probability")
    
    canvas = FigureCanvasTkAgg(fig, master = app_1)
    canvas.get_tk_widget().grid(rowspan = 30, column = 4, row = 0)
    canvas.draw()




button_solve = tkinter.Button(app_1, text = "Get Kuz Ram", width = 20, command = solve_kuz_ram)
button_solve.grid(row = 20, columnspan = 2)

#APP2_BEGINNING
app2_title = tkinter.Label(app_2, text = "Explosives Database", font = "Helvetica 14 bold")
app2_title.grid(row = 0, column = 1)

name_explosive = tkinter.Label(app_2, text = "Name: ")
name_explosive.grid(row = 1, column = 0)
n_explos = tkinter.StringVar()
name_exp = tkinter.Entry(app_2, textvariable = n_explos, width = 21)
name_exp.grid(row = 1, column =1)

den_explosive = tkinter.Label(app_2, text = "Density (gr./cm3): ")
den_explosive.grid(row = 2, column = 0)
den_explos = tkinter.DoubleVar()
den_exp = tkinter.Entry(app_2, textvariable = den_explos, width = 21)
den_exp.grid(row = 2, column =1)

vod_explosive = tkinter.Label(app_2, text = "VOD (m/s):")
vod_explosive.grid(row = 3, column = 0)
vod_explos = tkinter.DoubleVar()
vod_exp = tkinter.Entry(app_2, textvariable = vod_explos, width = 21)
vod_exp.grid(row = 3, column =1)

pd_explosive = tkinter.Label(app_2, text = "Det. Pressure (kbar.): ")
pd_explosive.grid(row = 4, column = 0)
pd_explos = tkinter.DoubleVar()
pd_exp = tkinter.Entry(app_2, textvariable = pd_explos, width = 21)
pd_exp.grid(row = 4, column =1)

ene_explosive = tkinter.Label(app_2, text = "Energy (kcal/kg.): ")
ene_explosive.grid(row = 5, column = 0)
ene_explos = tkinter.DoubleVar()
ene_exp = tkinter.Entry(app_2, textvariable = ene_explos, width = 21)
ene_exp.grid(row = 5, column =1)

wes_explosive = tkinter.Label(app_2, text = "Weigth Strength: ")
wes_explosive.grid(row = 6, column = 0)
wes_explos = tkinter.DoubleVar()
wes_exp = tkinter.Entry(app_2, textvariable = wes_explos, width = 21)
wes_exp.grid(row = 6, column =1)

def showexplosives():
    list_explosive.delete(0, tkinter.END)
    for row in database.view():
        list_explosive.insert(tkinter.END, row)
    return list_explosive, rolliton

def addexplosive():
    database.insert(n_explos.get(), den_explos.get(), vod_explos.get(), pd_explos.get(), ene_explos.get(), wes_explos.get())
    list_explosive.delete(0, tkinter.END)
    list_explosive.insert(tkinter.END,(n_explos.get(), den_explos.get(), vod_explos.get(), pd_explos.get(), ene_explos.get(), wes_explos.get()))

def get_selected_row(event):
    try:
        global selected_tuple
        index = list_explosive.curselection()[0]
        selected_tuple = list_explosive.get(index)
        name_exp.delete(0, tkinter.END)
        name_exp.insert(tkinter.END, selected_tuple[1])
        den_exp.delete(0, tkinter.END)
        den_exp.insert(tkinter.END, selected_tuple[2])
        vod_exp.delete(0, tkinter.END)
        vod_exp.insert(tkinter.END, selected_tuple[3])
        pd_exp.delete(0, tkinter.END)
        pd_exp.insert(tkinter.END, selected_tuple[4])
        ene_exp.delete(0, tkinter.END)
        ene_exp.insert(tkinter.END, selected_tuple[5])        
        wes_exp.delete(0, tkinter.END)
        wes_exp.insert(tkinter.END, selected_tuple[6])
    except IndexError:
        pass

def delete():
    database.delete(selected_tuple[0])

def update():
    database.update(selected_tuple[0], n_explos.get(), den_explos.get(), vod_explos.get(), pd_explos.get(), ene_explos.get(), wes_explos.get())
list_explosive = tkinter.Listbox(app_2, height = 30, width = 75)
list_explosive.grid(row = 10, columnspan = 3)
rolliton = tkinter.Scrollbar(app_2)
rolliton.grid(row = 10, column = 4, rowspan = 2)
list_explosive.configure(yscrollcommand = rolliton.set)
rolliton.configure(command = list_explosive.yview)
list_explosive.bind('<<ListboxSelect>>', get_selected_row)

add_explosive = tkinter.Button(app_2, text = "Add explosive data", width = 17, command = addexplosive)
add_explosive.grid(row = 1, columnspan = 2, column = 4)

view_explosive = tkinter.Button(app_2, text = "View explosives", bg = "white", width = 17, command = showexplosives)
view_explosive.grid(row = 2, column =4)

delete_explosive = tkinter.Button(app_2, text = "Delete", bg = "white", width = 17, command = delete)
delete_explosive.grid(row = 3, column =4)

update_explosive = tkinter.Button(app_2, text = "Update", bg = "white", width = 17, command = update)
update_explosive.grid(row = 4, column =4)

#APP3 BEGINNING


app_parent.pack(expand = 1, fill = 'both')
app.mainloop()
