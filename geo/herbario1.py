import sqlite3

# Configurar la conexión a la base de datos SQLite
DATABASE = 'hervario.db'

# Obtener la conexión a la base de datos
def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

# Crear la tabla 'plantas' si no existe
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS plantas (
        codigo INTEGER PRIMARY KEY,
        titulo_planta TEXT NOT NULL,
        nombres_vulgares TEXT NOT NULL,
        nombre_cientifico TEXT NOT NULL,
        identificacion TEXT NOT NULL,
        forma_biologica TEXT NOT NULL,
        floracion TEXT NOT NULL,
        imagen_nota TEXT NOT NULL,
        descripcion_imagen_nota TEXT NOT NULL,
        requerimientos_ambientales TEXT NOT NULL,
        distribucion_y_zonas_de_cultivo TEXT NOT NULL,
        implantacion_y_persistencia TEXT NOT NULL,
        comentarios TEXT NOT NULL,
        videos TEXT NOT NULL,
        imagen188x600 TEXT NOT NULL,
        imagen660x1280 TEXT NOT NULL,
        descripcion_home TEXT NOT NULL
    )
''')
conn.commit()
cursor.close()
conn.close()



# -------------------------------------------------------------------
# Definimos la clase "Plantas"
# -------------------------------------------------------------------
'''class Plantas:
    def __init__(self, codigo, nombres_vulgares, cantidad, precio):
         self.codigo = codigo
        self.nombres_vulgares = nombres_vulgares
        self.cantidad = cantidad
        self.precio = precio




# -------------------------------------------------------------------
# Definimos la clase "Inventario"
# -------------------------------------------------------------------
class herbario:
    def __init__(self):
        self.conexion = get_db_connection()
        self.cursor = self.conexion.cursor()

    def agregar_planta(self, codigo, descripcion, cantidad, precio):
        producto_existente = self.consultar_producto(codigo)
        if producto_existente:
            print("Ya existe un producto con ese código.")
            return False

        nuevo_producto = Producto(codigo, descripcion, cantidad, precio)
        self.cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?)", (codigo, descripcion, cantidad, precio))
        self.conexion.commit()
        return True

    def consultar_producto(self, codigo):
        self.cursor.execute("SELECT * FROM productos WHERE codigo = ?", (codigo,))
        row = self.cursor.fetchone()
        if row:
            codigo, descripcion, cantidad, precio = row
            return Producto(codigo, descripcion, cantidad, precio)
        return False

    def modificar_producto(self, codigo, nueva_descripcion, nueva_cantidad, nuevo_precio):
        producto = self.consultar_producto(codigo)
        if producto:
            producto.modificar(nueva_descripcion, nueva_cantidad, nuevo_precio)
            self.cursor.execute("UPDATE productos SET descripcion = ?, cantidad = ?, precio = ? WHERE codigo = ?",
                                (nueva_descripcion, nueva_cantidad, nuevo_precio, codigo))
            self.conexion.commit()

    def listar_productos(self):
        print("-" * 30)
        self.cursor.execute("SELECT * FROM productos")
        rows = self.cursor.fetchall()
        for row in rows:
            codigo, descripcion, cantidad, precio = row
            print(f"Código: {codigo}")
            print(f"Descripción: {descripcion}")
            print(f"Cantidad: {cantidad}")
            print(f"Precio: {precio}")
            print("-" * 30)

    def eliminar_producto(self, codigo):
        self.cursor.execute("DELETE FROM productos WHERE codigo = ?", (codigo,))
        if self.cursor.rowcount > 0:
            print("Producto eliminado.")
            self.conexion.commit()
        else:
            print("Producto no encontrado.")


# -------------------------------------------------------------------
# Definimos la clase "Carrito"
# -------------------------------------------------------------------
class Carrito:
    def __init__(self):
        self.conexion = sqlite3.connect('inventario.db')  # Conexión a la base de datos
        self.cursor = self.conexion.cursor()
        self.items = []

    def agregar(self, codigo, cantidad, inventario):
        producto = inventario.consultar_producto(codigo)
        if producto is False:
            print("El producto no existe.")
            return False
        if producto.cantidad < cantidad:
            print("Cantidad en stock insuficiente.")
            return False

        for item in self.items:
            if item.codigo == codigo:
                item.cantidad += cantidad
                self.cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE codigo = ?",
                                    (cantidad, codigo))
                self.conexion.commit()
                return True

        nuevo_item = Producto(codigo, producto.descripcion, cantidad, producto.precio)
        self.items.append(nuevo_item)
        self.cursor.execute("UPDATE productos SET cantidad = cantidad - ? WHERE codigo = ?",
                            (cantidad, codigo))
        self.conexion.commit()
        return True

    def quitar(self, codigo, cantidad, inventario): #Revisar
        for item in self.items:
            if item.codigo == codigo:
                if cantidad > item.cantidad:
                    print("Cantidad a quitar mayor a la cantidad en el carrito.")
                    return False
                item.cantidad -= cantidad
                if item.cantidad == 0:
                    self.items.remove(item)
                self.cursor.execute("UPDATE productos SET cantidad = cantidad + ? WHERE codigo = ?",
                                    (cantidad, codigo))
                self.conexion.commit()
                return True

        print("El producto no se encuentra en el carrito.")
        return False

    def mostrar(self):
        print("-" * 30)
        for item in self.items:
            print(f"Código: {item.codigo}")
            print(f"Descripción: {item.descripcion}")
            print(f"Cantidad: {item.cantidad}")
            print(f"Precio: {item.precio}")
            print("-" * 30)


# -------------------------------------------------------------------
# Ejemplo de uso de las clases y objetos definidos antes:
# -------------------------------------------------------------------
# Crear una instancia de la clase Inventario
x = Inventario()

# Crear una instancia de la clase Carrito
mi_carrito = Carrito()

# Agregar productos al inventario
x.agregar_producto(1, "Producto 1", 10, 19.99)
x.agregar_producto(2, "Producto 2", 5, 9.99)
x.agregar_producto(3, "Producto 3", 15, 29.99)

# Agregar productos al carrito
mi_carrito.agregar(1, 2, x)  # Agregar 2 unidades del producto con código 1 al carrito
mi_carrito.agregar(3, 1, x)  # Agregar 1 unidad del producto con código 3 al carrito
mi_carrito.quitar(1, 1, x)   # Quitar 1 unidad del producto con código 1 al carrito
mi_carrito.agregar(2, 1, x)  # Agregar 1 unidad del producto con código 2 al carrito

mi_carrito.mostrar()'''