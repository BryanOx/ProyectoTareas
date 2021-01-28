from tkinter import *
from tkinter import ttk
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Tareas(Base):
    __tablename__ = 'Tareas'

    ID = Column(Integer, primary_key=True)
    Fecha = Column(String(10))
    Hora = Column(String(5))
    Descripcion = Column(String(50))

class AdministradorTareas(object):
    def __init__(self):

        #   CONEXIÓN CON BASE DE DATOS
        engine = create_engine('sqlite:///tareas.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

        self.raiz = Tk()
        self.raiz.title("Administrador de Tareas")
        self.raiz.geometry("600x600")
        self.raiz.iconbitmap("icoHD.ico")
        self.raiz.resizable(0,0)

        style = ttk.Style()
        style.configure("TFrame", background="#0f0f0f")
        style.configure("TLabel", foreground="White", background="#0f0f0f")
        style.configure("Add.TButton", foreground="black", background="lime")
        style.configure("Erase.TButton", foreground="black", background="red")

        self.frame = ttk.Frame(self.raiz, style="TFrame")
        self.frame.pack(fill=BOTH, expand=True)

        self.label0 = ttk.Label(self.frame, text="Tareas programadas:", style="TLabel")
        self.label0.grid(row=0, column=2, columnspan=3)

        self.fechaTar = ttk.Label(self.frame, text="Fecha prog.", style="TLabel")
        self.fechaTar.grid(row=1, column=0)

        self.horaTar = ttk.Label(self.frame, text="Hora prog.", style="TLabel")
        self.horaTar.grid(row=1, column=1)

        self.descripcionTar = ttk.Label(self.frame, text="Descripcion", style="TLabel")
        self.descripcionTar.grid(row=1, column=2, columnspan=4)

        self.botonADD = ttk.Button(self.frame, text="Agregar tarea", style="Add.TButton")
        self.botonADD.grid(row=1, column=7, padx=20)

        self.botonERASE = ttk.Button(self.frame, text="Borrar tarea", style="Erase.TButton")
        self.botonERASE.grid(row=1, column=8)

        #   CREACION DE LABELS CON DESCRIPCION, FECHA Y HORA PARA LAS TAREAS SEGUN TAR. GUARDADAS EN DB

        tareas = self.session.query(Tareas).all()
        fila = 1
        for tarea in tareas:
            #print(tarea,f"\nFecha: {tarea.Fecha}\nHora: {tarea.Hora}\nDescripcion: {tarea.Descripcion}\n")
            labelF = ttk.Label(self.frame, text=f"{tarea.Fecha}", style="TLabel")
            labelF.grid(row=1+fila, column=0)

            labelH = ttk.Label(self.frame, text=f"{tarea.Hora}", style="TLabel")
            labelH.grid(row=1+fila, column=1)

            labelD = ttk.Label(self.frame, text=f"{tarea.Descripcion}", style="TLabel")
            labelD.grid(row=1+fila, column=2)
            
            fila += 1

        self.raiz.mainloop()

if __name__ == "__main__":
    app = AdministradorTareas()