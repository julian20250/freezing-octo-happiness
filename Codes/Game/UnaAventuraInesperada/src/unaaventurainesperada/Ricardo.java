/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package unaaventurainesperada;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.geom.AffineTransform;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Rectangle2D;

/**
 *
 * @author usuario
 */
public class Ricardo implements KeyListener{
    //Pasos de mi protagonista
    private final int pasoX = 20; //Tamaño del paso del protagonista en X
    private final int pasoY=20; //Tamaño del paso del protagonista en Y
    
    //Ancho y Alto total de la figura
    private final double totalWidth = 110d; //private no se deja ver
    private final double totalHeight= 290d; //final, la variable no se podra
    //cambiar
    
    //Posicion, ancho y alto en el escenario
    private double x,y;
    private double width, height;
    
    //Escalas
    private double escalaX, escalaY;
    
    //Movimiento
    private TipoDireccion direccion = TipoDireccion.parado;
    private final double longitudPaso = 20;
    private final Escenario escenario;
    
    public TipoDireccion getDireccion() {
        return direccion;
    }

    public void setDireccion(TipoDireccion direccion) {
        this.direccion = direccion;
    }
    
    public void darPaso(){
        switch(direccion){
            case derecha:
                x+= longitudPaso;
                break;
            case izquierda:
                x-=longitudPaso;
                break;
            case arriba:
                y-=longitudPaso;
                break;
            case abajo:
                y+=longitudPaso;
                break;
        }
    }
    
    
    public Ricardo(double x, double y, double width, double height, Escenario escenario) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.escalaX = width / totalWidth;
        this.escalaY = height / totalHeight;
        this.escenario = escenario;
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
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Ellipse2D.Double(25d, 0d, 70d, 75d));

        //Cabello
        graphics2D.setColor(new Color(114, 39, 39));
        graphics2D.fill(new Rectangle2D.Double(20d, 0d, 70d, 25d));
        graphics2D.fill(new Ellipse2D.Double(20d, 25d, 12d, 50d));
        graphics2D.fill(new Ellipse2D.Double(80d, 25d, 12d, 50d));

        //Cejas
        graphics2D.fill(new Rectangle2D.Double(40d, 25d, 10d, 5d));
        graphics2D.fill(new Rectangle2D.Double(60d, 25d, 10d, 5d));

        //Ojos
        graphics2D.setColor(new Color(255, 0, 0));
        graphics2D.fill(new Ellipse2D.Double(40d, 30d, 10d, 10d));
        graphics2D.fill(new Ellipse2D.Double(60d, 30d, 10d, 10d));

        //Nariz
        graphics2D.setColor(new Color(0, 0, 0));
        int[] lineax= {55, 60, 40};
        int[] lineay= {40, 50, 50};
        graphics2D.fillPolygon(lineax, lineay, lineax.length);

        //Boca
        graphics2D.setColor(new Color(125, 0, 0));
        graphics2D.fill(new Rectangle2D.Double(50d, 60d, 15d, 10d));

        //Cuerpo
        graphics2D.setColor(new Color(0,0,255));
        graphics2D.fill(new Ellipse2D.Double(28d,82d,65d,116d));

        //Cuello
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Rectangle2D.Double(50d, 80d, 15d, 10d));

        //Hombros
        graphics2D.setColor(new Color(232,132,231));
        graphics2D.fill(new Rectangle2D.Double(20d,85d,19d,15d));
        graphics2D.fill(new Rectangle2D.Double(80d,85d,19d,15d));

        //Brazos
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Rectangle2D.Double(20d,100d,10d,60d));
        graphics2D.fill(new Rectangle2D.Double(85d,100d,10d,60d));

        //Manos
        graphics2D.fill(new Ellipse2D.Double(15d,160d,20d,10d));
        graphics2D.fill(new Ellipse2D.Double(80d,160d,20d,10d));

        //Cintura
        graphics2D.setColor(new Color(111,222,123));
        graphics2D.fill(new Ellipse2D.Double(39d,177d,40d,40d));

        //Piernas
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Rectangle2D.Double(40d,210d,15d,70d));
        graphics2D.fill(new Rectangle2D.Double(65d,210d,15d,70d));

        //Zapatos
        graphics2D.setColor(new Color(0,0,0));
        graphics2D.fill(new Ellipse2D.Double(35d,270d,25d,10d));
        graphics2D.fill(new Ellipse2D.Double(60d,270d,25d,10d));
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    
    }
    
    //**
    // Incrementa un paso en X
    //        */
    public void incX(){
        x += pasoX;
    }
    //**
    // Decrementa un paso en X
    //        */
    public void decX(){
        x -= pasoX;
    }  
    //**
    // Incrementa un paso en Y
    //        */
    public void incY(){
        x += pasoX;
    }
    //**
    // Decrementa un paso en Y
    //        */
    public void decY(){
        x -= pasoX;
    }    

    @Override
    public void keyTyped(KeyEvent e) {
        
    }

    @Override
    public void keyPressed(KeyEvent e) {
        int tecla= e.getKeyCode();
        
        switch(tecla){
            case KeyEvent.VK_RIGHT:
                setDireccion(TipoDireccion.derecha);
                break;
            case KeyEvent.VK_LEFT:
                setDireccion(TipoDireccion.izquierda);
                break;
            case KeyEvent.VK_UP:
                setDireccion(TipoDireccion.arriba);
                break;
            case KeyEvent.VK_DOWN:
                setDireccion(TipoDireccion.abajo);
                break;
            default:
                setDireccion(TipoDireccion.parado);
                break;
        }
        
        darPaso();
        escenario.repaint();
    }

    @Override
    public void keyReleased(KeyEvent e) {
        
    }
    
}
