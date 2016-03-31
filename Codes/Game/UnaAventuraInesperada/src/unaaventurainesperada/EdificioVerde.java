/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package unaaventurainesperada;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.awt.geom.Rectangle2D;

/**
 *
 * @author usuario
 */
public class EdificioVerde {
    private final double totalWidth = 120d;
    private final double totalHeight= 290d;
    
    //Posicion, ancho y alto en el escenario
    private double x,y;
    private double width, height;
    
    //Escalas
    private double escalaX, escalaY;

    public EdificioVerde(double x, double y, double width, double height) {
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
        
        //Fundacion
        graphics2D.setColor(new Color(0,255,0));
        graphics2D.fill(new Rectangle2D.Double(0d, 0d, 120d, 290d));

        //Ventanas
        graphics2D.setColor(new Color(51,51,255));
        graphics2D.fill(new Rectangle2D.Double(10d, 0d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(80d, 0d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(10d, 50d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(80d, 50d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(10d, 100d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(80d, 10d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(10d, 150d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(80d, 150d, 30d, 30d));
        graphics2D.fill(new Rectangle2D.Double(10d, 250d, 10d, 20d));

        //Puerta
        graphics2D.setColor(new Color(102,51,0));
        graphics2D.fill(new Rectangle2D.Double(30d, 220d, 70d, 70d));
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
        
    }    
}
