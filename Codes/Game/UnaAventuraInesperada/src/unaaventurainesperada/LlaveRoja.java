/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package unaaventurainesperada;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Rectangle2D;

/**
 *
 * @author usuario
 */
public class LlaveRoja extends ObjetoGrafico {


    public LlaveRoja(double x, double y, double width, double height) {
        super(x,y,width,height,150,270);
    } 
    
    @Override
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setColor(new Color(255,0,0));
        graphics2D.fill(new Ellipse2D.Double(30d, 0d, 100d, 105d));

        //Anillo Central
        graphics2D.setColor(new Color(0, 0, 0));
        graphics2D.fill(new Ellipse2D.Double(50d, 20d, 60d, 65d));

        //Salida Llave
        graphics2D.setColor(new Color(255, 0, 0));
        graphics2D.fill(new Rectangle2D.Double(70d,105d,20d,155d));
        graphics2D.fill(new Rectangle2D.Double(50d,130d,20d,20d));
        graphics2D.fill(new Rectangle2D.Double(90d,150d,20d,20d));
        graphics2D.fill(new Rectangle2D.Double(50d,180d,20d,20d));
        graphics2D.fill(new Rectangle2D.Double(90d,200d,20d,20d));
        graphics2D.fill(new Rectangle2D.Double(50d,130d,20d,20d));
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }    
}
