/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Rectangle2D;

/**
 *
 * @author julian
 */
public class LlaveActual extends ObjetoGrafico {
    



    public LlaveActual(double x, double y, double width, double height) {
        super(x,y,width,height,290,100);
    } 
    

    
    @Override
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setFont(new Font("sans", Font.BOLD, 40 ));
        graphics2D.drawString("Llave Actual", 0,60);  
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }
    
    
}
