/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tallerrepaso2;

import java.util.ArrayList;

/**
 *
 * @author Administrador
 */
public class TablaCifrado {
    public static ArrayList<String> datos= new ArrayList<>();
    public static ArrayList<CaracterCifrado> cifrado= new ArrayList<>();    
    
    public void addCipher(String added){
        datos.add(added);
        String[] hola= added.split("-");
        for (int x=0; x<cifrado.size(); x++)
            if (hola[0].equals(cifrado.get(x).getA())){
                datos.remove(x);
                cifrado.remove(x);                
            }                            
        cifrado.add(new CaracterCifrado(hola[0], hola[1]));
        
    }
    public boolean checkVality(){
        boolean value=true;
        for(int x=0; x<cifrado.size()-1; x++)
            for (int y=x+1; y<cifrado.size(); y++)
                if (cifrado.get(x).getB().equals(cifrado.get(y).getB()))
                        value=false;                    
        return value;
    }
    public String cipherLine(String line){
        String listo="";
        if (!checkVality()) System.out.println("La tabla esta mal hecha");
        for (int x=0; x<line.length(); x++){
            boolean check=true; //Evitar que se sumen dos caracteres
            String caracter = Character.toString(line.charAt(x));
            for (int y=0; y<cifrado.size(); y++){                
                if (check && cifrado.get(y).getA().equals(caracter)){
                    listo+=cifrado.get(y).getB();
                    check=false;                    
                }
            }
            if (check) listo+=line.charAt(x);
        }
        return listo;
    }
    
    public String unCipherLine(String line){
        String listo="";
        if (!checkVality()) return null;
        for (int x=0; x<line.length(); x++){
            boolean check=true; //Evitar que se sumen dos caracteres
            String caracter = Character.toString(line.charAt(x));
            for (int y=0; y<cifrado.size(); y++){                
                if (check && cifrado.get(y).getB().equals(caracter)){
                    listo+=cifrado.get(y).getA();
                    check=false;                    
                }
            }
            if (check) listo+=line.charAt(x);
        }
        return listo;
    }
    public void Restart(){
        datos=new ArrayList<>();
        cifrado= new ArrayList<>();    
    }
    
}
