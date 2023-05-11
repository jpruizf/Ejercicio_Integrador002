import csv

class Alumno:
    __dni: str
    __apellido: str
    __nombre: str
    __carrera: str
    __anioquecursa: int
    def __init__(self,dnix,ape,nom,car,anioquecursa):
        self.__dni = dnix
        self.__apellido = ape
        self.__nombre = nom
        self.__carrera = car
        self.__anioquecursa = anioquecursa
    def __str__(self):
        return f"{self.__dni} | {self.__apellido} {self.__nombre} | {self.__carrera} | {self.__anioquecursa}"
    def obtener_dni(self):
        return self.__dni
    def obtener_apellido(self):
        return self.__apellido
    def obtener_nombre(self):
        return self.__nombre
    def obtener_anio(self):
        return self.__anioquecursa
class MateriasAprobadas:
    __dni: str
    __nombreMateria: str
    __fecha: str
    __nota: int
    __aprobacion:chr
    def __init__(self,dnix,auxmateria,auxfecha,auxnota,auxaprob):
        self.__dni = dnix
        self.__nombreMateria = auxmateria
        self.__fecha = auxfecha
        self.__nota = auxnota
        self.__aprobacion = auxaprob
    def obtener_nota(self):
        return self.__nota
    def __str__(self):
        return f"{self.__dni} | {self.__nombreMateria} | {self.__fecha} | {self.__nota} | {self.__aprobacion}"
    def obtener_dni(self):
        return self.__dni
    def obtener_materia(self):
        return self.__nombreMateria
    def obtener_fecha(self):
        return self.__fecha
class Gestor_materias:
    __lista_materias: list
    def __init__(self):
        self.__lista_materias = []
    def cargar_materias(self, dnix,auxmateria,auxfecha,auxnota,auxaprob):
        materia = MateriasAprobadas(dnix,auxmateria,auxfecha,auxnota,auxaprob)
        self.__lista_materias.append(materia)
        print(materia)
    #Defino esta funcion para contar cuantas veces coincide el dni del alumno
    def contar(self,dniaux):
        cont = 0
        for materia in self.__lista_materias:
            if  materia.obtener_dni() == dniaux:
                cont += 1
        return cont
    def sumar_notas(self):
        sumar = 0
        auxnota = 0
        for materia in self.__lista_materias:
            auxnota = materia.obtener_nota()
            if auxnota.isdigit():
                sumar += int(auxnota)
        return sumar
    def calcular_promedio(self,cont):
        sumar = self.sumar_notas()
        if cont != 0:
            auxpromedio = sumar // cont
        else:
            auxpromedio = 0
        return auxpromedio
    def mostrar_auxpromedio(self,aux):
        return aux

    #Defino funcion de calculo promedio sin aplazo
    def sumar_notas_sinAplazo(self):
        sumar = 0
        for materia in self.__lista_materias:
            auxnota = materia.obtener_nota()
            if materia.obtener_dni() == self.__lista_materias[0] and int(materia.obtener_nota()) >= 4:
                if auxnota.isdigit():
                    sumar += int(auxnota)
        return sumar
    def calcular_promedio_sinAplazo(self,cont):
        sumar = self.sumar_notas_sinAplazo()
        if cont != 0:
            prom = sumar // cont
        else:   
            prom = 0
        return prom
    def mostrar_promedioSinAplazo(self,aux2):
        return aux2
    def __eq__(self,aux000):
        for materia in self.__lista_materias:
            aux01 = materia.obtener_materia()
        return aux000 == aux01
    def enviar_fecha(self):
        for materia in self.__lista_materias:
            return materia.obtener_fecha()
