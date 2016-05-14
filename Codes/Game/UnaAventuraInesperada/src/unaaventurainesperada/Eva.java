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
import java.util.ArrayList;

/**
 *
 * @author usuario
 */
public class Eva extends ObjetoMovil implements Runnable {
    //Ancho y Alto total de la figura
    
    //cambiar
    
    //Posicion, ancho y alto en el escenario
    
    private int op=1;
    private final Escenario escenario;
    private final ValorPuntaje valorPuntaje;
    public boolean hate = false;
    public TipoDireccion direccion= TipoDireccion.abajo;

    
    public Eva(double x, double y, double width, double height, Escenario escenario, 
            ValorPuntaje valorPuntaje) {
        super(x,y,width,height,135,280, TipoDireccion.abajo,20);
        this.escenario=escenario;
        this.valorPuntaje=valorPuntaje;
    } 
    
    private void dibujar(Graphics2D graphics2D){
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
    }
    

    @Override
    public void dibujarDerecha(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        dibujar(graphics2D);
         //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);

    }
    @Override
    public void dibujarIzquierda(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        //graphics2D.translate(-getTotalWidth(), 0d);
        
        dibujar(graphics2D);
         //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);

    }
    @Override
    public void dibujarArriba(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        //graphics2D.translate(0d, -getTotalHeight());
        
        dibujar(graphics2D);
         //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);

    }
    @Override
    public void dibujarAbajo(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        //graphics2D.translate(0d, getTotalHeight());
        
        dibujar(graphics2D);
         //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);

    }
    public void voltear(){
        switch (op){
            case 1:
                direccion=TipoDireccion.abajo;
                break;
            case 2:
                direccion=TipoDireccion.arriba;
                break;
            case 3:
                direccion=TipoDireccion.izquierda;
                break;
            case 4:
                direccion=TipoDireccion.derecha;
                break;
        }
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
    @Override
    public void run() {
        for (;;){
            darPaso();   
            //System.err.println(direccion);
            ArrayList<ObjetoGrafico> quienes= escenario.conQuienesColisiona(this);
            for (ObjetoGrafico o: quienes){
                if (o instanceof Ricardo){
                    Ricardo ricardo = (Ricardo) o;
                    ricardo.alInicio();
                    valorPuntaje.villano();
                }
                if (o instanceof Foras){
                    valorPuntaje.asesino();
                }
                    
            }if (hate==true){
                System.out.println("HOLA");
                op=1;
                voltear();
                hate=false;
            }
             else if (x==120 && y==80 && direccion==TipoDireccion.abajo){            
                op=4;
                voltear();
            }
            else if (x==160 && y==80 && direccion==TipoDireccion.derecha){
                op=1;
                voltear();
            }
            else if (x==160 && y==120 && direccion==TipoDireccion.abajo){
                op=3;
                voltear();
            }
            else if (x==100 && y==120 && direccion==TipoDireccion.izquierda){
                op=2;
                voltear();
            }
            else if (x==100 && y==80 && direccion==TipoDireccion.arriba){
                op=4;
                voltear();
            }
            try{
                Thread.sleep(1000);               
            } catch(InterruptedException ex) { }
        }
    }

    @Override
    public void dibujarParado(Graphics2D graphics2D) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
    
    
}