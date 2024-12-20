import tkinter as tk
from tkinter import ttk
from main import Main
import tkinter.messagebox

class App_Agente(tk.Tk):

    def __init__(self):
      super().__init__()
      self.title("Inicio")
      self.geometry("900x500+250+30")
      self.configure(bg="white")  # Establece un fondo
      self.lista_Producto={}
      self.nombre = tk.StringVar()
      self.dinero = tk.IntVar()
      self.tiempo = tk.IntVar()
      self.producto = tk.StringVar()
      self.cantidad= tk.IntVar()
      self.agregar_fondo()
      self.etiqueta()
      self.entrada()
      self.boton()
      self.agregar_arbol()

    def agregar_fondo(self):
       fondo = tk.PhotoImage(file="./Agente_Designer.png")
       fondo_label = tk.Label(self, image=fondo)
       fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
       fondo_label.image = fondo 

    def etiqueta(self):
        etiqueta1 = tk.Label(self, text='Lista Productos',bg="#d477ed", font=("Copperplate Gothic Bold", 22, "bold"))
        etiqueta1.place(x=519, y=70)
        etiqueta2 = tk.Label(self, text='Nombre:',bg="#d477ed", font=("Arial", 16, "bold"))
        etiqueta2.place(x=38, y=286)
        etiqueta3 = tk.Label(self, text='Dinero:',bg="#6343e8", font=("Arial", 16, "bold"))
        etiqueta3.place(x=85.2, y=352)
        etiqueta4 = tk.Label(self, text='Tiempo:',bg="#6343e8", font=("Arial", 16, "bold"))
        etiqueta4.place(x=85.2, y=404)

    def entrada(self):
      
        self.entrada_Nombre = tk.Entry(self,textvariable=self.nombre, width=25, relief = "flat", bg="#d477ed")
        self.entrada_Nombre.place(x=145.5, y=295)
        self.entrada_Dinero = tk.Entry(self,textvariable=self.dinero, width=10, relief = "flat", bg="#6343e8")
        self.entrada_Dinero.place(x=210, y=352)
        self.entrada_Tiempo = tk.Entry(self,textvariable=self.tiempo, width=10, relief = "flat", bg="#6343e8")
        self.entrada_Tiempo.place(x=210, y=404)
        self.entrada_Producto = tk.Entry(self,textvariable=self.producto, width=20, relief = "flat", bg="#6343e8")
        self.entrada_Producto.place(x=460, y=175)
        self.entrada_cantidad = tk.Entry(self,textvariable=self.cantidad, width=10, relief = "flat", bg="#6343e8")
        self.entrada_cantidad.place(x=650, y=175)
    def boton(self):
       fondo_boton="#9543e8"
       boton1 = tk.Button(self,text="Asignar",command=self.ingresarDatos, background=fondo_boton, width=15, height=1, font=("Arial", 12, "bold"))
       boton1.place(x=218, y=450)
       boton2 = tk.Button(self,text="Añadir",command=self.añadir_listaProductos, background=fondo_boton, width=10, height=1, font=("Arial", 12, "bold"))
       boton2.place(x=750, y=171.5)
       boton3 = tk.Button(self,text="Eliminar",command=self.eliminar_Producto, background=fondo_boton, width=15, height=1, font=("Arial", 12, "bold"))
       boton3.place(x=692.6, y=450)

    def ingresarDatos(self):
        #Aqui se realizarà la asignaciòn de datos que se le proporciono por la interfaz al agente
        print(self.nombre.get()) #Para obtener el valor de nombre siempre poner .get()
        print(self.dinero.get()) #Lo smismo para los demas
        print(self.tiempo.get()) #expecto lista productos ya que es un arreglo
        print(self.lista_Producto)
        main = Main()
        main.ejecutar(self.lista_Producto, self.dinero.get(),self.tiempo.get())
        
        

    def añadir_listaProductos(self):
      producto_actual = self.producto.get()  #Obtener el valor actual del StringVar
      cant= self.cantidad.get()
      if producto_actual:  #Verificar si hay un valor antes de agregarlo a la lista
        self.lista_Producto[producto_actual] = cant 
        
        self.ingresarProductos()
        print(self.lista_Producto)

        # Limpiar la entrada de producto después de agregarlo a la lista
        self.entrada_cantidad.delete(0, 'end')
        self.entrada_Producto.delete(0, 'end')  #Borra desde el índice 0 hasta el final

    def eliminar_Producto(self):
      try:
          item_seleccionado = self.tree.selection()[0]
          valores_seleccionados = self.tree.item(item_seleccionado)['values']

          if valores_seleccionados[0] in self.lista_Producto:
            del self.lista_Producto[valores_seleccionados[0]]
            self.ingresarProductos()
            print(f"Se eliminó {valores_seleccionados[0]} de la lista.")
          else:
            print(f"{valores_seleccionados[0]} no se encontró en la lista.")

      except IndexError as e:
            tkinter.messagebox.showerror("Alert!!","Seleccione una materia")
            return e

    def agregar_arbol(self):
        # Crear un objeto ttk.Treeview
      self.tree = ttk.Treeview(self, columns=("Productos","Cantidad"), show="headings")

        # Definir el ancho de la columna 
      self.tree.column("Productos", width=250)
      self.tree.column("Cantidad", width=100)
      self.tree['height'] = 9

        # Definir el encabezado de la columna
      self.tree.heading("Productos", text="Productos")
      self.tree.heading("Cantidad", text="Cantidad")

        # Agregar elementos al Treeview
      #self.ingresarProductos()
        
        # Posicionar el Treeview en la ventana
      self.tree.place(x=525.3, y=230)

    def ingresarProductos(self):
        records = self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        for key, value in self.lista_Producto.items():
            self.tree.insert('', 'end', values=(key, value))
            print(f"{key}: {value}")
      
if __name__ == "__main__":
 app = App_Agente()
 app.mainloop()
