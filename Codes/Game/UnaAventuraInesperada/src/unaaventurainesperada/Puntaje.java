/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

/**
 *
 * @author julian
 */
public class Puntaje extends ObjetoGrafico {


    public Puntaje(double x, double y, double width, double height) {
        super(x,y,width,height,290,120);
    } 
    

    @Override
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setFont(new Font("sans", Font.BOLD, 60 ));
        graphics2D.drawString("Puntaje", 0,60);   
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }
    
    
}