class Gestor_alumnos:
    __lista_alumnos: list
    def __init__(self):
        self.__lista_alumnos = []
    def cargar_alumno(self,auxidni,auxapellido,auxnombre,auxcarrera,auxanio):
        alumno = Alumno(auxidni,auxapellido,auxnombre,auxcarrera,auxanio)
        self.__lista_alumnos.append(alumno)
        print(self.__str__())
    def __str__(self):
        alumnos_str = "\n".join(str(alumno) for alumno in self.__lista_alumnos)
        return f"{alumnos_str}"
    def dibujar_tabla(self,auxfecha0):
        tabla_alumnos = []
        for alumno in self.__lista_alumnos:
            aux001 = alumno.obtener_dni()
            aux002 = alumno.obtener_apellido()
            aux003 = alumno.obtener_nombre()
            aux004 = alumno.obtener_anio()
            datos = (aux001,aux002,aux003,aux004,auxfecha0,)
            tabla_alumnos.append(datos)
        return tabla_alumnos
    def mostrar_tabla(self,auxtabla:list):
        i = 0
        for i in auxtabla:
            print(f"\t {auxtabla}")
    def tabla_ordenada(self,auxtabla:list):
        for alumno in range(1, len(auxtabla)):
            key = auxtabla[alumno]
            j = alumno-1
        while  j >= 0 and auxtabla[j] > key:
            auxtabla[j+1] = auxtabla[j]
            j -= 1
            auxtabla[j+1] = key
        return auxtabla


#Algoritmo principal
if __name__ == '__main__':
    bandera = True
    gestor_alumnos = Gestor_alumnos()
    with open('alumnos.csv','r',encoding='utf-8') as archivo:
        lector = csv.reader(archivo,delimiter=';')
        for fila in lector:
            dni = str(fila[0].split()[0])
            apellido = str(fila[1].split()[0])
            nombre = str(fila[2].split()[0])
            carrera = str(fila[3].split()[0])
            anio = (fila[4].split()[0])
            gestor_alumnos.cargar_alumno(dni,apellido,nombre,carrera,anio)
    gestor_materias = Gestor_materias()
    with open('materiasAprobadas.csv','r',encoding='utf-8') as archivo:
        lector = csv.reader(archivo,delimiter=';')
        for fila in lector:
            dni = str(fila[0].split()[0])
            nombreMateria = str(fila[1].split()[0])
            fecha = (fila[2].split()[0])
            nota = (fila[3].split()[0])
            aprobacion = (fila[4].split()[0])
            gestor_materias.cargar_materias(dni,nombreMateria,fecha,nota,aprobacion)
            while bandera == True:
                print("***********/BIENVENIDO MENU DE OPCIONES/***********")
                print("1 >> Ingresar un dni de un alumno y ver el promedio y el promedio sin aplazo")
                print("2 >> Ingrese el nombre de una materia e informar los estudiantes aprobados como promocional las materias")
                print("3 >> Ver listado de alumnos en orden del año y en orden alfabetico")
                print("4 >> Finalizar operacion")
                opcion = input("Eliga una de las opciones dadas >> ")
                if opcion == '1':
                    auxdni = 0
                    auxdni = input(str("Ingrese DNI del alumno >> "))
                    total = gestor_materias.contar(auxdni)
                    calificacion2 = gestor_materias.calcular_promedio_sinAplazo(total)
                    calificacion = gestor_materias.calcular_promedio(total)
                    print(f"Promedio {gestor_materias.mostrar_auxpromedio(calificacion)}")
                    print(f"Promedio sin aplazo {gestor_materias.mostrar_promedioSinAplazo(calificacion2)}")
                elif opcion == '2':
                    auxmateria00 = ""
                    auxmateria00 = input("Ingrese el nombre de una materia --> ")
                    gestor_materias.__eq__(auxmateria00)
                    valor = gestor_materias.enviar_fecha()
                    tabla:list
                    tabla = gestor_alumnos.dibujar_tabla(valor)
                    gestor_alumnos.mostrar_tabla(tabla)
                elif opcion == '3':
                    tabla = gestor_alumnos.tabla_ordenada(tabla)
                    gestor_alumnos.mostrar_tabla(tabla)
                elif opcion == '4':
                    bandera = False
                else:
                    print("¡Ingrese una opcion valida!")