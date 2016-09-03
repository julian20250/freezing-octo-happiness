/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package inmoviliariak;

import java.util.ArrayList;
import java.util.Scanner;

/**
 *
 * @author felipe
 */
public class MenuInmoviliariaK {
    private ArrayList<Inmueble> l=new ArrayList<>();
    private double valoresVenta=0;
    private double valoresGanancia=0;
    private double totalImpuestos=0;
    public static void main(String[] args) {
        MenuInmoviliariaK menu = new MenuInmoviliariaK();
        menu.desplegarMenu();
    }

    private void desplegarMenu() {
        System.out.println("--- Inmoviliaria Konrad Menu ---");
        System.out.println("Ingrese una opcion:");
        System.out.println("1. Agregar inmueble.");
        System.out.println("2. Mostrar inmuebles disponibles.");
        System.out.println("3. Vender Inmueble.");
        System.out.println("4. Dar total recaudado por ventas netas.");
        System.out.println("5. Dar impuestos pagados.");
        System.out.println("6. Dar total recaudes despues de impuestos.");
        System.out.println("7. Salir.");              
        Scanner scanner = new Scanner(System.in);
        while(true){
            System.out.print("\nEscoja > ");  
            String opcionSeleccionada = scanner.nextLine();
            switch (opcionSeleccionada){
                case "1":
                    agregarInmueble(scanner);
                    break;
                case "2":
                    mostrarInmueblesDisponibles();
                    break;
                case "3":
                    venderInmueble(scanner);
                    break;
                case "4":
                    darRecaudoNeto();
                    break;
                case "5":
                    darImpuestosPagados();
                    break;
                case "6":
                    darRecaudosDespuesDeImpuestos();
                    break;
                case "7":
                    System.exit(0);
                    break;
                default:
                    System.out.println("Opcion no implementada.");
                    break;
            }
        }
        
    }

    private void agregarInmueble(Scanner sc) {
        System.out.print("Ingrese el inmueble > ");
        guardarDatos(sc.nextLine());
    }
    
    private void mostrarInmueblesDisponibles() {
        for(Inmueble inmueble: l)
            System.out.println(inmueble);
    }
    
    private void venderInmueble(Scanner sc) {
        System.out.print("Ingrese ID > ");
        int id=sc.nextInt();
        int count=0;
        int remover=0;
        for(Inmueble inmueble: l){
            if(id==inmueble.getId()){
                System.out.print("Precio venta: "+inmueble.getValue()+". Impuestos: "+
                        inmueble.getTax());
                valoresVenta+=inmueble.getOriginalValue();
                valoresGanancia+=inmueble.getValue();
                totalImpuestos+=inmueble.getTax();
                remover=count;
                
            }                
            count++;   
        }
        l.remove(remover);
                
    }
    
    private void darRecaudoNeto() {
        System.out.println("Ha ganado "+valoresVenta+" sin pagar impuestos");
    }
    
    private void darImpuestosPagados() {
        System.out.println("Tuvo que pagar "+totalImpuestos+" en impuestos");
    }
    
    private void darRecaudosDespuesDeImpuestos() {
        System.out.println("Su ganancia es de "+valoresGanancia+" una vez ha"+
                " pagado impuestos");
    }
    private void guardarDatos(String data){
        String[] parts=data.split("-");
        int type=Integer.parseInt(parts[1]);
        switch(type){
            case 1:
                Inmueble oficina=new Oficina(Integer.parseInt(parts[0]), type, 
                        Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Boolean.parseBoolean(parts[5]),
                        data);
                l.add(oficina);
                break;
            
            case 2:
                Inmueble viviendaCasa=new ViviendaCasa(Integer.parseInt(parts[0]), type, 
                        Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Integer.parseInt(parts[5]),
                        Boolean.parseBoolean(parts[6]),data);
                l.add(viviendaCasa);
                break;
            
            case 3:
                Inmueble viviendaApartamento=new ViviendaApartamento(Integer.parseInt(parts[0]),
                        type, Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Integer.parseInt(parts[5]),
                        Integer.parseInt(parts[6]),data);
                l.add(viviendaApartamento);
                break;       
        }
    }
}
