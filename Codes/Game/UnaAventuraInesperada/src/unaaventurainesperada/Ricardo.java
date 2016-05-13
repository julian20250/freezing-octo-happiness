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
import java.util.ArrayList;

/**
 *
 * @author usuario
 */
public class Ricardo extends ObjetoMovil implements KeyListener{
    //Pasos de mi protagonista
    private final int pasoX = 20; //Tamaño del paso del protagonista en X
    private final int pasoY=20; //Tamaño del paso del protagonista en Y
    private final LlaveVerde v_contador;
    private final LlaveAzul b_contador;
    private final LlaveRoja r_contador;
    private final ValorPuntaje valorPuntaje;
    private final Foras foras;
    private final Eva eva;
    private final Lost lost;
    private final LlaveAmarilla a_contador;
    private final Won won;
    private final TiempoRestante tiempoRestante;
    
    private boolean tok1=false;
    private boolean tok2=false;
    private boolean tok3=false;
    private boolean tok4=false;
    //Ancho y Alto total de la figura
    //private final double totalWidth = 110d; //private no se deja ver
    //private final double totalHeight= 290d; //final, la variable no se podra
    //cambiar
    
    //Posicion, ancho y alto en el escenario
    
    
    //Movimiento
    private final Escenario escenario; 
   
    
    public Ricardo(double x, double y, double width, double height, Escenario escenario, LlaveVerde v_contador,
            LlaveAzul b_contador, LlaveRoja r_contador, LlaveAmarilla a_contador,
            ValorPuntaje valorPuntaje, Foras foras, Eva eva, Lost lost, TiempoRestante tiempoRestante,
            Won won) {
        super(x,y,width,height,110d,290d, TipoDireccion.parado, 20);
        this.escenario = escenario;
        this.v_contador=v_contador;
        this.a_contador=a_contador;
        this.b_contador=b_contador;
        this.r_contador=r_contador;
        this.valorPuntaje=valorPuntaje;
        this.foras = foras;
        this.eva=eva;
        this.lost=lost;
        this.tiempoRestante=tiempoRestante;
        this.won =won;
    } 
    

    
    @Override
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
        LlaveAmarilla llaveAmarilla = null;
        LlaveAzul llaveAzul = null;
        LlaveRoja llaveRoja = null;
        LlaveVerde llaveVerde=null;
        ArrayList<ObjetoGrafico> todos =escenario.objetosGraficos;
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
            case KeyEvent.VK_R:
                for (ObjetoGrafico objetoGrafico : todos){
                objetoGrafico.setVisible(true);
                }
                lost.setVisible(false);
                alInicio();
                eva.setX(120d);
                eva.setY(0d);
                valorPuntaje.score=20000;
                tiempoRestante.minutos=1;
                tiempoRestante.segundos=30;
                break;
            default:
                setDireccion(TipoDireccion.parado);
                break;
        }
        
        darPaso();
        ArrayList<ObjetoGrafico> quienes= escenario.conQuienesColisiona(this);
        for (ObjetoGrafico o: quienes){
            if (o instanceof EdificioGris){
                devolver(o);
            }else if (o instanceof LlaveAmarilla){
                llaveAmarilla= (LlaveAmarilla) o;                
            }else if (o instanceof LlaveAzul){
                llaveAzul= (LlaveAzul) o;
            }else if (o instanceof LlaveRoja){
                llaveRoja= (LlaveRoja) o;
            }
            else if (o instanceof LlaveVerde){
                llaveVerde= (LlaveVerde) o;
            }else if (o instanceof EdificioVerde){
                if (!tok1){
                    devolver(o);
                }
            }else if (o instanceof EdificioAzul){
                if (!tok2){
                    devolver(o);
                }
            } else if (o instanceof EdificioAmarillo){
                if (!tok3){
                    devolver(o);
                }
            } else if (o instanceof EdificioRojo){
                if (!tok4){
                    devolver(o);
                }
            }else if (o instanceof Eva){
                alInicio2(o);
                valorPuntaje.villano();
            }else if (o instanceof Foras){
                foras.random();
                valorPuntaje.ayuda();
            }else if (o instanceof CasaRicardo){
                

                for (ObjetoGrafico objetoGrafico : todos){
                    objetoGrafico.setVisible(false);
                }
                won.setVisible(true);
            }              
        }
        if (llaveAmarilla !=null){
            llaveAmarilla.setColisionable(false);
            llaveAmarilla.setVisible(false);
            b_contador.setVisible(false);
            a_contador.setVisible(true);
            tok3= true;

        }
        if (llaveAzul !=null){
            llaveAzul.setColisionable(false);
            llaveAzul.setVisible(false);
            v_contador.setVisible(false);
            b_contador.setVisible(true);
            tok2=true;

        }
        if (llaveVerde !=null){
            llaveVerde.setColisionable(false);
            llaveVerde.setVisible(false);
            v_contador.setVisible(true);
            tok1=true;
            

        }
        if (llaveRoja !=null){
            llaveRoja.setColisionable(false);
            llaveRoja.setVisible(false);
            a_contador.setVisible(false);
            r_contador.setVisible(true);
            tok4= true;

        }
        escenario.repaint();
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
    public void keyReleased(KeyEvent e) {
        
    }

    @Override
    public void dibujarDerecha(Graphics2D graphics2D) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void dibujarIzquierda(Graphics2D graphics2D) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void dibujarArriba(Graphics2D graphics2D) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void dibujarAbajo(Graphics2D graphics2D) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    @Override
    public void dibujarParado(Graphics2D graphics2D) {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }

    
    @Override
    public void run() {
        throw new UnsupportedOperationException("Not supported yet."); //To change body of generated methods, choose Tools | Templates.
    }
    
}
