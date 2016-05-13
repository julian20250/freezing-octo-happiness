/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;

/**
 *
 * @author INGENIERIA
 */
public class Lost extends ObjetoGrafico {
     public Lost(double x, double y, double width, double height) {
        super(x,y,width,height,290,120);
    } 
    

    @Override
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setFont(new Font("sans", Font.BOLD, 30 ));
        graphics2D.drawString("You lost...", 0,60);
        graphics2D.drawString("R to restart", 0,80);   
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }
    
}
