import sys
from PyQt6 import QtWidgets,QtCore
class VentanaPrincipal(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ejercicio 1")
        self.setFixedSize(500, 300)
        layout = QtWidgets.QHBoxLayout(self)

        layout_izquierda = QtWidgets.QVBoxLayout()
        imagen_usuario = QtWidgets.QLabel()
        imagen_usuario.setFixedSize(100, 100)
        imagen_usuario.setStyleSheet("border: 1px solid black")
        layout_izquierda.addWidget(imagen_usuario)

        descripcion = QtWidgets.QPlainTextEdit()
        descripcion.setPlainText("")
        layout_izquierda.addWidget(descripcion)
        layout.addLayout(layout_izquierda)

        # Crea una lista para mostrar los atributos,(como no pedia la funcionalidad solamente le coloque atributo estatico)
        lista_atributos = QtWidgets.QListWidget()
        lista_atributos.addItems(["Atributo 1", "Atributo 2", "Atributo 3"])
        layout.addWidget(lista_atributos)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())