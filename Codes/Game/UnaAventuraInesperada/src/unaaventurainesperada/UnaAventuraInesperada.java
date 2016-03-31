/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package unaaventurainesperada;

import java.awt.Toolkit;
import javax.swing.JFrame;

/**
 *
 * @author usuario
 */
public class UnaAventuraInesperada {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        //Instanciar el marco (la ventana) y averiguar la resolucion
        JFrame marco = new JFrame("Una Aventura Inesperada");
        int screenWidth = Toolkit.getDefaultToolkit().getScreenSize().width;
        int screenHeight = Toolkit.getDefaultToolkit().getScreenSize().height;
        
        //El escenario
        Escenario escenario = new Escenario(0, 0, screenWidth, screenHeight, marco);
        marco.add(escenario);
        marco.setSize(screenWidth, screenHeight);
        marco.setVisible(true);
    }
    
}
