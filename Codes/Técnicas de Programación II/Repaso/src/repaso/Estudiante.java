/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package repaso;

/**
 *
 * @author Administrador
 */
public class Estudiante {
    int edad,ingresos,edad_ingreso,tiempo,semestres,parejas;
    float promedio;
    public Estudiante(int edad, float promedio, int ingresos, int tiempo, 
            int edad_ingreso, int semestres, int parejas) {        
        this.edad=edad;
        this.promedio=promedio;
        this.ingresos=ingresos;
        this.tiempo=tiempo;
        this.edad_ingreso=edad_ingreso;
        this.semestres=semestres;
        this.parejas=parejas;
    }
    
    void PrintInfo(){
        System.out.println("Edad: "+edad);
        System.out.println("Promedio: "+promedio);
        System.out.println("Ingresos semanales: "+ingresos);
        System.out.println("Tiempo para llegar a la Universidad: "+tiempo);
        System.out.println("Edad de ingreso: "+edad_ingreso);
        System.out.println("Semestres matriculados: "+semestres);
        System.out.println("Parejas sexuales: "+parejas);
    }
}
