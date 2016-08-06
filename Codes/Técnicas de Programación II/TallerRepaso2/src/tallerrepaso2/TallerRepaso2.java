/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tallerrepaso2;

import java.util.Scanner;

/**
 *
 * @author Administrador
 */
public class TallerRepaso2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner sc=new Scanner(System.in);
        TablaCifrado cifrado = new TablaCifrado();
        Menu.Desplegar(sc, cifrado);
    }
    
}
