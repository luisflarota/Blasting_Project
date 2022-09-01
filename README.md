## Building a Graphic User Interface for Blasting purposes - KUZ Ram Curve

--- 

<h2> Content </h2>

[1. The Problem](#s2) <br>
[2. The Solution ](#s3) <br>
&nbsp;&nbsp;&nbsp;&nbsp;[2.1 Building the application](#s4) <br>
[3. Application's features](#s5) <br>
[4. Future Work Ideas](#s6) <br>
[5. Code Source](#s7) <br>

----

<h2 id = "s2"> 1. The Problem </h2>

When analyzing a blasting design in an open pit mining operation, we usually find explosives data saved in excel sheets that needed to be copied and pasted in a report format and then looked up.
![db](https://user-images.githubusercontent.com/64980133/185801539-5027e567-62aa-4c26-8f20-7bea0f10fc92.png)

This raw data is often used for blasting engineers to predict how fragmented the rock will be after blasted - this is based on computing some equations, i.e., Kuz Ram model. It is most likely to find this analysis in Excel files such as the following, where engineers will need to look up the explosives properties in another table and then find the best blasting parameters.
![db2](https://user-images.githubusercontent.com/64980133/185801542-85b9a348-629a-4d86-9d94-572a02dfd3c6.png)

So<ins> how can we keep the source data for a blasting design and also their corresponding computations?</ins>

----

<h2 id = "s3"> 2. The Solution </h2>

Instead of keep using Excel files to store and perform computations, we thought about building a desktop graphical user interface (GUI) that could handle the two main processes of getting a Kuz-Ram curve (also see picture below):
*  Storing explosives data effectively
*  Compute variables dynamically based on explosives data

![blast1](https://user-images.githubusercontent.com/64980133/185801549-fb2ab967-c677-4de5-950f-7ec0427104e2.svg)

<h3 id = "s4"> 2.1 Building the application </h3>

The GUI was built with [Tkinter](https://docs.python.org/3/library/tkinter.html), which offers multiple features for desktop applications.

1- Inserting, viewing, updating and deleting data in a database's table

Once we got a SQLite database (located in the [Github_repo](https://github.com/luisflarota/Blasting_Project){:target="\_blank"}), we could perform multiple operations:

~~~python
class Dabase:
    def __init__(self, db):
        """
        Connects to the dbase.
        Args:
            db (.db file): path of the db file
        """
        # Connect to db 
        self.conn = sqlite3.connect(db, check_same_thread= False)
        # Allow to execute statements
        self.c = self.conn.cursor()
        # Make sure that the table for explosives exist
        self.c.execute(
            "CREATE TABLE IF NOT EXISTS explosives \
                (id INTEGER PRIMARY KEY, name FIXED,\
                density FLOAT, VOD INTEGER,\
                     Deton_Pressure FLOAT, Energy FLOAT, Weigth_S FLOAT)"
                     )

    def insert(self, name, density, vod, detpre, energy, wes):
        """
        Insert properties for a new explosive. This comes from some input boxes
        Args:
            name (str)        : Name of the explosive
            density(float)    : Density of the ..
            vod   (float)     : Velocity of detonation
            detpre (float)    : Detonation Pressure
            energy (float)    : Energy
            wes (float)       : Weigh pressure compared to ANFO
        """
        # First one for id
        self.c.execute(
            "INSERT INTO explosives VALUES (NULL, ?, ?, ?, ?, ?, ?)", 
            (name, density, vod, detpre, energy, wes)
            )
        self.conn.commit()

    def view(self):
        """ Show row data from explosives table in the GUI"""
        self.c.execute(
            "SELECT * from explosives"
            )
        # Show them in a list - this is the best way
        # to show data in Tkinter TODO: might be another though
        rows = self.c.fetchall()
        return rows   

    def update(self, id, name, density, vod, detpre, energy, wes):
        """ Will update the database if row added from insert method"""
        self.c.execute(
            "UPDATE explosives SET name = ?, density = ?, \
                VOD = ?, Deton_Pressure =?, Energy = ?, \
                    Weigth_S = ? WHERE id = ?", 
                    (name, density, vod, detpre, energy, wes, id)
                    )
        self.conn.commit()
~~~

2- Compute all variables for Kuz-Ram model

Even though one method from the app's frontend will be described here, this is not fully described here.
Please, check the [frontend-code](https://github.com/luisflarota/Blasting_Project/blob/master/frontend.py){:target="\_blank"} for more information.
~~~python
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
~~~

--- 

<h2 id = "s5"> 3. Application’s features </h2>

There are two main feature in this application:

* Handling data in the SQLite database

![db_f](https://user-images.githubusercontent.com/64980133/185801562-a66076ad-703a-4ea0-b323-af3bf8ec0b38.png)

* Getting the Kuz and Ram Curve
![db_s](https://user-images.githubusercontent.com/64980133/185801565-0618262a-b2d7-4fba-8307-7be16d0285fb.png)


---

<h2 id = "s6"> 5. Future Work Ideas </h2>

- <ins>Build the rock parameters tab </ins>. Even though it might be just a number, it would be easier to replicate the process of getting it.
- <ins>Research on how to show the explosives data in a table format</ins>.
- <ins>Get a binary file to execute the scripts</ins> Might be easier to download and run the app with one click
