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
    public ArrayList<Inmueble> l=new ArrayList<>();
    public ArrayList<Inmueble> V= new ArrayList<>();
    private double valoresVenta=0;
    private double valoresGanancia=0;
    private int sold=0;
    private double totalImpuestos=0;
    public static void main(String[] args) throws TipoInexistenteException {
        MenuInmoviliariaK menu = new MenuInmoviliariaK();
        Window window= new Window(menu);
        window.setVisible(true);
        
       // menu.desplegarMenu();
    }

    private void desplegarMenu() throws TipoInexistenteException {
        System.out.println("--- Inmoviliaria Konrad Menu ---");
        System.out.println("Ingrese una opcion:");
        System.out.println("1. Agregar inmueble.");
        System.out.println("2. Mostrar inmuebles disponibles.");
        System.out.println("3. Vender Inmueble.");
        System.out.println("4. Dar total recaudado por ventas netas.");
        System.out.println("5. Dar impuestos pagados.");
        System.out.println("6. Dar total recaudes despues de impuestos.");
        System.out.println("7. Salir.");     
        System.out.println("8. Mostrar inmueble con el precio mas bajo.");
        System.out.println("9. Estrato con mas predios en venta.");
        System.out.println("10. Conocer el numero de casas que tienen mas de 3 parqueaderos.");
        System.out.println("11. Contar cuantos inmuebles hay de un tipo determinado.");
        Scanner scanner = new Scanner(System.in);
        while(true){
            System.out.print("\nEscoja > ");  
            String opcionSeleccionada = scanner.nextLine();
            switch (opcionSeleccionada){
                case "1":
                    //try{
                    //    agregarInmueble(scanner);
                    //}catch(NumeroInadecuadoDeParametrosException ex){
                    //    ex.printStackTrace();
                    //}
                    //catch(MuchasOficinasException ex){
                    //    ex.printStackTrace();
                    //}
                    //catch(IdentificadorRepetidoException ex){
                    //    ex.printStackTrace();
                    //}catch(NoIngresoBooleanException ex){
                    //    ex.printStackTrace();
                    //}
                    break;
                case "2":
                    mostrarInmueblesDisponibles();
                    break;
                case "3":
                    //venderInmueble(scanner);
                    break;
                case "4":
                    darRecaudoNeto();
                    break;
                case "5":
                    try{
                        darImpuestosPagados();
                    }
                    catch(CeroInmueblesVendidosException ex){
                        ex.printStackTrace();
                    }
                    break;
                case "6":
                    darRecaudosDespuesDeImpuestos();
                    break;
                case "7":
                    System.exit(0);
                    break;
                case "8":
                    mostrarPrecioBajo();
                    break;
                case "9":
                    estratoMasPredios();
                    break;
                case "10":
                    numeroCasas();
                    break;
                case "11":
                    try{
                        contarInmuebles(scanner);
                    }catch (NumberFormatException ex){
                        System.out.println("No ingreso un numero. Volviendo al menu");
                    }

                    catch(TipoInexistenteException ex){
                        ex.printStackTrace();                
                    }
                    break;
                default:
                    System.out.println("Opcion no implementada. Si no ingreso"
                            + " nada, ignore esta advertencia.");
                    break;
            }
        }
        
    }

    public void agregarInmueble(String a) throws NumeroInadecuadoDeParametrosException, MuchasOficinasException,
            IdentificadorRepetidoException, NoIngresoBooleanException{
                
        guardarDatos(a);
        
    }
    
    public void mostrarInmueblesDisponibles() {
        for(Inmueble inmueble: l)
            System.out.println(inmueble);
    }
    
    public void venderInmueble(int id) {
        int count=0;
        this.sold++;
        int remover=0;
        boolean iWillRemove=false;
        for(Inmueble inmueble: l){
            if(id==inmueble.getId()){
                System.out.print("Precio venta: "+inmueble.getValue()+". Impuestos: "+
                        inmueble.getTax());
                valoresVenta+=inmueble.getValue();
                valoresGanancia+=inmueble.getValue()-inmueble.getTax();
                totalImpuestos+=inmueble.getTax();
                remover=count;
                iWillRemove=true;
            }                
            count++;   
        }
        if (iWillRemove){
            V.add(l.get(remover));
            l.remove(remover);            
        }
                
    }
    
    public String darRecaudoNeto() {
        return "Ha ganado "+valoresVenta+" sin pagar impuestos";
    }
    
    public String darImpuestosPagados() throws CeroInmueblesVendidosException {       
        if (this.sold==0)
            throw new CeroInmueblesVendidosException("No ha vendido nada.");
        return "Tuvo que pagar "+totalImpuestos+" en impuestos";

    }
    
    public String darRecaudosDespuesDeImpuestos() {
        return "Su ganancia es de "+valoresGanancia+" una vez ha"+
                " pagado impuestos";
    }
    private void guardarDatos(String data) throws NumeroInadecuadoDeParametrosException, MuchasOficinasException,
            IdentificadorRepetidoException, NoIngresoBooleanException{
        String[] parts=data.split("-");
        int type=Integer.parseInt(parts[1]);
        for (Inmueble inmueble: l)
            if (inmueble.getId()==Integer.parseInt(parts[0]))
                    throw new IdentificadorRepetidoException(parts[0]);
        switch(type){
            case 1:
                if (parts.length!=6)
                    throw new NumeroInadecuadoDeParametrosException(6,parts.length);
                int count=0;
                for(Inmueble inmueble: l)
                    if (inmueble.getTipo()==1)
                        count++;
                if (count==10)
                    throw new MuchasOficinasException("No puede ingresar mas de 10 oficinas");

                if (!parts[5].equals("true") && !parts[5].equals("false"))
                    throw new NoIngresoBooleanException(parts[5]);
                Inmueble oficina=new Oficina(Integer.parseInt(parts[0]), type, 
                        Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Boolean.parseBoolean(parts[5]),
                        data);
                l.add(oficina);
                break;

            case 2:
                if (parts.length!=7)
                    throw new NumeroInadecuadoDeParametrosException(7, parts.length);
                Inmueble viviendaCasa=new ViviendaCasa(Integer.parseInt(parts[0]), type, 
                        Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Integer.parseInt(parts[5]),
                        Boolean.parseBoolean(parts[6]),data);
                l.add(viviendaCasa);
                break;

            case 3:
                if (parts.length!=7)
                    throw new NumeroInadecuadoDeParametrosException(7, parts.length);
                Inmueble viviendaApartamento=new ViviendaApartamento(Integer.parseInt(parts[0]),
                        type, Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Integer.parseInt(parts[5]),
                        Integer.parseInt(parts[6]),data);
                l.add(viviendaApartamento);
                break;      

            case 4:
                if (parts.length!=8)
                    throw new NumeroInadecuadoDeParametrosException(8, parts.length);
                Inmueble finca= new Finca(Integer.parseInt(parts[0]), type, 
                        Integer.parseInt(parts[2]), Integer.parseInt(parts[3]),
                        Integer.parseInt(parts[4]), Integer.parseInt(parts[5]),
                        Boolean.parseBoolean(parts[6]),data,Integer.parseInt(parts[7]));
                l.add(finca);
        }                
    }

    private void mostrarPrecioBajo() {
        int position=0;
        double lestPrice=l.get(0).getOriginalValue();
        for(int ii=1; ii<l.size(); ii++){
            if (lestPrice>=l.get(ii).getOriginalValue()){
                lestPrice=l.get(ii).getOriginalValue();
                position=ii;
            }
        }
        System.out.println(l.get(position));
    }

    private void estratoMasPredios() {
        int[] estrato=new int[l.size()];
        int count=0;
        for(Inmueble inmueble: l){
                estrato[count]=inmueble.getEstrato();
                count++;
        }
        int[] repeticiones=new int[l.size()];

        for(int ii=0; ii<l.size(); ii++){
            int repe=0;
            for(int jj=0; jj<l.size();jj++)
                if(estrato[ii]==estrato[jj])
                    repe++;
            repeticiones[ii]=repe;                               
        }
        int max=0;
        int position=0;
        for(int ii=0; ii<l.size(); ii++){
            if (repeticiones[ii]>=max){
                max=repeticiones[ii];
                position=ii;
            }
        }
        System.out.println("El estrato con mas repeticiones es "+estrato[position]+
                " con "+max+" repeticiones");
    }

    private void numeroCasas() {
        for (Inmueble inmueble: l){
            if (inmueble.getTipo()==2){
                ViviendaCasa viviendaCasa=(ViviendaCasa) inmueble;
                if (viviendaCasa.getNumeroParqueaderos()>3)
                    System.out.println(viviendaCasa);
            }
        }
    }

    private void contarInmuebles(Scanner scanner) throws TipoInexistenteException, NumberFormatException{
        System.out.print("Ingrese el tipo de inmueble que desea contar > ");
        boolean flag=false;
        String type= scanner.nextLine();  
        int type_as_number=0;
        
            type_as_number=Integer.parseInt(type);                                                               
                if (type_as_number<=0 || type_as_number>4)            
                    throw new TipoInexistenteException("Se introdujo un tipo de inmueble inesperado ("+type_as_number+")");                                        
                
            int count=0;
            for (Inmueble inmueble: l)
                if (inmueble.getTipo()==type_as_number)
                    count++;
            System.out.println("Se encontraron "+count+" inmuebles de tipo "+type_as_number+".");
        
        
        
    }
}

