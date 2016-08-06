/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package repaso;

import java.util.Scanner;

/**
 *
 * @author Administrador
 */
public class Repaso {

    /**
     * @param args the command line arguments
     */
    private static Menu menu;
    private static Scanner sc;
    private static boolean breaker=true;
    public static void main(String[] args) {
        sc = new Scanner(System.in);
        Menu.Options();
        menu= new Menu(0);
        while (breaker){
            Menu.Ask();
            int a=sc.nextInt();  
            menu.setOption(a);
            menu.Start();
        }
    
        
        
        
        // TODO code application logic here
    }

    public static void setBreaker(boolean breaker) {
        Repaso.breaker = breaker;
    }
    
}