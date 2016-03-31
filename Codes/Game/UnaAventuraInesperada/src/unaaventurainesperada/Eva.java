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
public class Eva {
    //Ancho y Alto total de la figura
    private final double totalWidth = 135d; //private no se deja ver
    private final double totalHeight= 280d; //final, la variable no se podra
    //cambiar
    
    //Posicion, ancho y alto en el escenario
    private double x,y;
    private double width, height;
    
    //Escalas
    private double escalaX, escalaY;

    public Eva(double x, double y, double width, double height) {
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
        
        //Cabeza
        graphics2D.setColor(new Color(255,180,180));
        graphics2D.fill(new Ellipse2D.Double(24d, 0d, 80d, 80d));

        //Cabello
        graphics2D.setColor(new Color(0,0,0));
        graphics2D.fill(new Rectangle2D.Double(10d, 0d, 25d, 96d));
        graphics2D.fill(new Rectangle2D.Double(25d, 0d, 85d, 30d));
        graphics2D.fill(new Rectangle2D.Double(103d, 0d, 25d, 80d));

        //Ojos
        graphics2D.setColor(new Color(0,255,0));
        graphics2D.fill(new Rectangle2D.Double(50d,40d,10d,10d));
        graphics2D.fill(new Rectangle2D.Double(80d,40d,10d,10d));

        //Boca
        graphics2D.setColor(new Color(250,0,0));
        graphics2D.fill(new Rectangle2D.Double(55d,60d,30d,5d));
        graphics2D.fill(new Rectangle2D.Double(55d,65d,30d,5d));

        //Cuerpo
        graphics2D.setColor(new Color(252,33,123));
        graphics2D.fill(new Ellipse2D.Double(40d, 90d, 59d, 98d));

        //Cuello
        graphics2D.setColor(new Color(255,180,180));
        graphics2D.fill(new Rectangle2D.Double(62d,77d,13d,13d));

        //Hombros
        graphics2D.setColor(new Color(252,33,123));
        graphics2D.fill(new Rectangle2D.Double(34d,90d,25d,15d));
        graphics2D.fill(new Rectangle2D.Double(85d,90d,25d,15d));

        //Brazos
        graphics2D.setColor(new Color(255,180,180));
        graphics2D.fill(new Rectangle2D.Double(34d,105d,12d,55d));
        graphics2D.fill(new Rectangle2D.Double(98d,105d,12d,55d));

        //Manos
        graphics2D.fill(new Ellipse2D.Double(30d, 160d, 20d, 10d));
        graphics2D.fill(new Ellipse2D.Double(95d, 160d, 20d, 10d));


        //Falda
        graphics2D.setColor(new Color(234,123,231));
        int[] lineax= {50,95,115,80,55,35};
        int[] lineay= {180,180,200,200,200,200};
        graphics2D.fillPolygon(lineax, lineay, lineax.length);

        //Piernas
        graphics2D.setColor(new Color(255,180,180));
        graphics2D.fill(new Rectangle2D.Double(55d,200d,10d,65d));
        graphics2D.fill(new Rectangle2D.Double(80d,200d,10d,65d));

        //Zapatos
        graphics2D.setColor(new Color(255,100,180));
        graphics2D.fill(new Ellipse2D.Double(50d, 265d, 25d, 15d));
        graphics2D.fill(new Ellipse2D.Double(75d, 265d, 25d, 15d));
         //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);

    }
    
}