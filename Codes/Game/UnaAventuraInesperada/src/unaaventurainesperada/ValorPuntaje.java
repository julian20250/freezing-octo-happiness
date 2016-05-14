/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package unaaventurainesperada;

import java.awt.Font;
import java.awt.Graphics2D;
import java.awt.geom.AffineTransform;
import java.util.ArrayList;
import java.util.TimerTask;

/**
 *
 * @author INGENIERIA
 */
public class ValorPuntaje extends TimerTask {
    private final Lost lost;
    private final double totalWidth = 290d;
    private final double totalHeight= 100d;
    public boolean continuar=true;

    //Posicion, ancho y alto en el escenario
    private double x,y;
    private double width, height;
    
    //Escalas
    private double escalaX, escalaY;
    
    public long score=20000;
    private final Escenario escenario;
    public ValorPuntaje(double x, double y, double width, double height, Escenario escenario,
            Lost lost) {
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.escalaX = width / totalWidth;
        this.escalaY = height / totalHeight;
        this.escenario = escenario;
        this.lost = lost;
    } 
    
    public void decrementar() {

            score-=10;
    }
    public void villano(){
       if (score>0){
            score-=10000;
        }else score=0;
    }
    public void ayuda(){

         score+=5000;

    }
    public void asesino(){

         score-=15000;

    }
    
    @Override
    public String toString(){
        String cadena= "";
        cadena+=score;
        return cadena;
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
        graphics2D.setFont(new Font("sans", Font.BOLD, 60 ));
        graphics2D.drawString(toString(), 0,60);
        
        
        
        
        //Volver a la traslacion y escalacion anterior
        graphics2D.setTransform(affineTransform);
    }

    @Override
    public void run() {
        if (continuar==true) decrementar();
                        
        if (score<0){
            ArrayList<ObjetoGrafico> quienes= escenario.objetosGraficos;
            for (ObjetoGrafico objetoGrafico : quienes){
                objetoGrafico.setVisible(false);
            }
            lost.setVisible(true);
        }
        escenario.repaint();
    }
    
}


