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
import java.util.Random;
import java.util.List;

/**
 *
 * @author usuario
 */
public class Foras extends ObjetoMovil implements Runnable {
    private final Escenario escenario;
    public Foras(double x, double y, double width, double height, Escenario escenario) {
        super(x,y,width,height,145,280,TipoDireccion.abajo,20);
        this.escenario = escenario;
        
    } 
    
    @Override
    public void paint(Graphics2D graphics2D){
        //Transladar y escalar
        AffineTransform affineTransform = graphics2D.getTransform();
        graphics2D.translate(getX(), getY());
        graphics2D.scale(getEscalaX(), getEscalaY());
        
        //Cabeza
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Ellipse2D.Double(45d, 0d, 63d, 70d));

        //Gorro
        graphics2D.setColor(new Color(234,222,111));
        graphics2D.fill(new Ellipse2D.Double(37d, 0d, 77d, 30d));
        graphics2D.fill(new Ellipse2D.Double(30d, 5d, 23d, 65d));
        graphics2D.fill(new Ellipse2D.Double(97d, 5d, 23d, 65d));

        //Cejas
        graphics2D.setColor(new Color(114, 39, 39));
        graphics2D.fill(new Rectangle2D.Double(60d, 35d, 10d, 5d));
        graphics2D.fill(new Rectangle2D.Double(80d, 35d, 10d, 5d));

        //Ojos
        graphics2D.setColor(new Color(114, 123, 231));
        graphics2D.fill(new Rectangle2D.Double(60d, 40d, 10d, 10d));
        graphics2D.fill(new Rectangle2D.Double(80d, 40d, 10d, 10d));

        //Boca
        graphics2D.setColor(new Color(0, 0, 0));
        graphics2D.fill(new Rectangle2D.Double(65d, 60d, 20d, 5d));
        graphics2D.fill(new Rectangle2D.Double(65d, 65d, 20d, 5d));

        //Cuerpo
        graphics2D.setColor(new Color(95, 18, 18));
        graphics2D.fill(new Ellipse2D.Double(45d, 82d, 64d, 100d));

        //Cuello
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Rectangle2D.Double(65d, 75d, 19d, 13d));

        //Hombros
        graphics2D.setColor(new Color(95, 18, 18));
        graphics2D.fill(new Rectangle2D.Double(30d, 86d, 25d, 15d));
        graphics2D.fill(new Rectangle2D.Double(98d, 86d, 25d, 15d));

        //Brazos
        graphics2D.setColor(new Color(255, 180, 180));
        graphics2D.fill(new Rectangle2D.Double(30d, 100d, 13d, 60d));
        graphics2D.fill(new Rectangle2D.Double(106d, 100d, 13d, 60d));

        //Guantes
        graphics2D.setColor(new Color(95, 18, 18));
        graphics2D.fill(new Rectangle2D.Double(30d, 160d, 13d, 10d));
        graphics2D.fill(new Rectangle2D.Double(106d, 160d, 13d, 10d));

        //Cruz
        graphics2D.setColor(new Color(247, 255, 0));
        graphics2D.fill(new Rectangle2D.Double(70d, 100d, 10d, 60d));
        graphics2D.fill(new Rectangle2D.Double(60d, 120d, 30d, 10d));

        //Cintura
        graphics2D.setColor(new Color(95, 18, 18));
        graphics2D.fill(new Rectangle2D.Double(55d, 169d, 49d, 27d));

        //Piernas
        graphics2D.setColor(new Color(0, 0, 255));
        graphics2D.fill(new Rectangle2D.Double(55d, 195d, 25d, 75d));
        graphics2D.fill(new Rectangle2D.Double(80d, 195d, 25d, 75d));

        //Pies
        graphics2D.setColor(new Color(61, 23, 36));
        graphics2D.fill(new Rectangle2D.Double(45d, 270d, 35d, 10d));
        graphics2D.fill(new Rectangle2D.Double(80d, 270d, 35d, 10d)); 
         //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }

    
    
    

    synchronized public void random(){
        List<Integer> myCoordsx = new ArrayList<Integer>();
        List<Integer> myCoordsy = new ArrayList<Integer>();
        for (int i=0; i<260; i+=20){
            myCoordsx.add(i);
        }
        for (int i=0; i<180; i+=20){
            myCoordsy.add(i);
        }
        Random  rnd = new Random();
        int randomNumx = rnd.nextInt((myCoordsx.size()-1) );
        int randomNumy = rnd.nextInt((myCoordsy.size()-1) );
        x=myCoordsx.get(randomNumx);
        y=myCoordsy.get(randomNumy);
        while ((x==240 & y==140) || (x==260 & y==140) || (x==240 & y==160) || (x==260 & y==160)
                || (x==240 & y==180) || (x==260 & y==180)){
            randomNumx = rnd.nextInt((myCoordsx.size()) );
            randomNumy = rnd.nextInt((myCoordsy.size()) );
            x=myCoordsx.get(randomNumx);
            y=myCoordsy.get(randomNumy);
            
        }


        System.out.println(x);
        System.out.println(y);
              
    }
    @Override
    public void run(){
        for (;;){
            random();
            ArrayList<ObjetoGrafico> quienes= escenario.conQuienesColisiona(this);
            int tok;
             for (ObjetoGrafico o: quienes){
                 
                 tok=1;
                 if (o instanceof EdificioGris || o instanceof EdificioRojo ||
                         o instanceof EdificioVerde || o instanceof EdificioAmarillo ||
                         o instanceof EdificioAzul
                         ){                   
                    tok=0;
             }
             if (tok==1){
                   try{
                        Thread.sleep(5000);               
                    } catch(InterruptedException ex) { }  
                 }
             }
                 
            
            }
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

        
}
