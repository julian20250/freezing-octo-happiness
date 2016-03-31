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
public class LlaveAmarilla {
    private final double totalWidth = 150d;
    private final double totalHeight= 270d;

    //Posicion, ancho y alto en el escenario
    private double x,y;
    private double width, height;
    
    //Escalas
    private double escalaX, escalaY;

    public LlaveAmarilla(double x, double y, double width, double height) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.escalaX = width / totalWidth;
        this.escalaY = height / totalHeight;
    } 
    

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    public double getEscalaX() {
        return escalaX;
    }

    public double getEscalaY() {
        return escalaY;
    }
    
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Contorno Anillo
        graphics2D.setColor(new Color(255,255, 0));
        graphics2D.fill(new Ellipse2D.Double(30d, 0d, 100d, 105d));

        //Anillo Central
        graphics2D.setColor(new Color(0, 0, 0));
        graphics2D.fill(new Ellipse2D.Double(50d, 20d, 60d, 65d));

        //Salida Llave
        graphics2D.setColor(new Color(255, 255, 0));
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
