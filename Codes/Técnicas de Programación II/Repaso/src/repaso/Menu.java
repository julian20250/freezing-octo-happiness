/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package repaso;

import java.util.Objects;
import java.util.Scanner;


/**
 *
 * @author julian
 */
public class Menu {
    private int option;
    private final Scanner sc= new Scanner(System.in);
    private Correlacion correlacion = new Correlacion();
    public Menu(int option){
        this.option = option;        
    }

    public int getOption() {
        return option;
    }

    public void setOption(int option) {
        this.option = option;
    }
    
    
    static void Options(){
        System.out.println("El Programa Consta de las siguientes opciones:");
        System.out.println("1. Ingresar Estudiante.");
        System.out.println("2. Consultar listado de estudiantes.");
        System.out.println("3. Calcular correlacion promedio - ingresos semanales.");
        System.out.println("4. Calcular correlacion promedio - tiempo viaje.");
        System.out.println("5. Calcular correlacion promedio - edad ingreso.");
        System.out.println("6. Salir.\n");
    }
    
    static void Ask(){ 
        System.out.print("\nIngrese la opcion > ");    
    }
    
    public void Start(){
        
        int count=0;
        switch (option){
            case 1:
                String dato=null;
                System.out.println("\nSi desea parar la entrada de datos, digite break;"
                        + "\nsi desea imprimir la informacion del ultimo estudiante, digite print.");                
                while (!Objects.equals("break", dato)){
                    System.out.print("Ingrese Datos > ");
                    dato=sc.nextLine();
                    if (!Objects.equals("break", dato) && !Objects.equals("print", dato)){
                        Estudiante ingresar= Correlacion.Transform(dato);
                        correlacion.lista.add(ingresar);
                        count++;
                    }
                    if (Objects.equals("print", dato) && count!=0) correlacion.lista.get(correlacion.lista.size() - 1).PrintInfo();
                }
                System.out.println("\nVolviendo al menu principal...");
                break;
                
            case 2:
                System.out.println("\nEstos son los estudiantes que ha introducido: ");
                for (int x=0; x<correlacion.lista.size(); x++)
                    System.out.println(correlacion.lista.get(x).edad+"-"+correlacion.lista.get(x).promedio+
                            "-"+correlacion.lista.get(x).ingresos+"-"+correlacion.lista.get(x).tiempo+
                            "-"+correlacion.lista.get(x).edad_ingreso+"-"+correlacion.lista.get(x).semestres+
                            "-"+correlacion.lista.get(x).parejas);
                break;
                
            case 3:
                float prom_array[]= new float[correlacion.lista.size()]; 
                int ing_array[] = new int[correlacion.lista.size()]; 
                for (int x=0; x<correlacion.lista.size(); x++) {
                    prom_array[x]=correlacion.lista.get(x).promedio;
                    ing_array[x]=correlacion.lista.get(x).ingresos;
                }
                System.out.println("La correlacion correspondiente es: "+
                        Correlacion.Correlation(prom_array, ing_array));
                
                break;
                
            case 4:
                float prom2_array[]= new float[correlacion.lista.size()]; 
                int time_array[] = new int[correlacion.lista.size()]; 
                for (int x=0; x<correlacion.lista.size(); x++) {
                    prom2_array[x]=correlacion.lista.get(x).promedio;
                    time_array[x]=correlacion.lista.get(x).tiempo;
                }
                System.out.println("La correlacion correspondiente es: "+
                        Correlacion.Correlation(prom2_array, time_array));
                break;
            
            case 5:
                float prom3_array[]= new float[correlacion.lista.size()]; 
                int begin_array[] = new int[correlacion.lista.size()]; 
                for (int x=0; x<correlacion.lista.size(); x++) {
                    prom3_array[x]=correlacion.lista.get(x).promedio;
                    begin_array[x]=correlacion.lista.get(x).edad_ingreso;
                }
                System.out.println("La correlacion correspondiente es: "+
                        Correlacion.Correlation(prom3_array, begin_array));
                break;
            
            case 6:
                Repaso.setBreaker(false);
                break;
                
            default:
                System.out.println("Opcion no implementada.");
                break;
        }
    }
    
    
}
